# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Server_pb2 as Server__pb2


class RegisterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register_user = channel.unary_unary(
                '/user.RegisterService/register_user',
                request_serializer=Server__pb2.RegisterRequest.SerializeToString,
                response_deserializer=Server__pb2.RegisterResponse.FromString,
                )


class RegisterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegisterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register_user': grpc.unary_unary_rpc_method_handler(
                    servicer.register_user,
                    request_deserializer=Server__pb2.RegisterRequest.FromString,
                    response_serializer=Server__pb2.RegisterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.RegisterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RegisterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register_user(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.RegisterService/register_user',
            Server__pb2.RegisterRequest.SerializeToString,
            Server__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
