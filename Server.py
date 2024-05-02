import time
import redis
import grpc
from concurrent import futures

import Server_pb2_grpc
import Server_pb2
from RegisterService import register_service

global port
port = 50052
global r

def start():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server_pb2_grpc.add_RegisterServiceServicer_to_server(RegisterServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # Listen on port 50051
    server.start()
    print("The Server is waiting for registrations")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
    
class RegisterServiceServicer(Server_pb2_grpc.RegisterServiceServicer):
    def register_user(self, request: Server_pb2.Request, context) -> Server_pb2.Response:
        registration = register_service.register_user(request.username)
        response = Server_pb2.Response()
        response.value.extend(registration)
        return response