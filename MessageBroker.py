from concurrent import futures
import random
import threading
import time
import grpc
import pika
import pika.exchange_type

import MessageBroker_pb2_grpc
import MessageBroker_pb2
import NameServer_pb2_grpc
import NameServer_pb2


def start():
    try:
        broker = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        MessageBroker_pb2_grpc.add_MessageBrokerServicer_to_server(MessageBrokerServicer(), broker)
        broker.add_insecure_port('localhost:50050')
        broker.start()
        global connection_events 
        connection_events = {}
    except Exception as e:
        print("MessageBroker already started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        broker.stop(0)
    
class MessageBrokerServicer(MessageBroker_pb2_grpc.MessageBrokerServicer):
    def SubscribeToGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        exchange = f"exchange_{request.group_chat}"
        queue = f"{request.group_chat}_{request.sender}"
        
        channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)

        if(request.content == 'check'):
            try:
                channel.queue_declare(queue=queue, passive=True, durable=True)
                subscription = MessageBroker_pb2.Subscription(subscribed='True')
                connection.close()
            except Exception as e:
                subscription = MessageBroker_pb2.Subscription(subscribed='False')
            return subscription
        
        channel.queue_declare(queue=queue, durable=True)
        channel.queue_bind(exchange=exchange, queue=queue)
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = NameServer_pb2_grpc.NameServerStub(channel)
            new_gc = NameServer_pb2.ChatAddress(address=request.group_chat)
            stub.UpdateGroupsList(new_gc)
        connection.close()
        subscription = MessageBroker_pb2.Subscription(subscribed='True')
        return subscription
    

    def PublishMessageToGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        exchange = f"exchange_{request.group_chat}"
        
        msg = f"{request.sender}:{request.content}"

        channel.basic_publish(exchange=exchange, routing_key='', body=msg, properties=pika.BasicProperties(delivery_mode=2,))
        connection.close()
        
        empty = MessageBroker_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty
    
    
    def ConsumeMessagesFromGroupChat(self, request, context):
        global connection_events 
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        queue = f"{request.group_chat}_{request.sender}"
        channel.queue_declare(queue=queue, durable=True)
        connection_events[queue] = threading.Event()
        connection_events[queue].set()
        connection_events[queue].wait()

        def consume_messages():
            connection_events[queue].wait()
            while not context.is_active():
                time.sleep(0.1)
            try:
                for method_frame, properties, body in channel.consume(queue=queue):
                    msg_info = body.decode().split(":", 1)
                    response = MessageBroker_pb2.ChatMessage(content=msg_info[1], sender=msg_info[0], group_chat=request.group_chat)
                    yield response
                    if(connection_events[queue].is_set() == False):
                        print(f"closing connection with group {request.group_chat}")
                        connection.close()
                        break
            except Exception as e:
                print(f"Exception {e}")
                connection.close()
                channel.close()
            finally:
                connection.close()
        
        consumer_thread = threading.Thread(target=consume_messages)
        consumer_thread.daemon = True  # Allows the program to exit even if the thread is running
        consumer_thread.start()
        consumer_thread.join()
        
        return consume_messages()
    
    def EndConsumption(self, request, context):
        queue = f"{request.group_chat}_{request.sender}"
        if(connection_events[queue].is_set()):
            connection_events[queue].clear()
        else:
            print("Cant' close connection because it's already closed")
        empty = MessageBroker_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty
        
    
    def ChatDiscovery(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = NameServer_pb2_grpc.NameServerStub(channel)
            groups = stub.GetGroupsList(NameServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
        response = MessageBroker_pb2.ChatMessage(content='', sender='', group_chat=groups.address)
        connection.close()
        return response
        

    def UseInsultChannel(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # Declare the insult queue
        queue = 'insults_queue'
        channel.queue_declare(queue=queue, durable=True)

        insults = [
            "tonto", "bastard", "desgraciat", "subnormal", 
            "idiota", "imbècil", "cretí", "patètic", 
            "estúpid", "ignorant", "inútil", "cabró", 
            "pallasso", "miserable", "tarat", "ruc", 
            "bàrbar", "neci", "babau", "malparit"
        ]

        if request.content == '':
            selected_insults = random.sample(insults, 2)
            for insult in selected_insults:
                channel.basic_publish(exchange='', routing_key=queue, body=insult)
        else:
            channel.basic_publish(exchange='', routing_key=queue, body=request.content)
        time.sleep(0.1)
        try: 
            method_frame, header_frame, insult = channel.basic_get(queue='insults_queue', auto_ack=True)
        except Exception as e:
            response = MessageBroker_pb2.ChatMessage(content='No insultis tant', sender='', group_chat='')
            connection.close()
            return response
        
        connection.close()

        response = MessageBroker_pb2.ChatMessage(content=insult, sender='', group_chat='')
        return response
        
        
        