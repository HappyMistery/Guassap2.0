# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import NameServer_pb2 as NameServer__pb2


class NameServerStub(object):
    """Service for managing chat namespace and addresses
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterAddress = channel.unary_unary(
                '/NameServer/RegisterAddress',
                request_serializer=NameServer__pb2.UserAddress.SerializeToString,
                response_deserializer=NameServer__pb2.Empty.FromString,
                )
        self.GetChatAddress = channel.unary_unary(
                '/NameServer/GetChatAddress',
                request_serializer=NameServer__pb2.ChatId.SerializeToString,
                response_deserializer=NameServer__pb2.ChatAddress.FromString,
                )


class NameServerServicer(object):
    """Service for managing chat namespace and addresses
    """

    def RegisterAddress(self, request, context):
        """Registers the IP address and port associated with a username
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChatAddress(self, request, context):
        """Retrieves the address associated with a chat ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterAddress,
                    request_deserializer=NameServer__pb2.UserAddress.FromString,
                    response_serializer=NameServer__pb2.Empty.SerializeToString,
            ),
            'GetChatAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChatAddress,
                    request_deserializer=NameServer__pb2.ChatId.FromString,
                    response_serializer=NameServer__pb2.ChatAddress.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameServer(object):
    """Service for managing chat namespace and addresses
    """

    @staticmethod
    def RegisterAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameServer/RegisterAddress',
            NameServer__pb2.UserAddress.SerializeToString,
            NameServer__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChatAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameServer/GetChatAddress',
            NameServer__pb2.ChatId.SerializeToString,
            NameServer__pb2.ChatAddress.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)