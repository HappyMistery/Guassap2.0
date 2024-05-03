import time
import grpc
from concurrent import futures

import NameServer_pb2_grpc
import NameServer_pb2
from RegistrationService import registration_service

def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    NameServer_pb2_grpc.add_NameServerServicer_to_server(NameServerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("The Name Server is waiting for registrations")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
    
class NameServerServicer(NameServer_pb2_grpc.NameServerServicer):
    def RegisterUser(self, request, context):
        registration = registration_service.register_user(request)
        response = NameServer_pb2.Response()
        response.value.extend(registration)
        return response