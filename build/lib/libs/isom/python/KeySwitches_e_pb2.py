# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KeySwitches_e.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IsomStdDef_pb2 as IsomStdDef__pb2
import KeySwitches_pb2 as KeySwitches__pb2
import DetectorGroups_pb2 as DetectorGroups__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='KeySwitches_e.proto',
  package='Honeywell.Security.ISOM.KeySwitches',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13KeySwitches_e.proto\x12#Honeywell.Security.ISOM.KeySwitches\x1a\x10IsomStdDef.proto\x1a\x11KeySwitches.proto\x1a\x14\x44\x65tectorGroups.proto\"\xb6\x01\n\x11KeySwitchConfig_e2\xa0\x01\n\x1d\x44\x65viceAssignedToDetectorGroup\x12\x34.Honeywell.Security.ISOM.KeySwitches.KeySwitchConfig\x18\xa1\xf7\x36 \x03(\x0b\x32;.Honeywell.Security.ISOM.DetectorGroups.DetectorGroupConfigB\x04\xa0\xb5\x18\x01\"\xb6\x01\n\x11KeySwitchEntity_e2\xa0\x01\n\x1d\x44\x65viceAssignedToDetectorGroup\x12\x34.Honeywell.Security.ISOM.KeySwitches.KeySwitchEntity\x18\xa1\xf7\x36 \x03(\x0b\x32;.Honeywell.Security.ISOM.DetectorGroups.DetectorGroupEntityB\x04\xa0\xb5\x18\x01')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,KeySwitches__pb2.DESCRIPTOR,DetectorGroups__pb2.DESCRIPTOR,])




_KEYSWITCHCONFIG_E = _descriptor.Descriptor(
  name='KeySwitchConfig_e',
  full_name='Honeywell.Security.ISOM.KeySwitches.KeySwitchConfig_e',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='DeviceAssignedToDetectorGroup', full_name='Honeywell.Security.ISOM.KeySwitches.KeySwitchConfig_e.DeviceAssignedToDetectorGroup', index=0,
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
  serialized_end=302,
)


_KEYSWITCHENTITY_E = _descriptor.Descriptor(
  name='KeySwitchEntity_e',
  full_name='Honeywell.Security.ISOM.KeySwitches.KeySwitchEntity_e',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='DeviceAssignedToDetectorGroup', full_name='Honeywell.Security.ISOM.KeySwitches.KeySwitchEntity_e.DeviceAssignedToDetectorGroup', index=0,
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
  serialized_start=305,
  serialized_end=487,
)

DESCRIPTOR.message_types_by_name['KeySwitchConfig_e'] = _KEYSWITCHCONFIG_E
DESCRIPTOR.message_types_by_name['KeySwitchEntity_e'] = _KEYSWITCHENTITY_E
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeySwitchConfig_e = _reflection.GeneratedProtocolMessageType('KeySwitchConfig_e', (_message.Message,), {
  'DESCRIPTOR' : _KEYSWITCHCONFIG_E,
  '__module__' : 'KeySwitches_e_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.KeySwitches.KeySwitchConfig_e)
  })
_sym_db.RegisterMessage(KeySwitchConfig_e)

KeySwitchEntity_e = _reflection.GeneratedProtocolMessageType('KeySwitchEntity_e', (_message.Message,), {
  'DESCRIPTOR' : _KEYSWITCHENTITY_E,
  '__module__' : 'KeySwitches_e_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.KeySwitches.KeySwitchEntity_e)
  })
_sym_db.RegisterMessage(KeySwitchEntity_e)

_KEYSWITCHCONFIG_E.extensions_by_name['DeviceAssignedToDetectorGroup'].message_type = DetectorGroups__pb2._DETECTORGROUPCONFIG
KeySwitches__pb2.KeySwitchConfig.RegisterExtension(_KEYSWITCHCONFIG_E.extensions_by_name['DeviceAssignedToDetectorGroup'])
_KEYSWITCHENTITY_E.extensions_by_name['DeviceAssignedToDetectorGroup'].message_type = DetectorGroups__pb2._DETECTORGROUPENTITY
KeySwitches__pb2.KeySwitchEntity.RegisterExtension(_KEYSWITCHENTITY_E.extensions_by_name['DeviceAssignedToDetectorGroup'])

_KEYSWITCHCONFIG_E.extensions_by_name['DeviceAssignedToDetectorGroup']._options = None
_KEYSWITCHENTITY_E.extensions_by_name['DeviceAssignedToDetectorGroup']._options = None
# @@protoc_insertion_point(module_scope)
