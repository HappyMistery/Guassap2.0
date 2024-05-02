from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChatId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class UserAddress(_message.Message):
    __slots__ = ("useraddr",)
    USERADDR_FIELD_NUMBER: _ClassVar[int]
    useraddr: str
    def __init__(self, useraddr: _Optional[str] = ...) -> None: ...

class ChatMessage(_message.Message):
    __slots__ = ("content", "sender_username", "timestamp")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SENDER_USERNAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    content: str
    sender_username: str
    timestamp: int
    def __init__(self, content: _Optional[str] = ..., sender_username: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...
