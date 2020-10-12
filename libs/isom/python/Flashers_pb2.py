# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Flashers.proto

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
import IsomDevices_pb2 as IsomDevices__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Flashers.proto',
  package='Honeywell.Security.ISOM.Flashers',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x46lashers.proto\x12 Honeywell.Security.ISOM.Flashers\x1a\x10IsomStdDef.proto\x1a\x11IsomDevices.proto\"]\n\x11\x46lasherOperations\x12>\n\tresources\x18\x0b \x03(\x0e\x32+.Honeywell.Security.ISOM.Flashers.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"e\n\x19\x46lasherSupportedRelations\x12>\n\trelations\x18\x0b \x03(\x0e\x32+.Honeywell.Security.ISOM.Flashers.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"S\n\rFlasherEvents\x12\x38\n\x06\x65vents\x18\x0b \x03(\x0e\x32(.Honeywell.Security.ISOM.Flashers.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"[\n\x12\x46lasherIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"m\n\x16\x46lasherIdentifiersList\x12I\n\x0bidentifiers\x18\x0b \x03(\x0b\x32\x34.Honeywell.Security.ISOM.Flashers.FlasherIdentifiers*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"t\n\x0f\x46lasherRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12\x39\n\x04name\x18\x0c \x01(\x0e\x32+.Honeywell.Security.ISOM.Flashers.Relations\x12\x10\n\x08\x65ntityId\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"d\n\x13\x46lasherRelationList\x12\x43\n\x08relation\x18\x0b \x03(\x0b\x32\x31.Honeywell.Security.ISOM.Flashers.FlasherRelation*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xe8\x01\n\rFlasherConfig\x12I\n\x0bidentifiers\x18\x0b \x01(\x0b\x32\x34.Honeywell.Security.ISOM.Flashers.FlasherIdentifiers\x12\x43\n\x08relation\x18\n \x03(\x0b\x32\x31.Honeywell.Security.ISOM.Flashers.FlasherRelation\x12=\n\x04omit\x18\x14 \x01(\x0e\x32/.Honeywell.Security.ISOM.Devices.DeviceOmitType*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"^\n\x11\x46lasherConfigList\x12?\n\x06\x63onfig\x18\x0b \x03(\x0b\x32/.Honeywell.Security.ISOM.Flashers.FlasherConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x8d\x01\n\rFlasherEntity\x12?\n\x06\x63onfig\x18\x0b \x01(\x0b\x32/.Honeywell.Security.ISOM.Flashers.FlasherConfig\x12;\n\x05state\x18\x0c \x01(\x0b\x32,.Honeywell.Security.ISOM.Devices.DeviceState*\xb2\x03\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x11\n\x0creleaseState\x10\x92O\x12\x1a\n\x15releaseState_s_normal\x10\x93O\x12\x1b\n\x16releaseState_s_release\x10\x94O\x12\x0e\n\tomitState\x10\x9cO\x12\x17\n\x12omitState_s_unOmit\x10\x9dO\x12\x15\n\x10omitState_s_omit\x10\x9eO\x12\x10\n\x0b\x62ypassState\x10\xa6O\x12\x19\n\x14\x62ypassState_s_normal\x10\xa7O\x12\x19\n\x14\x62ypassState_s_bypass\x10\xa8O\x12\n\n\x05state\x10\xb0O\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*\"\n\tRelations\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*\x94\x01\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x1a\n\x15releaseState_p_normal\x10\xc8\x65\x12\x1b\n\x16releaseState_p_release\x10\xc9\x65\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,IsomDevices__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.Flashers.Resources',
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
      name='releaseState', index=9, number=10130,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='releaseState_s_normal', index=10, number=10131,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='releaseState_s_release', index=11, number=10132,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='omitState', index=12, number=10140,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='omitState_s_unOmit', index=13, number=10141,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='omitState_s_omit', index=14, number=10142,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='bypassState', index=15, number=10150,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='bypassState_s_normal', index=16, number=10151,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='bypassState_s_bypass', index=17, number=10152,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='state', index=18, number=10160,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Resources', index=19, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1272,
  serialized_end=1706,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.Flashers.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=0, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1708,
  serialized_end=1742,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.Flashers.Events',
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
      name='releaseState_p_normal', index=3, number=13000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='releaseState_p_release', index=4, number=13001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Events', index=5, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1745,
  serialized_end=1893,
)
_sym_db.RegisterEnumDescriptor(_EVENTS)

Events = enum_type_wrapper.EnumTypeWrapper(_EVENTS)
supportedOperations = 1010
supportedRelations = 1011
supportedEvents = 1012
supportedCapabilities = 1013
fullEntity = 10050
info = 10051
config = 10071
identifiers = 10091
relations = 10111
releaseState = 10130
releaseState_s_normal = 10131
releaseState_s_release = 10132
omitState = 10140
omitState_s_unOmit = 10141
omitState_s_omit = 10142
bypassState = 10150
bypassState_s_normal = 10151
bypassState_s_bypass = 10152
state = 10160
Max_Resources = 1073741824
Max_Relations = 1073741824
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
releaseState_p_normal = 13000
releaseState_p_release = 13001
Max_Events = 1073741824



_FLASHEROPERATIONS = _descriptor.Descriptor(
  name='FlasherOperations',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.Flashers.FlasherOperations.resources', index=0,
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
  serialized_start=89,
  serialized_end=182,
)


_FLASHERSUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='FlasherSupportedRelations',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.Flashers.FlasherSupportedRelations.relations', index=0,
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
  serialized_start=184,
  serialized_end=285,
)


_FLASHEREVENTS = _descriptor.Descriptor(
  name='FlasherEvents',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.Flashers.FlasherEvents.events', index=0,
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
  serialized_start=287,
  serialized_end=370,
)


_FLASHERIDENTIFIERS = _descriptor.Descriptor(
  name='FlasherIdentifiers',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiers.name', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiers.description', index=3,
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
  serialized_start=372,
  serialized_end=463,
)


_FLASHERIDENTIFIERSLIST = _descriptor.Descriptor(
  name='FlasherIdentifiersList',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.Flashers.FlasherIdentifiersList.identifiers', index=0,
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
  serialized_start=465,
  serialized_end=574,
)


_FLASHERRELATION = _descriptor.Descriptor(
  name='FlasherRelation',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.Flashers.FlasherRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.Flashers.FlasherRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1073741824,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.Flashers.FlasherRelation.entityId', index=2,
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
  serialized_start=576,
  serialized_end=692,
)


_FLASHERRELATIONLIST = _descriptor.Descriptor(
  name='FlasherRelationList',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.Flashers.FlasherRelationList.relation', index=0,
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
  serialized_start=694,
  serialized_end=794,
)


_FLASHERCONFIG = _descriptor.Descriptor(
  name='FlasherConfig',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.Flashers.FlasherConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.Flashers.FlasherConfig.relation', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omit', full_name='Honeywell.Security.ISOM.Flashers.FlasherConfig.omit', index=2,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
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
  serialized_start=797,
  serialized_end=1029,
)


_FLASHERCONFIGLIST = _descriptor.Descriptor(
  name='FlasherConfigList',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.Flashers.FlasherConfigList.config', index=0,
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
  serialized_start=1031,
  serialized_end=1125,
)


_FLASHERENTITY = _descriptor.Descriptor(
  name='FlasherEntity',
  full_name='Honeywell.Security.ISOM.Flashers.FlasherEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.Flashers.FlasherEntity.config', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='Honeywell.Security.ISOM.Flashers.FlasherEntity.state', index=1,
      number=12, type=11, cpp_type=10, label=1,
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
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1128,
  serialized_end=1269,
)

_FLASHEROPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_FLASHERSUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_FLASHEREVENTS.fields_by_name['events'].enum_type = _EVENTS
_FLASHERIDENTIFIERSLIST.fields_by_name['identifiers'].message_type = _FLASHERIDENTIFIERS
_FLASHERRELATION.fields_by_name['name'].enum_type = _RELATIONS
_FLASHERRELATIONLIST.fields_by_name['relation'].message_type = _FLASHERRELATION
_FLASHERCONFIG.fields_by_name['identifiers'].message_type = _FLASHERIDENTIFIERS
_FLASHERCONFIG.fields_by_name['relation'].message_type = _FLASHERRELATION
_FLASHERCONFIG.fields_by_name['omit'].enum_type = IsomDevices__pb2._DEVICEOMITTYPE
_FLASHERCONFIGLIST.fields_by_name['config'].message_type = _FLASHERCONFIG
_FLASHERENTITY.fields_by_name['config'].message_type = _FLASHERCONFIG
_FLASHERENTITY.fields_by_name['state'].message_type = IsomDevices__pb2._DEVICESTATE
DESCRIPTOR.message_types_by_name['FlasherOperations'] = _FLASHEROPERATIONS
DESCRIPTOR.message_types_by_name['FlasherSupportedRelations'] = _FLASHERSUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['FlasherEvents'] = _FLASHEREVENTS
DESCRIPTOR.message_types_by_name['FlasherIdentifiers'] = _FLASHERIDENTIFIERS
DESCRIPTOR.message_types_by_name['FlasherIdentifiersList'] = _FLASHERIDENTIFIERSLIST
DESCRIPTOR.message_types_by_name['FlasherRelation'] = _FLASHERRELATION
DESCRIPTOR.message_types_by_name['FlasherRelationList'] = _FLASHERRELATIONLIST
DESCRIPTOR.message_types_by_name['FlasherConfig'] = _FLASHERCONFIG
DESCRIPTOR.message_types_by_name['FlasherConfigList'] = _FLASHERCONFIGLIST
DESCRIPTOR.message_types_by_name['FlasherEntity'] = _FLASHERENTITY
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlasherOperations = _reflection.GeneratedProtocolMessageType('FlasherOperations', (_message.Message,), {
  'DESCRIPTOR' : _FLASHEROPERATIONS,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherOperations)
  })
_sym_db.RegisterMessage(FlasherOperations)

FlasherSupportedRelations = _reflection.GeneratedProtocolMessageType('FlasherSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERSUPPORTEDRELATIONS,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherSupportedRelations)
  })
_sym_db.RegisterMessage(FlasherSupportedRelations)

FlasherEvents = _reflection.GeneratedProtocolMessageType('FlasherEvents', (_message.Message,), {
  'DESCRIPTOR' : _FLASHEREVENTS,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherEvents)
  })
_sym_db.RegisterMessage(FlasherEvents)

FlasherIdentifiers = _reflection.GeneratedProtocolMessageType('FlasherIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERIDENTIFIERS,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherIdentifiers)
  })
_sym_db.RegisterMessage(FlasherIdentifiers)

FlasherIdentifiersList = _reflection.GeneratedProtocolMessageType('FlasherIdentifiersList', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERIDENTIFIERSLIST,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherIdentifiersList)
  })
_sym_db.RegisterMessage(FlasherIdentifiersList)

FlasherRelation = _reflection.GeneratedProtocolMessageType('FlasherRelation', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERRELATION,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherRelation)
  })
_sym_db.RegisterMessage(FlasherRelation)

FlasherRelationList = _reflection.GeneratedProtocolMessageType('FlasherRelationList', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERRELATIONLIST,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherRelationList)
  })
_sym_db.RegisterMessage(FlasherRelationList)

FlasherConfig = _reflection.GeneratedProtocolMessageType('FlasherConfig', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERCONFIG,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherConfig)
  })
_sym_db.RegisterMessage(FlasherConfig)

FlasherConfigList = _reflection.GeneratedProtocolMessageType('FlasherConfigList', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERCONFIGLIST,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherConfigList)
  })
_sym_db.RegisterMessage(FlasherConfigList)

FlasherEntity = _reflection.GeneratedProtocolMessageType('FlasherEntity', (_message.Message,), {
  'DESCRIPTOR' : _FLASHERENTITY,
  '__module__' : 'Flashers_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Flashers.FlasherEntity)
  })
_sym_db.RegisterMessage(FlasherEntity)


# @@protoc_insertion_point(module_scope)