import redis
import NameServer_pb2

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

if not r.exists('user_port'):
    r.set('user_port', 50052)
if not r.exists('group_chats'):
    r.set('group_chats', '')


class RedisService:
    def register_user(self, request):
        ip_port = f"{request.ip_address}:{r.get('user_port')}"
        if r.exists(request.username):
            return NameServer_pb2.Response(success=False)
    
        r.set(request.username, ip_port)
        r.set('user_port', int(r.get('user_port'))+1)
        return NameServer_pb2.Response(success=True)
    
    def get_user_info(self, request):
        return r.get(request.username)
    
    def update_groups_list(self, request):
        r.set('group_chats', f"{r.get('group_chats')}{request.address},")
        

registration_service = RedisService()