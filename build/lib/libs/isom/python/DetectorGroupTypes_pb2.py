# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DetectorGroupTypes.proto

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
  name='DetectorGroupTypes.proto',
  package='Honeywell.Security.ISOM.DetectorGroupTypes',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x44\x65tectorGroupTypes.proto\x12*Honeywell.Security.ISOM.DetectorGroupTypes\x1a\x10IsomStdDef.proto\"e\n\x1c\x44\x65tectorGroupTypeIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x87\x01\n\x1c\x44\x65tectorGroupIdentifiersList\x12]\n\x0bidentifiers\x18\x0b \x03(\x0b\x32H.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x88\x01\n\x19\x44\x65tectorGroupTypeRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12\x43\n\x04name\x18\x0c \x01(\x0e\x32\x35.Honeywell.Security.ISOM.DetectorGroupTypes.Relations\x12\x10\n\x08\x65ntityId\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"x\n\x1d\x44\x65tectorGroupTypeRelationList\x12W\n\x08relation\x18\x0b \x03(\x0b\x32\x45.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation\"H\n\x11\x44GArmingModeFlags\x12\x15\n\rnightStayMode\x18\x0b \x01(\x08\x12\x12\n\ncustomMode\x18\x0c \x01(\x08*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xdb\x02\n\x17\x44\x65tectorGroupTypeConfig\x12]\n\x0bidentifiers\x18\x0b \x01(\x0b\x32H.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers\x12W\n\x08relation\x18\n \x03(\x0b\x32\x45.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation\x12T\n\x0c\x61rmModeFlags\x18\xe8\x07 \x01(\x0b\x32=.Honeywell.Security.ISOM.DetectorGroupTypes.DGArmingModeFlags\x12\x15\n\x0cswingerLimit\x18\xe9\x07 \x01(\x04\x12\x11\n\x08\x63\x61tegory\x18\xea\x07 \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"|\n\x1b\x44\x65tectorGroupTypeConfigList\x12S\n\x06\x63onfig\x18\x0c \x03(\x0b\x32\x43.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"x\n\x17\x44\x65tectorGroupTypeEntity\x12S\n\x06\x63onfig\x18\x15 \x01(\x0b\x32\x43.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"|\n\x1b\x44\x65tectorGroupTypeEntityList\x12S\n\x06\x65ntity\x18\x0b \x03(\x0b\x32\x43.Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xd2\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*P\n\tRelations\x12,\n\'DetectorGroupTypeAsignedToDetectorGroup\x10\xc3N\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*[\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.Resources',
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
  serialized_start=1391,
  serialized_end=1601,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DetectorGroupTypeAsignedToDetectorGroup', index=0, number=10051,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=1, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1603,
  serialized_end=1683,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.Events',
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
  serialized_start=1685,
  serialized_end=1776,
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
Max_Resources = 1073741824
DetectorGroupTypeAsignedToDetectorGroup = 10051
Max_Relations = 1073741824
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
Max_Events = 1073741824



_DETECTORGROUPTYPEIDENTIFIERS = _descriptor.Descriptor(
  name='DetectorGroupTypeIdentifiers',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers.name', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers.description', index=3,
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
  serialized_start=90,
  serialized_end=191,
)


_DETECTORGROUPIDENTIFIERSLIST = _descriptor.Descriptor(
  name='DetectorGroupIdentifiersList',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupIdentifiersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupIdentifiersList.identifiers', index=0,
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
  serialized_start=194,
  serialized_end=329,
)


_DETECTORGROUPTYPERELATION = _descriptor.Descriptor(
  name='DetectorGroupTypeRelation',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=10051,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation.entityId', index=2,
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
  serialized_start=332,
  serialized_end=468,
)


_DETECTORGROUPTYPERELATIONLIST = _descriptor.Descriptor(
  name='DetectorGroupTypeRelationList',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelationList.relation', index=0,
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
  serialized_start=470,
  serialized_end=590,
)


_DGARMINGMODEFLAGS = _descriptor.Descriptor(
  name='DGArmingModeFlags',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DGArmingModeFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nightStayMode', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DGArmingModeFlags.nightStayMode', index=0,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customMode', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DGArmingModeFlags.customMode', index=1,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=592,
  serialized_end=664,
)


_DETECTORGROUPTYPECONFIG = _descriptor.Descriptor(
  name='DetectorGroupTypeConfig',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig.relation', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='armModeFlags', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig.armModeFlags', index=2,
      number=1000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swingerLimit', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig.swingerLimit', index=3,
      number=1001, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig.category', index=4,
      number=1002, type=9, cpp_type=9, label=1,
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
  serialized_start=667,
  serialized_end=1014,
)


_DETECTORGROUPTYPECONFIGLIST = _descriptor.Descriptor(
  name='DetectorGroupTypeConfigList',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfigList.config', index=0,
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
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=1016,
  serialized_end=1140,
)


_DETECTORGROUPTYPEENTITY = _descriptor.Descriptor(
  name='DetectorGroupTypeEntity',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntity.config', index=0,
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
  serialized_start=1142,
  serialized_end=1262,
)


_DETECTORGROUPTYPEENTITYLIST = _descriptor.Descriptor(
  name='DetectorGroupTypeEntityList',
  full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntityList.entity', index=0,
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
  serialized_start=1264,
  serialized_end=1388,
)

_DETECTORGROUPIDENTIFIERSLIST.fields_by_name['identifiers'].message_type = _DETECTORGROUPTYPEIDENTIFIERS
_DETECTORGROUPTYPERELATION.fields_by_name['name'].enum_type = _RELATIONS
_DETECTORGROUPTYPERELATIONLIST.fields_by_name['relation'].message_type = _DETECTORGROUPTYPERELATION
_DETECTORGROUPTYPECONFIG.fields_by_name['identifiers'].message_type = _DETECTORGROUPTYPEIDENTIFIERS
_DETECTORGROUPTYPECONFIG.fields_by_name['relation'].message_type = _DETECTORGROUPTYPERELATION
_DETECTORGROUPTYPECONFIG.fields_by_name['armModeFlags'].message_type = _DGARMINGMODEFLAGS
_DETECTORGROUPTYPECONFIGLIST.fields_by_name['config'].message_type = _DETECTORGROUPTYPECONFIG
_DETECTORGROUPTYPEENTITY.fields_by_name['config'].message_type = _DETECTORGROUPTYPECONFIG
_DETECTORGROUPTYPEENTITYLIST.fields_by_name['entity'].message_type = _DETECTORGROUPTYPEENTITY
DESCRIPTOR.message_types_by_name['DetectorGroupTypeIdentifiers'] = _DETECTORGROUPTYPEIDENTIFIERS
DESCRIPTOR.message_types_by_name['DetectorGroupIdentifiersList'] = _DETECTORGROUPIDENTIFIERSLIST
DESCRIPTOR.message_types_by_name['DetectorGroupTypeRelation'] = _DETECTORGROUPTYPERELATION
DESCRIPTOR.message_types_by_name['DetectorGroupTypeRelationList'] = _DETECTORGROUPTYPERELATIONLIST
DESCRIPTOR.message_types_by_name['DGArmingModeFlags'] = _DGARMINGMODEFLAGS
DESCRIPTOR.message_types_by_name['DetectorGroupTypeConfig'] = _DETECTORGROUPTYPECONFIG
DESCRIPTOR.message_types_by_name['DetectorGroupTypeConfigList'] = _DETECTORGROUPTYPECONFIGLIST
DESCRIPTOR.message_types_by_name['DetectorGroupTypeEntity'] = _DETECTORGROUPTYPEENTITY
DESCRIPTOR.message_types_by_name['DetectorGroupTypeEntityList'] = _DETECTORGROUPTYPEENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetectorGroupTypeIdentifiers = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPEIDENTIFIERS,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeIdentifiers)
  })
_sym_db.RegisterMessage(DetectorGroupTypeIdentifiers)

DetectorGroupIdentifiersList = _reflection.GeneratedProtocolMessageType('DetectorGroupIdentifiersList', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPIDENTIFIERSLIST,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupIdentifiersList)
  })
_sym_db.RegisterMessage(DetectorGroupIdentifiersList)

DetectorGroupTypeRelation = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeRelation', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPERELATION,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelation)
  })
_sym_db.RegisterMessage(DetectorGroupTypeRelation)

DetectorGroupTypeRelationList = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeRelationList', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPERELATIONLIST,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeRelationList)
  })
_sym_db.RegisterMessage(DetectorGroupTypeRelationList)

DGArmingModeFlags = _reflection.GeneratedProtocolMessageType('DGArmingModeFlags', (_message.Message,), {
  'DESCRIPTOR' : _DGARMINGMODEFLAGS,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DGArmingModeFlags)
  })
_sym_db.RegisterMessage(DGArmingModeFlags)

DetectorGroupTypeConfig = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeConfig', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPECONFIG,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfig)
  })
_sym_db.RegisterMessage(DetectorGroupTypeConfig)

DetectorGroupTypeConfigList = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeConfigList', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPECONFIGLIST,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeConfigList)
  })
_sym_db.RegisterMessage(DetectorGroupTypeConfigList)

DetectorGroupTypeEntity = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeEntity', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPEENTITY,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntity)
  })
_sym_db.RegisterMessage(DetectorGroupTypeEntity)

DetectorGroupTypeEntityList = _reflection.GeneratedProtocolMessageType('DetectorGroupTypeEntityList', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORGROUPTYPEENTITYLIST,
  '__module__' : 'DetectorGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DetectorGroupTypes.DetectorGroupTypeEntityList)
  })
_sym_db.RegisterMessage(DetectorGroupTypeEntityList)


# @@protoc_insertion_point(module_scope)