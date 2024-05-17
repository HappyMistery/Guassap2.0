from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatIdentifier(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("content", "sender_username", "group_chat")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SENDER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_CHAT_FIELD_NUMBER: _ClassVar[int]
    content: str
    sender_username: str
    group_chat: str
    def __init__(self, content: _Optional[str] = ..., sender_username: _Optional[str] = ..., group_chat: _Optional[str] = ...) -> None: ...
