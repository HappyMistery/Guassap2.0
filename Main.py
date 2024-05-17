import subprocess
import threading

def main():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("Successfully installed requirements from requirements.txt")
    except subprocess.CalledProcessError as e:
        print("Requirements already installed")
       
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./Client.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './Client.proto'])
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./MessageBroker.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './MessageBroker.proto'])
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./NameServer.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './NameServer.proto'])
    
    try:
        subprocess.check_call(['wsl', 'redis-server'])
    except Exception as e:
        print("redis server already started")
        
    try:
        subprocess.check_call(['wsl', 'docker', 'pull', 'rabbitmq'])
    except Exception as e:
        print("rabbitmq already added")
        
    try:
        subprocess.check_call(['wsl', 'docker', 'run', '-d', '--name', 'rabbitmq', '-p', '5672:5672', '-p', '15672:15672', 'rabbitmq'])
    except Exception as e:
        print("rabbitmq already started")
        
    import Client, Server
    
    client_thread = threading.Thread(target=Client.start)
    server_thread = threading.Thread(target=Server.start)
    
    client_thread.start()
    server_thread.start()

    client_thread.join()
    server_thread.join()
main()
    
