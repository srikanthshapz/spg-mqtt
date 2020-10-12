# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PMCollections.proto

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
import PMs_pb2 as PMs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='PMCollections.proto',
  package='Honeywell.Security.ISOM.PMCollections',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x13PMCollections.proto\x12%Honeywell.Security.ISOM.PMCollections\x1a\x10IsomStdDef.proto\x1a\tPMs.proto\"g\n\x16PMCollectionOperations\x12\x43\n\tresources\x18\x0b \x03(\x0e\x32\x30.Honeywell.Security.ISOM.PMCollections.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"o\n\x1ePMCollectionSupportedRelations\x12\x43\n\trelations\x18\x0b \x03(\x0e\x32\x30.Honeywell.Security.ISOM.PMCollections.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"]\n\x12PMCollectionEvents\x12=\n\x06\x65vents\x18\x0b \x03(\x0e\x32-.Honeywell.Security.ISOM.PMCollections.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"$\n\x18PMCollectionTriggerState*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"Z\n\x11PMCollectionState\x12;\n\tomitState\x18\r \x01(\x0b\x32(.Honeywell.Security.ISOM.PMs.PMOmitState*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"`\n\x17PMCollectionIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"|\n\x1bPMCollectionIdentifiersList\x12S\n\x0bidentifiers\x18\x0b \x03(\x0b\x32>.Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"~\n\x14PMCollectionRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12>\n\x04name\x18\x0c \x01(\x0e\x32\x30.Honeywell.Security.ISOM.PMCollections.Relations\x12\x10\n\x08\x65ntityId\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"i\n\x18PMCollectionRelationList\x12M\n\x08relation\x18\x0b \x03(\x0b\x32;.Honeywell.Security.ISOM.PMCollections.PMCollectionRelation\"a\n\x18PMCollectionMemberConfig\x12;\n\x06member\x18\x17 \x01(\x0b\x32+.Honeywell.Security.ISOM.IsomEntityInstance*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xb2\x04\n\x12PMCollectionConfig\x12S\n\x0bidentifiers\x18\x0b \x01(\x0b\x32>.Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers\x12M\n\x08relation\x18\n \x03(\x0b\x32;.Honeywell.Security.ISOM.PMCollections.PMCollectionRelation\x12\x45\n\x04type\x18\x14 \x01(\x0e\x32\x37.Honeywell.Security.ISOM.PMCollections.PMCollectionType\x12\x39\n\x08omitType\x18\x15 \x01(\x0e\x32\'.Honeywell.Security.ISOM.PMs.PMOmitType\x12\x13\n\x0borderedList\x18\x16 \x01(\x08\x12U\n\x0cmemberConfig\x18\x17 \x03(\x0b\x32?.Honeywell.Security.ISOM.PMCollections.PMCollectionMemberConfig\x12\x1f\n\x17minActivationsToTrigger\x18\x19 \x01(\x04\x12N\n\x19overallDurationForTrigger\x18\x1a \x01(\x0b\x32%.Honeywell.Security.ISOM.IsomDurationB\x04\x90\xb5\x18\x11\x12\x0f\n\x07subType\x18\x1b \x01(\t*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"m\n\x16PMCollectionConfigList\x12I\n\x06\x63onfig\x18\x0c \x03(\x0b\x32\x39.Honeywell.Security.ISOM.PMCollections.PMCollectionConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xb2\x01\n\x12PMCollectionEntity\x12I\n\x06\x63onfig\x18\x15 \x01(\x0b\x32\x39.Honeywell.Security.ISOM.PMCollections.PMCollectionConfig\x12G\n\x05state\x18\x1f \x01(\x0b\x32\x38.Honeywell.Security.ISOM.PMCollections.PMCollectionState*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"m\n\x16PMCollectionEntityList\x12I\n\x06\x65ntity\x18\x0b \x03(\x0b\x32\x39.Honeywell.Security.ISOM.PMCollections.PMCollectionEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xde\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\n\n\x05state\x10\xceO\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*\x98\x02\n\tRelations\x12!\n\x1cPMCollectionOwnedByPartition\x10\xc3N\x12\x1b\n\x16PMCollectionRefersToPM\x10\xc4N\x12#\n\x1ePMCollectionAsExitForPartition\x10\xc5N\x12$\n\x1fPMCollectionAsEntryForPartition\x10\xc6N\x12$\n\x1fPMCollectionAssignedToPartition\x10\xc7N\x12 \n\x1bPMCollectionAssociatedMacro\x10\xc8N\x12!\n\x1cPMCollectionTemplateInSystem\x10\xc9N\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*w\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x1a\n\x15triggerState_p_active\x10\x9dN\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04*O\n\x17PMCollectionTriggerType\x12\n\n\x06normal\x10\x0b\x12\x0b\n\x07started\x10\x0c\x12\x0c\n\x08timedOut\x10\r\x12\r\n\ttriggered\x10\x0e*l\n\x15PMAllertTriggerSource\x12\x14\n\x10PartitionFullSet\x10\x0b\x12\x1a\n\x16PMCollectionStartState\x10\x0c\x12!\n\x19Max_PMAllertTriggerSource\x10\x80\x80\x80\x80\x04*_\n\x10PMCollectionType\x12\x0e\n\nEntryRoute\x10\x0b\x12\r\n\tExitRoute\x10\x0c\x12\x0e\n\nDependency\x10\r\x12\x1c\n\x14Max_PMCollectionType\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,PMs__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.PMCollections.Resources',
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
      name='state', index=9, number=10190,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Resources', index=10, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2061,
  serialized_end=2283,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.PMCollections.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PMCollectionOwnedByPartition', index=0, number=10051,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionRefersToPM', index=1, number=10052,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionAsExitForPartition', index=2, number=10053,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionAsEntryForPartition', index=3, number=10054,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionAssignedToPartition', index=4, number=10055,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionAssociatedMacro', index=5, number=10056,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionTemplateInSystem', index=6, number=10057,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=7, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2286,
  serialized_end=2566,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.PMCollections.Events',
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
      name='triggerState_p_active', index=3, number=10013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Events', index=4, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2568,
  serialized_end=2687,
)
_sym_db.RegisterEnumDescriptor(_EVENTS)

Events = enum_type_wrapper.EnumTypeWrapper(_EVENTS)
_PMCOLLECTIONTRIGGERTYPE = _descriptor.EnumDescriptor(
  name='PMCollectionTriggerType',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionTriggerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='normal', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='started', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='timedOut', index=2, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='triggered', index=3, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2689,
  serialized_end=2768,
)
_sym_db.RegisterEnumDescriptor(_PMCOLLECTIONTRIGGERTYPE)

PMCollectionTriggerType = enum_type_wrapper.EnumTypeWrapper(_PMCOLLECTIONTRIGGERTYPE)
_PMALLERTTRIGGERSOURCE = _descriptor.EnumDescriptor(
  name='PMAllertTriggerSource',
  full_name='Honeywell.Security.ISOM.PMCollections.PMAllertTriggerSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PartitionFullSet', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PMCollectionStartState', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_PMAllertTriggerSource', index=2, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2770,
  serialized_end=2878,
)
_sym_db.RegisterEnumDescriptor(_PMALLERTTRIGGERSOURCE)

PMAllertTriggerSource = enum_type_wrapper.EnumTypeWrapper(_PMALLERTTRIGGERSOURCE)
_PMCOLLECTIONTYPE = _descriptor.EnumDescriptor(
  name='PMCollectionType',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EntryRoute', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ExitRoute', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Dependency', index=2, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_PMCollectionType', index=3, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2880,
  serialized_end=2975,
)
_sym_db.RegisterEnumDescriptor(_PMCOLLECTIONTYPE)

PMCollectionType = enum_type_wrapper.EnumTypeWrapper(_PMCOLLECTIONTYPE)
supportedOperations = 1010
supportedRelations = 1011
supportedEvents = 1012
supportedCapabilities = 1013
fullEntity = 10050
info = 10051
config = 10071
identifiers = 10091
relations = 10111
state = 10190
Max_Resources = 1073741824
PMCollectionOwnedByPartition = 10051
PMCollectionRefersToPM = 10052
PMCollectionAsExitForPartition = 10053
PMCollectionAsEntryForPartition = 10054
PMCollectionAssignedToPartition = 10055
PMCollectionAssociatedMacro = 10056
PMCollectionTemplateInSystem = 10057
Max_Relations = 1073741824
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
triggerState_p_active = 10013
Max_Events = 1073741824
normal = 11
started = 12
timedOut = 13
triggered = 14
PartitionFullSet = 11
PMCollectionStartState = 12
Max_PMAllertTriggerSource = 1073741824
EntryRoute = 11
ExitRoute = 12
Dependency = 13
Max_PMCollectionType = 1073741824



_PMCOLLECTIONOPERATIONS = _descriptor.Descriptor(
  name='PMCollectionOperations',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionOperations.resources', index=0,
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
  serialized_start=91,
  serialized_end=194,
)


_PMCOLLECTIONSUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='PMCollectionSupportedRelations',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionSupportedRelations.relations', index=0,
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
  serialized_start=196,
  serialized_end=307,
)


_PMCOLLECTIONEVENTS = _descriptor.Descriptor(
  name='PMCollectionEvents',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEvents.events', index=0,
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
  serialized_start=309,
  serialized_end=402,
)


_PMCOLLECTIONTRIGGERSTATE = _descriptor.Descriptor(
  name='PMCollectionTriggerState',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionTriggerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=404,
  serialized_end=440,
)


_PMCOLLECTIONSTATE = _descriptor.Descriptor(
  name='PMCollectionState',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='omitState', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionState.omitState', index=0,
      number=13, type=11, cpp_type=10, label=1,
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
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=532,
)


_PMCOLLECTIONIDENTIFIERS = _descriptor.Descriptor(
  name='PMCollectionIdentifiers',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers.name', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers.description', index=3,
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
  serialized_start=534,
  serialized_end=630,
)


_PMCOLLECTIONIDENTIFIERSLIST = _descriptor.Descriptor(
  name='PMCollectionIdentifiersList',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiersList.identifiers', index=0,
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
  serialized_start=632,
  serialized_end=756,
)


_PMCOLLECTIONRELATION = _descriptor.Descriptor(
  name='PMCollectionRelation',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=10051,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionRelation.entityId', index=2,
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
  serialized_start=758,
  serialized_end=884,
)


_PMCOLLECTIONRELATIONLIST = _descriptor.Descriptor(
  name='PMCollectionRelationList',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionRelationList.relation', index=0,
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
  serialized_start=886,
  serialized_end=991,
)


_PMCOLLECTIONMEMBERCONFIG = _descriptor.Descriptor(
  name='PMCollectionMemberConfig',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionMemberConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionMemberConfig.member', index=0,
      number=23, type=11, cpp_type=10, label=1,
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
  extension_ranges=[(1000000, 1100000), ],
  oneofs=[
  ],
  serialized_start=993,
  serialized_end=1090,
)


_PMCOLLECTIONCONFIG = _descriptor.Descriptor(
  name='PMCollectionConfig',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.relation', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.type', index=2,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='omitType', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.omitType', index=3,
      number=21, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderedList', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.orderedList', index=4,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memberConfig', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.memberConfig', index=5,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minActivationsToTrigger', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.minActivationsToTrigger', index=6,
      number=25, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overallDurationForTrigger', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.overallDurationForTrigger', index=7,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\220\265\030\021'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subType', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfig.subType', index=8,
      number=27, type=9, cpp_type=9, label=1,
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
  serialized_start=1093,
  serialized_end=1655,
)


_PMCOLLECTIONCONFIGLIST = _descriptor.Descriptor(
  name='PMCollectionConfigList',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionConfigList.config', index=0,
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
  serialized_start=1657,
  serialized_end=1766,
)


_PMCOLLECTIONENTITY = _descriptor.Descriptor(
  name='PMCollectionEntity',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEntity.config', index=0,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEntity.state', index=1,
      number=31, type=11, cpp_type=10, label=1,
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
  serialized_start=1769,
  serialized_end=1947,
)


_PMCOLLECTIONENTITYLIST = _descriptor.Descriptor(
  name='PMCollectionEntityList',
  full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.PMCollections.PMCollectionEntityList.entity', index=0,
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
  serialized_start=1949,
  serialized_end=2058,
)

_PMCOLLECTIONOPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_PMCOLLECTIONSUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_PMCOLLECTIONEVENTS.fields_by_name['events'].enum_type = _EVENTS
_PMCOLLECTIONSTATE.fields_by_name['omitState'].message_type = PMs__pb2._PMOMITSTATE
_PMCOLLECTIONIDENTIFIERSLIST.fields_by_name['identifiers'].message_type = _PMCOLLECTIONIDENTIFIERS
_PMCOLLECTIONRELATION.fields_by_name['name'].enum_type = _RELATIONS
_PMCOLLECTIONRELATIONLIST.fields_by_name['relation'].message_type = _PMCOLLECTIONRELATION
_PMCOLLECTIONMEMBERCONFIG.fields_by_name['member'].message_type = IsomStdDef__pb2._ISOMENTITYINSTANCE
_PMCOLLECTIONCONFIG.fields_by_name['identifiers'].message_type = _PMCOLLECTIONIDENTIFIERS
_PMCOLLECTIONCONFIG.fields_by_name['relation'].message_type = _PMCOLLECTIONRELATION
_PMCOLLECTIONCONFIG.fields_by_name['type'].enum_type = _PMCOLLECTIONTYPE
_PMCOLLECTIONCONFIG.fields_by_name['omitType'].enum_type = PMs__pb2._PMOMITTYPE
_PMCOLLECTIONCONFIG.fields_by_name['memberConfig'].message_type = _PMCOLLECTIONMEMBERCONFIG
_PMCOLLECTIONCONFIG.fields_by_name['overallDurationForTrigger'].message_type = IsomStdDef__pb2._ISOMDURATION
_PMCOLLECTIONCONFIGLIST.fields_by_name['config'].message_type = _PMCOLLECTIONCONFIG
_PMCOLLECTIONENTITY.fields_by_name['config'].message_type = _PMCOLLECTIONCONFIG
_PMCOLLECTIONENTITY.fields_by_name['state'].message_type = _PMCOLLECTIONSTATE
_PMCOLLECTIONENTITYLIST.fields_by_name['entity'].message_type = _PMCOLLECTIONENTITY
DESCRIPTOR.message_types_by_name['PMCollectionOperations'] = _PMCOLLECTIONOPERATIONS
DESCRIPTOR.message_types_by_name['PMCollectionSupportedRelations'] = _PMCOLLECTIONSUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['PMCollectionEvents'] = _PMCOLLECTIONEVENTS
DESCRIPTOR.message_types_by_name['PMCollectionTriggerState'] = _PMCOLLECTIONTRIGGERSTATE
DESCRIPTOR.message_types_by_name['PMCollectionState'] = _PMCOLLECTIONSTATE
DESCRIPTOR.message_types_by_name['PMCollectionIdentifiers'] = _PMCOLLECTIONIDENTIFIERS
DESCRIPTOR.message_types_by_name['PMCollectionIdentifiersList'] = _PMCOLLECTIONIDENTIFIERSLIST
DESCRIPTOR.message_types_by_name['PMCollectionRelation'] = _PMCOLLECTIONRELATION
DESCRIPTOR.message_types_by_name['PMCollectionRelationList'] = _PMCOLLECTIONRELATIONLIST
DESCRIPTOR.message_types_by_name['PMCollectionMemberConfig'] = _PMCOLLECTIONMEMBERCONFIG
DESCRIPTOR.message_types_by_name['PMCollectionConfig'] = _PMCOLLECTIONCONFIG
DESCRIPTOR.message_types_by_name['PMCollectionConfigList'] = _PMCOLLECTIONCONFIGLIST
DESCRIPTOR.message_types_by_name['PMCollectionEntity'] = _PMCOLLECTIONENTITY
DESCRIPTOR.message_types_by_name['PMCollectionEntityList'] = _PMCOLLECTIONENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
DESCRIPTOR.enum_types_by_name['PMCollectionTriggerType'] = _PMCOLLECTIONTRIGGERTYPE
DESCRIPTOR.enum_types_by_name['PMAllertTriggerSource'] = _PMALLERTTRIGGERSOURCE
DESCRIPTOR.enum_types_by_name['PMCollectionType'] = _PMCOLLECTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PMCollectionOperations = _reflection.GeneratedProtocolMessageType('PMCollectionOperations', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONOPERATIONS,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionOperations)
  })
_sym_db.RegisterMessage(PMCollectionOperations)

PMCollectionSupportedRelations = _reflection.GeneratedProtocolMessageType('PMCollectionSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONSUPPORTEDRELATIONS,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionSupportedRelations)
  })
_sym_db.RegisterMessage(PMCollectionSupportedRelations)

PMCollectionEvents = _reflection.GeneratedProtocolMessageType('PMCollectionEvents', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONEVENTS,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionEvents)
  })
_sym_db.RegisterMessage(PMCollectionEvents)

PMCollectionTriggerState = _reflection.GeneratedProtocolMessageType('PMCollectionTriggerState', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONTRIGGERSTATE,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionTriggerState)
  })
_sym_db.RegisterMessage(PMCollectionTriggerState)

PMCollectionState = _reflection.GeneratedProtocolMessageType('PMCollectionState', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONSTATE,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionState)
  })
_sym_db.RegisterMessage(PMCollectionState)

PMCollectionIdentifiers = _reflection.GeneratedProtocolMessageType('PMCollectionIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONIDENTIFIERS,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiers)
  })
_sym_db.RegisterMessage(PMCollectionIdentifiers)

PMCollectionIdentifiersList = _reflection.GeneratedProtocolMessageType('PMCollectionIdentifiersList', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONIDENTIFIERSLIST,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionIdentifiersList)
  })
_sym_db.RegisterMessage(PMCollectionIdentifiersList)

PMCollectionRelation = _reflection.GeneratedProtocolMessageType('PMCollectionRelation', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONRELATION,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionRelation)
  })
_sym_db.RegisterMessage(PMCollectionRelation)

PMCollectionRelationList = _reflection.GeneratedProtocolMessageType('PMCollectionRelationList', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONRELATIONLIST,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionRelationList)
  })
_sym_db.RegisterMessage(PMCollectionRelationList)

PMCollectionMemberConfig = _reflection.GeneratedProtocolMessageType('PMCollectionMemberConfig', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONMEMBERCONFIG,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionMemberConfig)
  })
_sym_db.RegisterMessage(PMCollectionMemberConfig)

PMCollectionConfig = _reflection.GeneratedProtocolMessageType('PMCollectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONCONFIG,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionConfig)
  })
_sym_db.RegisterMessage(PMCollectionConfig)

PMCollectionConfigList = _reflection.GeneratedProtocolMessageType('PMCollectionConfigList', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONCONFIGLIST,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionConfigList)
  })
_sym_db.RegisterMessage(PMCollectionConfigList)

PMCollectionEntity = _reflection.GeneratedProtocolMessageType('PMCollectionEntity', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONENTITY,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionEntity)
  })
_sym_db.RegisterMessage(PMCollectionEntity)

PMCollectionEntityList = _reflection.GeneratedProtocolMessageType('PMCollectionEntityList', (_message.Message,), {
  'DESCRIPTOR' : _PMCOLLECTIONENTITYLIST,
  '__module__' : 'PMCollections_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.PMCollections.PMCollectionEntityList)
  })
_sym_db.RegisterMessage(PMCollectionEntityList)


_PMCOLLECTIONCONFIG.fields_by_name['overallDurationForTrigger']._options = None
# @@protoc_insertion_point(module_scope)
