# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Streams_e.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IsomStdDef_pb2 as IsomStdDef__pb2
import Streams_pb2 as Streams__pb2
import Clips_pb2 as Clips__pb2
import StreamProfile_pb2 as StreamProfile__pb2
import RecordProfile_pb2 as RecordProfile__pb2
import IsomEvents_pb2 as IsomEvents__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Streams_e.proto',
  package='Honeywell.Security.ISOM.Streams',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0fStreams_e.proto\x12\x1fHoneywell.Security.ISOM.Streams\x1a\x10IsomStdDef.proto\x1a\rStreams.proto\x1a\x0b\x43lips.proto\x1a\x13StreamProfile.proto\x1a\x13RecordProfile.proto\x1a\x10IsomEvents.proto\"\xcf\x03\n\x0eStreamConfig_e2\x81\x01\n\x17StreamRetrievedFromClip\x12-.Honeywell.Security.ISOM.Streams.StreamConfig\x18\xa1\xf7\x36 \x03(\x0b\x32).Honeywell.Security.ISOM.Clips.ClipConfigB\x04\xa0\xb5\x18\x01\x32\x9b\x01\n\x1fStreamRetrievedForStreamProfile\x12-.Honeywell.Security.ISOM.Streams.StreamConfig\x18\xa2\xf7\x36 \x03(\x0b\x32;.Honeywell.Security.ISOM.StreamProfiles.StreamProfileConfigB\x04\xa0\xb5\x18\x01\x32\x9a\x01\n\"StreamRetrievedDataFromEventStream\x12-.Honeywell.Security.ISOM.Streams.StreamConfig\x18\xa3\xf7\x36 \x03(\x0b\x32\x37.Honeywell.Security.ISOM.EventStreams.EventStreamConfigB\x04\xa0\xb5\x18\x01')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,Streams__pb2.DESCRIPTOR,Clips__pb2.DESCRIPTOR,StreamProfile__pb2.DESCRIPTOR,RecordProfile__pb2.DESCRIPTOR,IsomEvents__pb2.DESCRIPTOR,])




_STREAMCONFIG_E = _descriptor.Descriptor(
  name='StreamConfig_e',
  full_name='Honeywell.Security.ISOM.Streams.StreamConfig_e',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='StreamRetrievedFromClip', full_name='Honeywell.Security.ISOM.Streams.StreamConfig_e.StreamRetrievedFromClip', index=0,
      number=900001, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StreamRetrievedForStreamProfile', full_name='Honeywell.Security.ISOM.Streams.StreamConfig_e.StreamRetrievedForStreamProfile', index=1,
      number=900002, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=_b('\240\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StreamRetrievedDataFromEventStream', full_name='Honeywell.Security.ISOM.Streams.StreamConfig_e.StreamRetrievedDataFromEventStream', index=2,
      number=900003, type=11, cpp_type=10, label=3,
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
  serialized_start=159,
  serialized_end=622,
)

DESCRIPTOR.message_types_by_name['StreamConfig_e'] = _STREAMCONFIG_E
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamConfig_e = _reflection.GeneratedProtocolMessageType('StreamConfig_e', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCONFIG_E,
  '__module__' : 'Streams_e_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Streams.StreamConfig_e)
  })
_sym_db.RegisterMessage(StreamConfig_e)

_STREAMCONFIG_E.extensions_by_name['StreamRetrievedFromClip'].message_type = Clips__pb2._CLIPCONFIG
Streams__pb2.StreamConfig.RegisterExtension(_STREAMCONFIG_E.extensions_by_name['StreamRetrievedFromClip'])
_STREAMCONFIG_E.extensions_by_name['StreamRetrievedForStreamProfile'].message_type = StreamProfile__pb2._STREAMPROFILECONFIG
Streams__pb2.StreamConfig.RegisterExtension(_STREAMCONFIG_E.extensions_by_name['StreamRetrievedForStreamProfile'])
_STREAMCONFIG_E.extensions_by_name['StreamRetrievedDataFromEventStream'].message_type = IsomEvents__pb2._EVENTSTREAMCONFIG
Streams__pb2.StreamConfig.RegisterExtension(_STREAMCONFIG_E.extensions_by_name['StreamRetrievedDataFromEventStream'])

_STREAMCONFIG_E.extensions_by_name['StreamRetrievedFromClip']._options = None
_STREAMCONFIG_E.extensions_by_name['StreamRetrievedForStreamProfile']._options = None
_STREAMCONFIG_E.extensions_by_name['StreamRetrievedDataFromEventStream']._options = None
# @@protoc_insertion_point(module_scope)