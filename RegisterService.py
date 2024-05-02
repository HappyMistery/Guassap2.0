import redis
import Server_pb2

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

port = 50052

class RegisterService:
    def register_user(self, request: Server_pb2.RegisterRequest, context) -> Server_pb2.RegisterResponse:
        username = request.username
        if r.exists(username):
            return Server_pb2.RegisterResponse(success=False)
    
        r.set(username, port)
        port = port + 1
        return Server_pb2.RegisterResponse(success=True)

register_service = RegisterService()