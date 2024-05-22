import time
import grpc
from concurrent import futures

import NameServer_pb2_grpc
import NameServer_pb2
from RedisService import registration_service

def start():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        NameServer_pb2_grpc.add_NameServerServicer_to_server(NameServerServicer(), server)
        server.add_insecure_port('localhost:50051')
        server.start()
    except Exception as e:
        print("NameServer already started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
    
class NameServerServicer(NameServer_pb2_grpc.NameServerServicer):
    def RegisterUser(self, request, context):
        registration = registration_service.register_user(request)
        response = NameServer_pb2.Response()
        response.success = registration.success
        return response
    
    def GetUserInfo(self, request, context):
        u_info = registration_service.get_user_info(request)
        response = NameServer_pb2.ChatAddress()
        if(u_info is None):
            response.address = 'None'
        else:
            response.address = u_info
        return response
    
    def UpdateGroupsList(self, request, context):
        registration_service.update_groups_list(request)
        response = NameServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response
    
    def GetGroupsList(self, request, context):
        group_chats_list = NameServer_pb2.UserAddress(username='group_chats')
        groups = registration_service.get_user_info(group_chats_list)
        response = NameServer_pb2.ChatAddress(address=groups)
        return response