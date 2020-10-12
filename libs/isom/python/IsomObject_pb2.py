# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IsomObject.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IsomCommonHeaders_pb2 as IsomCommonHeaders__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IsomObject.proto',
  package='Honeywell.Security.ISOM',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10IsomObject.proto\x12\x17Honeywell.Security.ISOM\x1a\x17IsomCommonHeaders.proto\"C\n\x13\x41uthorizationHeader\x12\x10\n\x08userName\x18\x0b \x01(\t\x12\x10\n\x08password\x18\x0c \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xac\x01\n\x0c\x44omainObject\x12\x12\n\nobjectType\x18\x0b \x01(\x04\x12)\n\x03uri\x18\x0c \x01(\x0b\x32\x1c.Honeywell.Security.ISOM.URI\x12@\n\nauthHeader\x18\r \x01(\x0b\x32,.Honeywell.Security.ISOM.AuthorizationHeader\x12\x11\n\tsessionId\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xce\x01\n\x11IsomRequestObject\x12\x15\n\rtransactionId\x18\x0b \x01(\x04\x12\x38\n\tdomainObj\x18\x0c \x01(\x0b\x32%.Honeywell.Security.ISOM.DomainObject\x12I\n\x13payloadTransferMode\x18\r \x01(\x0e\x32,.Honeywell.Security.ISOM.PayloadTransferMode\x12\x13\n\x0bpayloadSize\x18\x0e \x01(\x04*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xab\x01\n\x12IsomResponseObject\x12\x15\n\rtransactionId\x18\x0b \x01(\x04\x12\x14\n\x0cresponseCode\x18\x0c \x01(\x04\x12I\n\x13payloadTransferMode\x18\r \x01(\x0e\x32,.Honeywell.Security.ISOM.PayloadTransferMode\x12\x13\n\x0bpayloadSize\x18\x0e \x01(\x04*\x08\x08\xc0\x84=\x10\xe0\x91\x43*B\n\x13PayloadTransferMode\x12\x0e\n\nBy_PayLoad\x10\x0b\x12\x0b\n\x07\x42y_File\x10\x0c\x12\x0e\n\nBy_Chunked\x10\r')
  ,
  dependencies=[IsomCommonHeaders__pb2.DESCRIPTOR,])

_PAYLOADTRANSFERMODE = _descriptor.EnumDescriptor(
  name='PayloadTransferMode',
  full_name='Honeywell.Security.ISOM.PayloadTransferMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='By_PayLoad', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='By_File', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='By_Chunked', index=2, number=13,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=697,
  serialized_end=763,
)
_sym_db.RegisterEnumDescriptor(_PAYLOADTRANSFERMODE)

PayloadTransferMode = enum_type_wrapper.EnumTypeWrapper(_PAYLOADTRANSFERMODE)
By_PayLoad = 11
By_File = 12
By_Chunked = 13



_AUTHORIZATIONHEADER = _descriptor.Descriptor(
  name='AuthorizationHeader',
  full_name='Honeywell.Security.ISOM.AuthorizationHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='Honeywell.Security.ISOM.AuthorizationHeader.userName', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='Honeywell.Security.ISOM.AuthorizationHeader.password', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=137,
)


_DOMAINOBJECT = _descriptor.Descriptor(
  name='DomainObject',
  full_name='Honeywell.Security.ISOM.DomainObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectType', full_name='Honeywell.Security.ISOM.DomainObject.objectType', index=0,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uri', full_name='Honeywell.Security.ISOM.DomainObject.uri', index=1,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authHeader', full_name='Honeywell.Security.ISOM.DomainObject.authHeader', index=2,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='Honeywell.Security.ISOM.DomainObject.sessionId', index=3,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=312,
)


_ISOMREQUESTOBJECT = _descriptor.Descriptor(
  name='IsomRequestObject',
  full_name='Honeywell.Security.ISOM.IsomRequestObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactionId', full_name='Honeywell.Security.ISOM.IsomRequestObject.transactionId', index=0,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domainObj', full_name='Honeywell.Security.ISOM.IsomRequestObject.domainObj', index=1,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payloadTransferMode', full_name='Honeywell.Security.ISOM.IsomRequestObject.payloadTransferMode', index=2,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payloadSize', full_name='Honeywell.Security.ISOM.IsomRequestObject.payloadSize', index=3,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=521,
)


_ISOMRESPONSEOBJECT = _descriptor.Descriptor(
  name='IsomResponseObject',
  full_name='Honeywell.Security.ISOM.IsomResponseObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactionId', full_name='Honeywell.Security.ISOM.IsomResponseObject.transactionId', index=0,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responseCode', full_name='Honeywell.Security.ISOM.IsomResponseObject.responseCode', index=1,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payloadTransferMode', full_name='Honeywell.Security.ISOM.IsomResponseObject.payloadTransferMode', index=2,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payloadSize', full_name='Honeywell.Security.ISOM.IsomResponseObject.payloadSize', index=3,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=695,
)

_DOMAINOBJECT.fields_by_name['uri'].message_type = IsomCommonHeaders__pb2._URI
_DOMAINOBJECT.fields_by_name['authHeader'].message_type = _AUTHORIZATIONHEADER
_ISOMREQUESTOBJECT.fields_by_name['domainObj'].message_type = _DOMAINOBJECT
_ISOMREQUESTOBJECT.fields_by_name['payloadTransferMode'].enum_type = _PAYLOADTRANSFERMODE
_ISOMRESPONSEOBJECT.fields_by_name['payloadTransferMode'].enum_type = _PAYLOADTRANSFERMODE
DESCRIPTOR.message_types_by_name['AuthorizationHeader'] = _AUTHORIZATIONHEADER
DESCRIPTOR.message_types_by_name['DomainObject'] = _DOMAINOBJECT
DESCRIPTOR.message_types_by_name['IsomRequestObject'] = _ISOMREQUESTOBJECT
DESCRIPTOR.message_types_by_name['IsomResponseObject'] = _ISOMRESPONSEOBJECT
DESCRIPTOR.enum_types_by_name['PayloadTransferMode'] = _PAYLOADTRANSFERMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthorizationHeader = _reflection.GeneratedProtocolMessageType('AuthorizationHeader', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONHEADER,
  '__module__' : 'IsomObject_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.AuthorizationHeader)
  })
_sym_db.RegisterMessage(AuthorizationHeader)

DomainObject = _reflection.GeneratedProtocolMessageType('DomainObject', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINOBJECT,
  '__module__' : 'IsomObject_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DomainObject)
  })
_sym_db.RegisterMessage(DomainObject)

IsomRequestObject = _reflection.GeneratedProtocolMessageType('IsomRequestObject', (_message.Message,), {
  'DESCRIPTOR' : _ISOMREQUESTOBJECT,
  '__module__' : 'IsomObject_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.IsomRequestObject)
  })
_sym_db.RegisterMessage(IsomRequestObject)

IsomResponseObject = _reflection.GeneratedProtocolMessageType('IsomResponseObject', (_message.Message,), {
  'DESCRIPTOR' : _ISOMRESPONSEOBJECT,
  '__module__' : 'IsomObject_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.IsomResponseObject)
  })
_sym_db.RegisterMessage(IsomResponseObject)


# @@protoc_insertion_point(module_scope)