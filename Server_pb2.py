# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Server.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cServer.proto\x12\x04user\"#\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"4\n\x10RegisterResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2S\n\x0fRegisterService\x12@\n\rregister_user\x12\x15.user.RegisterRequest\x1a\x16.user.RegisterResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Server_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REGISTERREQUEST']._serialized_start=22
  _globals['_REGISTERREQUEST']._serialized_end=57
  _globals['_REGISTERRESPONSE']._serialized_start=59
  _globals['_REGISTERRESPONSE']._serialized_end=111
  _globals['_REGISTERSERVICE']._serialized_start=113
  _globals['_REGISTERSERVICE']._serialized_end=196
# @@protoc_insertion_point(module_scope)
