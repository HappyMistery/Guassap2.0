import pika, threading

class InsultChannel:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='insults', durable=True)
        self.channel.basic_consume(queue='insults', on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
        enviador_thread = threading.Thread(target=self.enviar_mensaje)
        enviador_thread.start()
    
    def callback(channel, method, properties, body):
        print(f"Received insult: {body.decode()}")
        
    def enviar_mensaje(self):
        while True:
            mensaje = input("Mensaje: ")
            self.channel.basic_publish(exchange='', routing_key='insults', body=mensaje)