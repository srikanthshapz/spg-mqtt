# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActivationGroupTypes.proto

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
  name='ActivationGroupTypes.proto',
  package='Honeywell.Security.ISOM.ActivationGroupTypes',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1a\x41\x63tivationGroupTypes.proto\x12,Honeywell.Security.ISOM.ActivationGroupTypes\x1a\x10IsomStdDef.proto\"u\n\x1d\x41\x63tivationGroupTypeOperations\x12J\n\tresources\x18\x0b \x03(\x0e\x32\x37.Honeywell.Security.ISOM.ActivationGroupTypes.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"}\n%ActivationGroupTypeSupportedRelations\x12J\n\trelations\x18\x0b \x03(\x0e\x32\x37.Honeywell.Security.ISOM.ActivationGroupTypes.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"k\n\x19\x41\x63tivationGroupTypeEvents\x12\x44\n\x06\x65vents\x18\x0b \x03(\x0e\x32\x34.Honeywell.Security.ISOM.ActivationGroupTypes.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"g\n\x1e\x41\x63tivationGroupTypeIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x8d\x01\n\x1e\x41\x63tivationGroupIdentifiersList\x12\x61\n\x0bidentifiers\x18\x0b \x03(\x0b\x32L.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x8c\x01\n\x1b\x41\x63tivationGroupTypeRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12\x45\n\x04name\x18\x0c \x01(\x0e\x32\x37.Honeywell.Security.ISOM.ActivationGroupTypes.Relations\x12\x10\n\x08\x65ntityId\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"~\n\x1f\x41\x63tivationGroupTypeRelationList\x12[\n\x08relation\x18\x0b \x03(\x0b\x32I.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation\"\xf8\x01\n\x19\x41\x63tivationGroupTypeConfig\x12\x61\n\x0bidentifiers\x18\x0b \x01(\x0b\x32L.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers\x12[\n\x08relation\x18\n \x03(\x0b\x32I.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation\x12\x11\n\x08\x63\x61tegory\x18\xea\x07 \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x82\x01\n\x1d\x41\x63tivationGroupTypeConfigList\x12W\n\x06\x63onfig\x18\x0c \x03(\x0b\x32G.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"~\n\x19\x41\x63tivationGroupTypeEntity\x12W\n\x06\x63onfig\x18\x15 \x01(\x0b\x32G.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"\x82\x01\n\x1d\x41\x63tivationGroupTypeEntityList\x12W\n\x06\x65ntity\x18\x0b \x03(\x0b\x32G.Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xd2\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*T\n\tRelations\x12\x30\n+ActivationGroupTypeAsignedToActivationGroup\x10\xc3N\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*[\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.Resources',
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
  serialized_start=1615,
  serialized_end=1825,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ActivationGroupTypeAsignedToActivationGroup', index=0, number=10051,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=1, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1827,
  serialized_end=1911,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.Events',
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
  serialized_start=1913,
  serialized_end=2004,
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
ActivationGroupTypeAsignedToActivationGroup = 10051
Max_Relations = 1073741824
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
Max_Events = 1073741824



_ACTIVATIONGROUPTYPEOPERATIONS = _descriptor.Descriptor(
  name='ActivationGroupTypeOperations',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeOperations.resources', index=0,
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
  serialized_start=94,
  serialized_end=211,
)


_ACTIVATIONGROUPTYPESUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='ActivationGroupTypeSupportedRelations',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeSupportedRelations.relations', index=0,
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
  serialized_start=213,
  serialized_end=338,
)


_ACTIVATIONGROUPTYPEEVENTS = _descriptor.Descriptor(
  name='ActivationGroupTypeEvents',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEvents.events', index=0,
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
  serialized_start=340,
  serialized_end=447,
)


_ACTIVATIONGROUPTYPEIDENTIFIERS = _descriptor.Descriptor(
  name='ActivationGroupTypeIdentifiers',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers.name', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers.description', index=3,
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
  serialized_start=449,
  serialized_end=552,
)


_ACTIVATIONGROUPIDENTIFIERSLIST = _descriptor.Descriptor(
  name='ActivationGroupIdentifiersList',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupIdentifiersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupIdentifiersList.identifiers', index=0,
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
  serialized_start=555,
  serialized_end=696,
)


_ACTIVATIONGROUPTYPERELATION = _descriptor.Descriptor(
  name='ActivationGroupTypeRelation',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=10051,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation.entityId', index=2,
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
  serialized_start=699,
  serialized_end=839,
)


_ACTIVATIONGROUPTYPERELATIONLIST = _descriptor.Descriptor(
  name='ActivationGroupTypeRelationList',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelationList.relation', index=0,
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
  serialized_start=841,
  serialized_end=967,
)


_ACTIVATIONGROUPTYPECONFIG = _descriptor.Descriptor(
  name='ActivationGroupTypeConfig',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig.relation', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig.category', index=2,
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
  serialized_start=970,
  serialized_end=1218,
)


_ACTIVATIONGROUPTYPECONFIGLIST = _descriptor.Descriptor(
  name='ActivationGroupTypeConfigList',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfigList.config', index=0,
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
  serialized_start=1221,
  serialized_end=1351,
)


_ACTIVATIONGROUPTYPEENTITY = _descriptor.Descriptor(
  name='ActivationGroupTypeEntity',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntity.config', index=0,
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
  serialized_start=1353,
  serialized_end=1479,
)


_ACTIVATIONGROUPTYPEENTITYLIST = _descriptor.Descriptor(
  name='ActivationGroupTypeEntityList',
  full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntityList.entity', index=0,
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
  serialized_start=1482,
  serialized_end=1612,
)

_ACTIVATIONGROUPTYPEOPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_ACTIVATIONGROUPTYPESUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_ACTIVATIONGROUPTYPEEVENTS.fields_by_name['events'].enum_type = _EVENTS
_ACTIVATIONGROUPIDENTIFIERSLIST.fields_by_name['identifiers'].message_type = _ACTIVATIONGROUPTYPEIDENTIFIERS
_ACTIVATIONGROUPTYPERELATION.fields_by_name['name'].enum_type = _RELATIONS
_ACTIVATIONGROUPTYPERELATIONLIST.fields_by_name['relation'].message_type = _ACTIVATIONGROUPTYPERELATION
_ACTIVATIONGROUPTYPECONFIG.fields_by_name['identifiers'].message_type = _ACTIVATIONGROUPTYPEIDENTIFIERS
_ACTIVATIONGROUPTYPECONFIG.fields_by_name['relation'].message_type = _ACTIVATIONGROUPTYPERELATION
_ACTIVATIONGROUPTYPECONFIGLIST.fields_by_name['config'].message_type = _ACTIVATIONGROUPTYPECONFIG
_ACTIVATIONGROUPTYPEENTITY.fields_by_name['config'].message_type = _ACTIVATIONGROUPTYPECONFIG
_ACTIVATIONGROUPTYPEENTITYLIST.fields_by_name['entity'].message_type = _ACTIVATIONGROUPTYPEENTITY
DESCRIPTOR.message_types_by_name['ActivationGroupTypeOperations'] = _ACTIVATIONGROUPTYPEOPERATIONS
DESCRIPTOR.message_types_by_name['ActivationGroupTypeSupportedRelations'] = _ACTIVATIONGROUPTYPESUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['ActivationGroupTypeEvents'] = _ACTIVATIONGROUPTYPEEVENTS
DESCRIPTOR.message_types_by_name['ActivationGroupTypeIdentifiers'] = _ACTIVATIONGROUPTYPEIDENTIFIERS
DESCRIPTOR.message_types_by_name['ActivationGroupIdentifiersList'] = _ACTIVATIONGROUPIDENTIFIERSLIST
DESCRIPTOR.message_types_by_name['ActivationGroupTypeRelation'] = _ACTIVATIONGROUPTYPERELATION
DESCRIPTOR.message_types_by_name['ActivationGroupTypeRelationList'] = _ACTIVATIONGROUPTYPERELATIONLIST
DESCRIPTOR.message_types_by_name['ActivationGroupTypeConfig'] = _ACTIVATIONGROUPTYPECONFIG
DESCRIPTOR.message_types_by_name['ActivationGroupTypeConfigList'] = _ACTIVATIONGROUPTYPECONFIGLIST
DESCRIPTOR.message_types_by_name['ActivationGroupTypeEntity'] = _ACTIVATIONGROUPTYPEENTITY
DESCRIPTOR.message_types_by_name['ActivationGroupTypeEntityList'] = _ACTIVATIONGROUPTYPEENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActivationGroupTypeOperations = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeOperations', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPEOPERATIONS,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeOperations)
  })
_sym_db.RegisterMessage(ActivationGroupTypeOperations)

ActivationGroupTypeSupportedRelations = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPESUPPORTEDRELATIONS,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeSupportedRelations)
  })
_sym_db.RegisterMessage(ActivationGroupTypeSupportedRelations)

ActivationGroupTypeEvents = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeEvents', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPEEVENTS,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEvents)
  })
_sym_db.RegisterMessage(ActivationGroupTypeEvents)

ActivationGroupTypeIdentifiers = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPEIDENTIFIERS,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeIdentifiers)
  })
_sym_db.RegisterMessage(ActivationGroupTypeIdentifiers)

ActivationGroupIdentifiersList = _reflection.GeneratedProtocolMessageType('ActivationGroupIdentifiersList', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPIDENTIFIERSLIST,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupIdentifiersList)
  })
_sym_db.RegisterMessage(ActivationGroupIdentifiersList)

ActivationGroupTypeRelation = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeRelation', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPERELATION,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelation)
  })
_sym_db.RegisterMessage(ActivationGroupTypeRelation)

ActivationGroupTypeRelationList = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeRelationList', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPERELATIONLIST,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeRelationList)
  })
_sym_db.RegisterMessage(ActivationGroupTypeRelationList)

ActivationGroupTypeConfig = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPECONFIG,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfig)
  })
_sym_db.RegisterMessage(ActivationGroupTypeConfig)

ActivationGroupTypeConfigList = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeConfigList', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPECONFIGLIST,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeConfigList)
  })
_sym_db.RegisterMessage(ActivationGroupTypeConfigList)

ActivationGroupTypeEntity = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeEntity', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPEENTITY,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntity)
  })
_sym_db.RegisterMessage(ActivationGroupTypeEntity)

ActivationGroupTypeEntityList = _reflection.GeneratedProtocolMessageType('ActivationGroupTypeEntityList', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVATIONGROUPTYPEENTITYLIST,
  '__module__' : 'ActivationGroupTypes_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.ActivationGroupTypes.ActivationGroupTypeEntityList)
  })
_sym_db.RegisterMessage(ActivationGroupTypeEntityList)


# @@protoc_insertion_point(module_scope)
