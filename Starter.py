import threading
import Client, Server

def main():
    client_thread = threading.Thread(target=Client.start)
    server_thread = threading.Thread(target=Server.start)
    
    client_thread.start()
    server_thread.start()

    client_thread.join()
    server_thread.join()
main()
    
