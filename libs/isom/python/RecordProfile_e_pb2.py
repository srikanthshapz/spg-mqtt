# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RecordProfile_e.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IsomStdDef_pb2 as IsomStdDef__pb2
import RecordProfile_pb2 as RecordProfile__pb2
import Volumes_pb2 as Volumes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RecordProfile_e.proto',
  package='Honeywell.Security.ISOM.RecordProfiles',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x15RecordProfile_e.proto\x12&Honeywell.Security.ISOM.RecordProfiles\x1a\x10IsomStdDef.proto\x1a\x13RecordProfile.proto\x1a\rVolumes.proto\"\xb7\x01\n\x15RecordProfileConfig_e2\x9d\x01\n!RecordProfileAssociatedWithVolume\x12;.Honeywell.Security.ISOM.RecordProfiles.RecordProfileConfig\x18\xa1\xf7\x36 \x03(\x0b\x32-.Honeywell.Security.ISOM.Volumes.VolumeConfigB\x04\xa0\xb5\x18\x01')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,RecordProfile__pb2.DESCRIPTOR,Volumes__pb2.DESCRIPTOR,])




_RECORDPROFILECONFIG_E = _descriptor.Descriptor(
  name='RecordProfileConfig_e',
  full_name='Honeywell.Security.ISOM.RecordProfiles.RecordProfileConfig_e',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='RecordProfileAssociatedWithVolume', full_name='Honeywell.Security.ISOM.RecordProfiles.RecordProfileConfig_e.RecordProfileAssociatedWithVolume', index=0,
      number=900001, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=303,
)

DESCRIPTOR.message_types_by_name['RecordProfileConfig_e'] = _RECORDPROFILECONFIG_E
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecordProfileConfig_e = _reflection.GeneratedProtocolMessageType('RecordProfileConfig_e', (_message.Message,), {
  'DESCRIPTOR' : _RECORDPROFILECONFIG_E,
  '__module__' : 'RecordProfile_e_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.RecordProfiles.RecordProfileConfig_e)
  })
_sym_db.RegisterMessage(RecordProfileConfig_e)

_RECORDPROFILECONFIG_E.extensions_by_name['RecordProfileAssociatedWithVolume'].message_type = Volumes__pb2._VOLUMECONFIG
RecordProfile__pb2.RecordProfileConfig.RegisterExtension(_RECORDPROFILECONFIG_E.extensions_by_name['RecordProfileAssociatedWithVolume'])

_RECORDPROFILECONFIG_E.extensions_by_name['RecordProfileAssociatedWithVolume']._options = None
# @@protoc_insertion_point(module_scope)
