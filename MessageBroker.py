from concurrent import futures
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
    except Exception as e:
        print("MessageBroker already started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        broker.stop(0)
    
class MessageBrokerServicer(MessageBroker_pb2_grpc.MessageBrokerServicer):
    global channel
    global ns
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
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        queue = f"{request.group_chat}_{request.sender}"
        
        channel.queue_declare(queue=queue, durable=True)
        
        def consume_messages():
            #for method_frame, properties, body in channel.consume(queue=queue, auto_ack=False):
            #    msg_info = body.decode().split(":", 1)
            #    response = MessageBroker_pb2.ChatMessage(content=msg_info[1], sender=msg_info[0], group_chat=request.group_chat)
            #yield response
            
            while True:
                method_frame, properties, body = channel.basic_get(queue=queue, auto_ack=False)
                if method_frame:
                    msg_info = body.decode().split(":", 1)
                    response = MessageBroker_pb2.ChatMessage(content=msg_info[1], sender=msg_info[0], group_chat=request.group_chat)
                    yield response
                else:
                    # If no message is available, we let the rest of the program run without blocking
                    break
        #consume_thread = threading.Thread(target=consume_messages)
        #consume_thread.start()

        return consume_messages()
    
    def ChatDiscovery(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = NameServer_pb2_grpc.NameServerStub(channel)
            groups = stub.GetGroupsList(NameServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
        response = MessageBroker_pb2.ChatMessage(content='', sender='', group_chat=groups.address)
        return response
        
        
        
        