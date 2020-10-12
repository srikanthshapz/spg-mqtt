# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Channels.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IsomStdDef_pb2 as IsomStdDef__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Channels.proto',
  package='Honeywell.Security.ISOM.Channels',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x43hannels.proto\x12 Honeywell.Security.ISOM.Channels\x1a\x10IsomStdDef.proto\"]\n\x11\x43hannelOperations\x12>\n\tresources\x18\x0b \x03(\x0e\x32+.Honeywell.Security.ISOM.Channels.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"e\n\x19\x43hannelSupportedRelations\x12>\n\trelations\x18\x0b \x03(\x0e\x32+.Honeywell.Security.ISOM.Channels.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"S\n\rChannelEvents\x12\x38\n\x06\x65vents\x18\x0b \x03(\x0e\x32(.Honeywell.Security.ISOM.Channels.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"j\n\x0f\x43hannelRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12\x39\n\x04name\x18\x0c \x01(\x0e\x32+.Honeywell.Security.ISOM.Channels.Relations\x12\x10\n\x08\x65ntityID\x18\r \x01(\t\"Z\n\x13\x43hannelRelationList\x12\x43\n\x08relation\x18\x0b \x03(\x0b\x32\x31.Honeywell.Security.ISOM.Channels.ChannelRelation\"C\n\x12\x43hannelIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\t\"\xa9\x01\n\rChannelConfig\x12I\n\x0bidentifiers\x18\x0b \x01(\x0b\x32\x34.Honeywell.Security.ISOM.Channels.ChannelIdentifiers\x12\x43\n\x08relation\x18\x0c \x03(\x0b\x32\x31.Honeywell.Security.ISOM.Channels.ChannelRelation*\x08\x08\xc0\x84=\x10\x87\x94=\"[\n\x11\x43hannelConfigList\x12\x46\n\rchannelConfig\x18\x0b \x03(\x0b\x32/.Honeywell.Security.ISOM.Channels.ChannelConfig\"Z\n\rChannelEntity\x12?\n\x06\x63onfig\x18\x15 \x01(\x0b\x32/.Honeywell.Security.ISOM.Channels.ChannelConfig*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"^\n\x11\x43hannelEntityList\x12?\n\x06\x65ntity\x18\x0b \x03(\x0b\x32/.Honeywell.Security.ISOM.Channels.ChannelEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xd2\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*z\n\tRelations\x12\x1c\n\x18\x43hannelConnectedToCamera\x10\x0b\x12\x1c\n\x18\x43hannelBelongsToRecorder\x10\x0c\x12\x1a\n\x16\x43hannelAssignedChannel\x10\r\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*[\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04*l\n\x0b\x43hannelType\x12\x08\n\x04Live\x10\x0b\x12\x11\n\rUserInitiated\x10\x0c\x12\x0e\n\nBackground\x10\r\x12\t\n\x05\x45vent\x10\x0e\x12\x0c\n\x08Schedule\x10\x0f\x12\x17\n\x0fMax_ChannelType\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.Channels.Resources',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='supportedOperations', index=0, number=1010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='supportedRelations', index=1, number=1011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='supportedEvents', index=2, number=1012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='supportedCapabilities', index=3, number=1013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='fullEntity', index=4, number=10050,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='info', index=5, number=10051,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config', index=6, number=10071,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='identifiers', index=7, number=10091,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='relations', index=8, number=10111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Resources', index=9, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1076,
  serialized_end=1286,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.Channels.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ChannelConnectedToCamera', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ChannelBelongsToRecorder', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ChannelAssignedChannel', index=2, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=3, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1288,
  serialized_end=1410,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.Channels.Events',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='config_p_add', index=0, number=10010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config_p_modify', index=1, number=10011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config_p_delete', index=2, number=10012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Events', index=3, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1412,
  serialized_end=1503,
)
_sym_db.RegisterEnumDescriptor(_EVENTS)

Events = enum_type_wrapper.EnumTypeWrapper(_EVENTS)
_CHANNELTYPE = _descriptor.EnumDescriptor(
  name='ChannelType',
  full_name='Honeywell.Security.ISOM.Channels.ChannelType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Live', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UserInitiated', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Background', index=2, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Event', index=3, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Schedule', index=4, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_ChannelType', index=5, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1505,
  serialized_end=1613,
)
_sym_db.RegisterEnumDescriptor(_CHANNELTYPE)

ChannelType = enum_type_wrapper.EnumTypeWrapper(_CHANNELTYPE)
supportedOperations = 1010
supportedRelations = 1011
supportedEvents = 1012
supportedCapabilities = 1013
fullEntity = 10050
info = 10051
config = 10071
identifiers = 10091
relations = 10111
Max_Resources = 1073741824
ChannelConnectedToCamera = 11
ChannelBelongsToRecorder = 12
ChannelAssignedChannel = 13
Max_Relations = 1073741824
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
Max_Events = 1073741824
Live = 11
UserInitiated = 12
Background = 13
Event = 14
Schedule = 15
Max_ChannelType = 1073741824



_CHANNELOPERATIONS = _descriptor.Descriptor(
  name='ChannelOperations',
  full_name='Honeywell.Security.ISOM.Channels.ChannelOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.Channels.ChannelOperations.resources', index=0,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=163,
)


_CHANNELSUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='ChannelSupportedRelations',
  full_name='Honeywell.Security.ISOM.Channels.ChannelSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.Channels.ChannelSupportedRelations.relations', index=0,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=165,
  serialized_end=266,
)


_CHANNELEVENTS = _descriptor.Descriptor(
  name='ChannelEvents',
  full_name='Honeywell.Security.ISOM.Channels.ChannelEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.Channels.ChannelEvents.events', index=0,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=268,
  serialized_end=351,
)


_CHANNELRELATION = _descriptor.Descriptor(
  name='ChannelRelation',
  full_name='Honeywell.Security.ISOM.Channels.ChannelRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.Channels.ChannelRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.Channels.ChannelRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityID', full_name='Honeywell.Security.ISOM.Channels.ChannelRelation.entityID', index=2,
      number=13, type=9, cpp_type=9, label=1,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=459,
)


_CHANNELRELATIONLIST = _descriptor.Descriptor(
  name='ChannelRelationList',
  full_name='Honeywell.Security.ISOM.Channels.ChannelRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.Channels.ChannelRelationList.relation', index=0,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=551,
)


_CHANNELIDENTIFIERS = _descriptor.Descriptor(
  name='ChannelIdentifiers',
  full_name='Honeywell.Security.ISOM.Channels.ChannelIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.Channels.ChannelIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.Channels.ChannelIdentifiers.name', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.Channels.ChannelIdentifiers.description', index=2,
      number=13, type=9, cpp_type=9, label=1,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=553,
  serialized_end=620,
)


_CHANNELCONFIG = _descriptor.Descriptor(
  name='ChannelConfig',
  full_name='Honeywell.Security.ISOM.Channels.ChannelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.Channels.ChannelConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.Channels.ChannelConfig.relation', index=1,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[(1000000, 1001991), ],
  oneofs=[
  ],
  serialized_start=623,
  serialized_end=792,
)


_CHANNELCONFIGLIST = _descriptor.Descriptor(
  name='ChannelConfigList',
  full_name='Honeywell.Security.ISOM.Channels.ChannelConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelConfig', full_name='Honeywell.Security.ISOM.Channels.ChannelConfigList.channelConfig', index=0,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=794,
  serialized_end=885,
)


_CHANNELENTITY = _descriptor.Descriptor(
  name='ChannelEntity',
  full_name='Honeywell.Security.ISOM.Channels.ChannelEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.Channels.ChannelEntity.config', index=0,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[(900000, 1100000), ],
  oneofs=[
  ],
  serialized_start=887,
  serialized_end=977,
)


_CHANNELENTITYLIST = _descriptor.Descriptor(
  name='ChannelEntityList',
  full_name='Honeywell.Security.ISOM.Channels.ChannelEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.Channels.ChannelEntityList.entity', index=0,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=979,
  serialized_end=1073,
)

_CHANNELOPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_CHANNELSUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_CHANNELEVENTS.fields_by_name['events'].enum_type = _EVENTS
_CHANNELRELATION.fields_by_name['name'].enum_type = _RELATIONS
_CHANNELRELATIONLIST.fields_by_name['relation'].message_type = _CHANNELRELATION
_CHANNELCONFIG.fields_by_name['identifiers'].message_type = _CHANNELIDENTIFIERS
_CHANNELCONFIG.fields_by_name['relation'].message_type = _CHANNELRELATION
_CHANNELCONFIGLIST.fields_by_name['channelConfig'].message_type = _CHANNELCONFIG
_CHANNELENTITY.fields_by_name['config'].message_type = _CHANNELCONFIG
_CHANNELENTITYLIST.fields_by_name['entity'].message_type = _CHANNELENTITY
DESCRIPTOR.message_types_by_name['ChannelOperations'] = _CHANNELOPERATIONS
DESCRIPTOR.message_types_by_name['ChannelSupportedRelations'] = _CHANNELSUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['ChannelEvents'] = _CHANNELEVENTS
DESCRIPTOR.message_types_by_name['ChannelRelation'] = _CHANNELRELATION
DESCRIPTOR.message_types_by_name['ChannelRelationList'] = _CHANNELRELATIONLIST
DESCRIPTOR.message_types_by_name['ChannelIdentifiers'] = _CHANNELIDENTIFIERS
DESCRIPTOR.message_types_by_name['ChannelConfig'] = _CHANNELCONFIG
DESCRIPTOR.message_types_by_name['ChannelConfigList'] = _CHANNELCONFIGLIST
DESCRIPTOR.message_types_by_name['ChannelEntity'] = _CHANNELENTITY
DESCRIPTOR.message_types_by_name['ChannelEntityList'] = _CHANNELENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
DESCRIPTOR.enum_types_by_name['ChannelType'] = _CHANNELTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelOperations = _reflection.GeneratedProtocolMessageType('ChannelOperations', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELOPERATIONS,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelOperations)
  })
_sym_db.RegisterMessage(ChannelOperations)

ChannelSupportedRelations = _reflection.GeneratedProtocolMessageType('ChannelSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSUPPORTEDRELATIONS,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelSupportedRelations)
  })
_sym_db.RegisterMessage(ChannelSupportedRelations)

ChannelEvents = _reflection.GeneratedProtocolMessageType('ChannelEvents', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELEVENTS,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelEvents)
  })
_sym_db.RegisterMessage(ChannelEvents)

ChannelRelation = _reflection.GeneratedProtocolMessageType('ChannelRelation', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELRELATION,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelRelation)
  })
_sym_db.RegisterMessage(ChannelRelation)

ChannelRelationList = _reflection.GeneratedProtocolMessageType('ChannelRelationList', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELRELATIONLIST,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelRelationList)
  })
_sym_db.RegisterMessage(ChannelRelationList)

ChannelIdentifiers = _reflection.GeneratedProtocolMessageType('ChannelIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELIDENTIFIERS,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelIdentifiers)
  })
_sym_db.RegisterMessage(ChannelIdentifiers)

ChannelConfig = _reflection.GeneratedProtocolMessageType('ChannelConfig', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIG,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelConfig)
  })
_sym_db.RegisterMessage(ChannelConfig)

ChannelConfigList = _reflection.GeneratedProtocolMessageType('ChannelConfigList', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCONFIGLIST,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelConfigList)
  })
_sym_db.RegisterMessage(ChannelConfigList)

ChannelEntity = _reflection.GeneratedProtocolMessageType('ChannelEntity', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELENTITY,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelEntity)
  })
_sym_db.RegisterMessage(ChannelEntity)

ChannelEntityList = _reflection.GeneratedProtocolMessageType('ChannelEntityList', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELENTITYLIST,
  '__module__' : 'Channels_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Channels.ChannelEntityList)
  })
_sym_db.RegisterMessage(ChannelEntityList)


# @@protoc_insertion_point(module_scope)
