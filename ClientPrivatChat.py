import redis
import Client_pb2

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

class PrivateChat:
    def connect_pc(self, User, port):
        print("hola")

private_chat = PrivateChat()