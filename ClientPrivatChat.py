import Client_pb2


class PrivateChat:
    def __init__(self):
        self.msg = ""
        self.insults_severity = dict()
        
    def send_message(self, message):
        self.msg = message.content
        return 'Done'
    
    def recieve_message(self):
        messg = Client_pb2.Message(content=self.msg)
        return messg

private_chat = PrivateChat()