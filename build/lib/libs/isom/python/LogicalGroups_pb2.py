# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LogicalGroups.proto

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
  name='LogicalGroups.proto',
  package='Honeywell.Security.ISOM.LogicalGroups',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13LogicalGroups.proto\x12%Honeywell.Security.ISOM.LogicalGroups\x1a\x10IsomStdDef.proto\"g\n\x16LogicalGroupOperations\x12\x43\n\tresources\x18\x0b \x03(\x0e\x32\x30.Honeywell.Security.ISOM.LogicalGroups.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"o\n\x1eLogicalGroupSupportedRelations\x12\x43\n\trelations\x18\x0b \x03(\x0e\x32\x30.Honeywell.Security.ISOM.LogicalGroups.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"]\n\x12LogicalGroupEvents\x12=\n\x06\x65vents\x18\x0b \x03(\x0e\x32-.Honeywell.Security.ISOM.LogicalGroups.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"~\n\x14LogicalGroupRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12>\n\x04name\x18\x0c \x01(\x0e\x32\x30.Honeywell.Security.ISOM.LogicalGroups.Relations\x12\x10\n\x08\x65ntityId\x18\r \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"i\n\x18LogicalGroupRelationList\x12M\n\x08relation\x18\x0b \x03(\x0b\x32;.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation\"K\n\x17LogicalGroupIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x9a\x02\n\x12LogicalGroupConfig\x12S\n\x0bidentifiers\x18\x0b \x01(\x0b\x32>.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupIdentifiers\x12M\n\x08relation\x18\x0c \x03(\x0b\x32;.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation\x12\x45\n\x04type\x18\r \x01(\x0e\x32\x37.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupType\x12\x0f\n\x07subType\x18\x0e \x01(\t*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"y\n\x16LogicalGroupConfigList\x12U\n\x12LogicalGroupConfig\x18\x0b \x03(\x0b\x32\x39.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"i\n\x12LogicalGroupEntity\x12I\n\x06\x63onfig\x18\x15 \x01(\x0b\x32\x39.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"m\n\x16LogicalGroupEntityList\x12I\n\x06\x65ntity\x18\x0b \x03(\x0b\x32\x39.Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xd2\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*[\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04*\x8d\x02\n\tRelations\x12(\n$LogicalGroupAssociatedToLogicalGroup\x10\x0e\x12*\n&LogicalGroupAssociatedWithLogicalGroup\x10\x0f\x12#\n\x1fLogicalGroupAssociatedToAccount\x10\x10\x12 \n\x1cLogicalGroupAssociatedToSite\x10\x11\x12,\n(LogicalGroupAssociatedToCredentialHolder\x10\x12\x12\x1e\n\x1aLogicalGroupOwnedByAccount\x10\x13\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*c\n\x10LogicalGroupType\x12\x0b\n\x07Unknown\x10\x0b\x12\n\n\x06\x44\x65vice\x10\x0c\x12\x08\n\x04\x41rea\x10\r\x12\x0e\n\nCollection\x10\x0e\x12\x1c\n\x14Max_LogicalGroupType\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.LogicalGroups.Resources',
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
  serialized_start=1332,
  serialized_end=1542,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.LogicalGroups.Events',
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
  serialized_start=1544,
  serialized_end=1635,
)
_sym_db.RegisterEnumDescriptor(_EVENTS)

Events = enum_type_wrapper.EnumTypeWrapper(_EVENTS)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.LogicalGroups.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LogicalGroupAssociatedToLogicalGroup', index=0, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogicalGroupAssociatedWithLogicalGroup', index=1, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogicalGroupAssociatedToAccount', index=2, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogicalGroupAssociatedToSite', index=3, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogicalGroupAssociatedToCredentialHolder', index=4, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LogicalGroupOwnedByAccount', index=5, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=6, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1638,
  serialized_end=1907,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_LOGICALGROUPTYPE = _descriptor.EnumDescriptor(
  name='LogicalGroupType',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Device', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Area', index=2, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Collection', index=3, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_LogicalGroupType', index=4, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1909,
  serialized_end=2008,
)
_sym_db.RegisterEnumDescriptor(_LOGICALGROUPTYPE)

LogicalGroupType = enum_type_wrapper.EnumTypeWrapper(_LOGICALGROUPTYPE)
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
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
Max_Events = 1073741824
LogicalGroupAssociatedToLogicalGroup = 14
LogicalGroupAssociatedWithLogicalGroup = 15
LogicalGroupAssociatedToAccount = 16
LogicalGroupAssociatedToSite = 17
LogicalGroupAssociatedToCredentialHolder = 18
LogicalGroupOwnedByAccount = 19
Max_Relations = 1073741824
Unknown = 11
Device = 12
Area = 13
Collection = 14
Max_LogicalGroupType = 1073741824



_LOGICALGROUPOPERATIONS = _descriptor.Descriptor(
  name='LogicalGroupOperations',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupOperations.resources', index=0,
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
  serialized_start=80,
  serialized_end=183,
)


_LOGICALGROUPSUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='LogicalGroupSupportedRelations',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupSupportedRelations.relations', index=0,
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
  serialized_start=185,
  serialized_end=296,
)


_LOGICALGROUPEVENTS = _descriptor.Descriptor(
  name='LogicalGroupEvents',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEvents.events', index=0,
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
  serialized_start=298,
  serialized_end=391,
)


_LOGICALGROUPRELATION = _descriptor.Descriptor(
  name='LogicalGroupRelation',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=14,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation.entityId', index=2,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=393,
  serialized_end=519,
)


_LOGICALGROUPRELATIONLIST = _descriptor.Descriptor(
  name='LogicalGroupRelationList',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelationList.relation', index=0,
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
  serialized_start=521,
  serialized_end=626,
)


_LOGICALGROUPIDENTIFIERS = _descriptor.Descriptor(
  name='LogicalGroupIdentifiers',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupIdentifiers.name', index=2,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=628,
  serialized_end=703,
)


_LOGICALGROUPCONFIG = _descriptor.Descriptor(
  name='LogicalGroupConfig',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig.relation', index=1,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig.type', index=2,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subType', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig.subType', index=3,
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
  extension_ranges=[(900000, 1100000), ],
  oneofs=[
  ],
  serialized_start=706,
  serialized_end=988,
)


_LOGICALGROUPCONFIGLIST = _descriptor.Descriptor(
  name='LogicalGroupConfigList',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='LogicalGroupConfig', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfigList.LogicalGroupConfig', index=0,
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
  serialized_start=990,
  serialized_end=1111,
)


_LOGICALGROUPENTITY = _descriptor.Descriptor(
  name='LogicalGroupEntity',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntity.config', index=0,
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
  serialized_start=1113,
  serialized_end=1218,
)


_LOGICALGROUPENTITYLIST = _descriptor.Descriptor(
  name='LogicalGroupEntityList',
  full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntityList.entity', index=0,
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
  serialized_start=1220,
  serialized_end=1329,
)

_LOGICALGROUPOPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_LOGICALGROUPSUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_LOGICALGROUPEVENTS.fields_by_name['events'].enum_type = _EVENTS
_LOGICALGROUPRELATION.fields_by_name['name'].enum_type = _RELATIONS
_LOGICALGROUPRELATIONLIST.fields_by_name['relation'].message_type = _LOGICALGROUPRELATION
_LOGICALGROUPCONFIG.fields_by_name['identifiers'].message_type = _LOGICALGROUPIDENTIFIERS
_LOGICALGROUPCONFIG.fields_by_name['relation'].message_type = _LOGICALGROUPRELATION
_LOGICALGROUPCONFIG.fields_by_name['type'].enum_type = _LOGICALGROUPTYPE
_LOGICALGROUPCONFIGLIST.fields_by_name['LogicalGroupConfig'].message_type = _LOGICALGROUPCONFIG
_LOGICALGROUPENTITY.fields_by_name['config'].message_type = _LOGICALGROUPCONFIG
_LOGICALGROUPENTITYLIST.fields_by_name['entity'].message_type = _LOGICALGROUPENTITY
DESCRIPTOR.message_types_by_name['LogicalGroupOperations'] = _LOGICALGROUPOPERATIONS
DESCRIPTOR.message_types_by_name['LogicalGroupSupportedRelations'] = _LOGICALGROUPSUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['LogicalGroupEvents'] = _LOGICALGROUPEVENTS
DESCRIPTOR.message_types_by_name['LogicalGroupRelation'] = _LOGICALGROUPRELATION
DESCRIPTOR.message_types_by_name['LogicalGroupRelationList'] = _LOGICALGROUPRELATIONLIST
DESCRIPTOR.message_types_by_name['LogicalGroupIdentifiers'] = _LOGICALGROUPIDENTIFIERS
DESCRIPTOR.message_types_by_name['LogicalGroupConfig'] = _LOGICALGROUPCONFIG
DESCRIPTOR.message_types_by_name['LogicalGroupConfigList'] = _LOGICALGROUPCONFIGLIST
DESCRIPTOR.message_types_by_name['LogicalGroupEntity'] = _LOGICALGROUPENTITY
DESCRIPTOR.message_types_by_name['LogicalGroupEntityList'] = _LOGICALGROUPENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['LogicalGroupType'] = _LOGICALGROUPTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogicalGroupOperations = _reflection.GeneratedProtocolMessageType('LogicalGroupOperations', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPOPERATIONS,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupOperations)
  })
_sym_db.RegisterMessage(LogicalGroupOperations)

LogicalGroupSupportedRelations = _reflection.GeneratedProtocolMessageType('LogicalGroupSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPSUPPORTEDRELATIONS,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupSupportedRelations)
  })
_sym_db.RegisterMessage(LogicalGroupSupportedRelations)

LogicalGroupEvents = _reflection.GeneratedProtocolMessageType('LogicalGroupEvents', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPEVENTS,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEvents)
  })
_sym_db.RegisterMessage(LogicalGroupEvents)

LogicalGroupRelation = _reflection.GeneratedProtocolMessageType('LogicalGroupRelation', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPRELATION,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelation)
  })
_sym_db.RegisterMessage(LogicalGroupRelation)

LogicalGroupRelationList = _reflection.GeneratedProtocolMessageType('LogicalGroupRelationList', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPRELATIONLIST,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupRelationList)
  })
_sym_db.RegisterMessage(LogicalGroupRelationList)

LogicalGroupIdentifiers = _reflection.GeneratedProtocolMessageType('LogicalGroupIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPIDENTIFIERS,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupIdentifiers)
  })
_sym_db.RegisterMessage(LogicalGroupIdentifiers)

LogicalGroupConfig = _reflection.GeneratedProtocolMessageType('LogicalGroupConfig', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPCONFIG,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfig)
  })
_sym_db.RegisterMessage(LogicalGroupConfig)

LogicalGroupConfigList = _reflection.GeneratedProtocolMessageType('LogicalGroupConfigList', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPCONFIGLIST,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupConfigList)
  })
_sym_db.RegisterMessage(LogicalGroupConfigList)

LogicalGroupEntity = _reflection.GeneratedProtocolMessageType('LogicalGroupEntity', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPENTITY,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntity)
  })
_sym_db.RegisterMessage(LogicalGroupEntity)

LogicalGroupEntityList = _reflection.GeneratedProtocolMessageType('LogicalGroupEntityList', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALGROUPENTITYLIST,
  '__module__' : 'LogicalGroups_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.LogicalGroups.LogicalGroupEntityList)
  })
_sym_db.RegisterMessage(LogicalGroupEntityList)


# @@protoc_insertion_point(module_scope)