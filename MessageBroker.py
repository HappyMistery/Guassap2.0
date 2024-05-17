from concurrent import futures
import time
import grpc
import pika

import MessageBroker_pb2_grpc
import MessageBroker_pb2


global channel
def start():
    try:
        broker = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        MessageBroker_pb2_grpc.add_MessageBrokerServicer_to_server(MessageBrokerServicer(), broker)
        broker.add_insecure_port('localhost:50050')
        broker.start()
    except Exception as e:
        print("Server already started")
    print("The Name Server is waiting for registrations")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        broker.stop(0)
    
class MessageBrokerServicer(MessageBroker_pb2_grpc.MessageBrokerServicer):
    def SubscribeToGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=request.group_chat)
        connection.close()
        empty = MessageBroker_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return empty

    def PublishMessageToGroupChat(self, request, context):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=request.group_chat)

        channel.basic_publish(exchange='', routing_key=request.group_chat, body=request.content)
        print(f" [x] Sent {request.content}")
        connection.close()