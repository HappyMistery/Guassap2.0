import redis
import grpc
from concurrent import futures

import Server_pb2_grpc
import Server_pb2

global port
port = 50052
global r

def start():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Server_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # Listen on port 50051
    server.start()
    print("The Server is waiting for registrations")
    
class UserServiceServicer(Server_pb2_grpc.UserServiceServicer):
    def register_user(self, request: Server_pb2.RegisterRequest, context) -> Server_pb2.RegisterResponse:
        username = request.username
        if r.exists(username):
            return Server_pb2.RegisterResponse(success=False)
    
        r.set(username, port)
        return Server_pb2.RegisterResponse(success=True)