import redis, grpc
import Server_pb2

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

port = 50052

class RegisterService:
    def register_user(self, request: Server_pb2.Request, context: grpc.RpcContext) -> Server_pb2.Response:
        username = request.username
        print("USERNAMEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        if r.exists(username):
            return Server_pb2.Response(success=False)
    
        r.set(username, port)
        port = port + 1
        return Server_pb2.Response(success=True)

register_service = RegisterService()