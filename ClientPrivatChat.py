import redis
import Client_pb2

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

class PrivateChat:
    def send_message(self, message):
        print(message.content)
        return Client_pb2.Empty()

private_chat = PrivateChat()