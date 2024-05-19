from concurrent import futures
import time
import grpc
import pika

import MessageBroker_pb2_grpc
import MessageBroker_pb2


def start():
    try:
        broker = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        MessageBroker_pb2_grpc.add_MessageBrokerServicer_to_server(MessageBrokerServicer(), broker)
        broker.add_insecure_port('localhost:50050')
        broker.start()
    except Exception as e:
        print("MessageBroker already started")
    print("\nThe Message Broker is waiting for messages")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        broker.stop(0)
    
class MessageBrokerServicer(MessageBroker_pb2_grpc.MessageBrokerServicer):
    global channel
    def SubscribeToGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=request.id)
        connection.close()
        empty = MessageBroker_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty

    def PublishMessageToGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        channel.basic_publish(exchange='', routing_key=request.group_chat, body=request.content)
        connection.close()
        empty = MessageBroker_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty
    
    def ConsumeMessagesFromGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=request.id)

        def consume_messages():
            print("Trying to get messages...")
            while True:
                method_frame, _, body = channel.basic_get(queue=request.id, auto_ack=True)
                if method_frame:
                    response = MessageBroker_pb2.ChatMessage(content=body.decode(), sender_username='', group_chat=request.id)
                    yield response
                else:
                    # If no message is available, sleep for a short time to avoid looping too fast
                    break

        return consume_messages()