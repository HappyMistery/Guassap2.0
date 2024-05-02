import subprocess
import Client

def main():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("Successfully installed requirements from requirements.txt")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
       
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./Client.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './Client.proto'])
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./MessageBroker.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './MessageBroker.proto'])
    #python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. --pyi_out=. ./NameServer.proto
    subprocess.check_call(['python3', '-m', 'grpc_tools.protoc', '-I./', '--python_out=.', '--grpc_python_out=.', '--pyi_out=.', './NameServer.proto'])
    Client.start()
main()
    
