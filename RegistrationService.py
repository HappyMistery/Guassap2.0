import redis
import NameServer_pb2

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

user_port = 50052

class RegisterService:
    def register_user(self, request):
        r.ping()
        ip_port = str(request.ip_address)+":"+str(user_port)
        print(request.username)
        print(ip_port)
        if r.exists(request.username):
            return NameServer_pb2.Response(success=False)
    
        r.set(request.username, ip_port)
        user_port = user_port + 1
        return NameServer_pb2.Response(success=True)

registration_service = RegisterService()