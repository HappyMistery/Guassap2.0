# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Client_pb2 as Client__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ChatServiceStub(object):
    """Service for managing chat connections and messages
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConnectGChat = channel.unary_stream(
                '/ChatService/ConnectGChat',
                request_serializer=Client__pb2.ChatId.SerializeToString,
                response_deserializer=Client__pb2.Message.FromString,
                )
        self.SubscribeToGroupChat = channel.unary_stream(
                '/ChatService/SubscribeToGroupChat',
                request_serializer=Client__pb2.ChatId.SerializeToString,
                response_deserializer=Client__pb2.Message.FromString,
                )
        self.DiscoverChats = channel.unary_stream(
                '/ChatService/DiscoverChats',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=Client__pb2.ChatId.FromString,
                )
        self.SendInsult = channel.unary_unary(
                '/ChatService/SendInsult',
                request_serializer=Client__pb2.User.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SendPrivateMessage = channel.unary_unary(
                '/ChatService/SendPrivateMessage',
                request_serializer=Client__pb2.Message.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.RecievePrivateMessage = channel.unary_unary(
                '/ChatService/RecievePrivateMessage',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ChatServiceServicer(object):
    """Service for managing chat connections and messages
    """

    def ConnectGChat(self, request, context):
        """Connects to an existing chat (group)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeToGroupChat(self, request, context):
        """Starts listening to messages in a group chat
        Creates the chat if it doesn't exist
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DiscoverChats(self, request, context):
        """Requests a list of active chats
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendInsult(self, request, context):
        """Sends an insult message to another client (undefined behavior)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendPrivateMessage(self, request, context):
        """Sends a message to a user
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RecievePrivateMessage(self, request, context):
        """Recieves a private message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ConnectGChat': grpc.unary_stream_rpc_method_handler(
                    servicer.ConnectGChat,
                    request_deserializer=Client__pb2.ChatId.FromString,
                    response_serializer=Client__pb2.Message.SerializeToString,
            ),
            'SubscribeToGroupChat': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeToGroupChat,
                    request_deserializer=Client__pb2.ChatId.FromString,
                    response_serializer=Client__pb2.Message.SerializeToString,
            ),
            'DiscoverChats': grpc.unary_stream_rpc_method_handler(
                    servicer.DiscoverChats,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=Client__pb2.ChatId.SerializeToString,
            ),
            'SendInsult': grpc.unary_unary_rpc_method_handler(
                    servicer.SendInsult,
                    request_deserializer=Client__pb2.User.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SendPrivateMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPrivateMessage,
                    request_deserializer=Client__pb2.Message.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'RecievePrivateMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.RecievePrivateMessage,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatService(object):
    """Service for managing chat connections and messages
    """

    @staticmethod
    def ConnectGChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ChatService/ConnectGChat',
            Client__pb2.ChatId.SerializeToString,
            Client__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeToGroupChat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ChatService/SubscribeToGroupChat',
            Client__pb2.ChatId.SerializeToString,
            Client__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DiscoverChats(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ChatService/DiscoverChats',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            Client__pb2.ChatId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendInsult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ChatService/SendInsult',
            Client__pb2.User.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendPrivateMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ChatService/SendPrivateMessage',
            Client__pb2.Message.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RecievePrivateMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ChatService/RecievePrivateMessage',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
