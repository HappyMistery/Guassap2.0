import threading
import NameServer
import MessageBroker

def start():
    ns_thread = threading.Thread(target=NameServer.start)
    mb_thread = threading.Thread(target=MessageBroker.start)
    
    ns_thread.start()
    mb_thread.start()

    ns_thread.join()
    mb_thread.join()