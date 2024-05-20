import subprocess
import threading

def main():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.DEVNULL)
        print("Successfully installed requirements from requirements.txt")
    except subprocess.CalledProcessError as e:
        print("Requirements already installed")
       
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./Client.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './Client.proto'], stdout=subprocess.DEVNULL)
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./MessageBroker.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './MessageBroker.proto'], stdout=subprocess.DEVNULL)
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./NameServer.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './NameServer.proto'], stdout=subprocess.DEVNULL)
    
    try:
        subprocess.check_call(['wsl', 'redis-server'], stdout=subprocess.DEVNULL)
    except Exception as e:
        print("redis server already started")
        
    try:
        subprocess.check_call(['wsl', 'docker', 'pull', 'rabbitmq'], stdout=subprocess.DEVNULL)
    except Exception as e:
        print("rabbitmq already added")
        
    try:
        subprocess.check_call(['wsl', 'docker', 'run', '-d', '--name', 'rabbitmq', '-p', '5672:5672', '-p', '15672:15672', 'rabbitmq'], stdout=subprocess.DEVNULL)
    except Exception as e:
        print("rabbitmq already started")
        
    import Server
    
    server_thread = threading.Thread(target=Server.start)
    client1_thread = threading.Thread(target=run_client)
    client2_thread = threading.Thread(target=run_client)
    client3_thread = threading.Thread(target=run_client)
    
    server_thread.start()
    client1_thread.start()
    client2_thread.start()
    client3_thread.start()

    server_thread.join()
    client1_thread.join()
    client2_thread.join()
    client3_thread.join()
    
def run_client():
    subprocess.run(['py', 'Client.py'], shell=True)
    
main()
    
