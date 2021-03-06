# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Sites.proto

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
  name='Sites.proto',
  package='Honeywell.Security.ISOM.Sites',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0bSites.proto\x12\x1dHoneywell.Security.ISOM.Sites\x1a\x10IsomStdDef.proto\"W\n\x0eSiteOperations\x12;\n\tresources\x18\x0b \x03(\x0e\x32(.Honeywell.Security.ISOM.Sites.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"_\n\x16SiteSupportedRelations\x12;\n\trelations\x18\x0b \x03(\x0e\x32(.Honeywell.Security.ISOM.Sites.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"M\n\nSiteEvents\x12\x35\n\x06\x65vents\x18\x0b \x03(\x0e\x32%.Honeywell.Security.ISOM.Sites.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"n\n\x0cSiteRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12\x36\n\x04name\x18\x0c \x01(\x0e\x32(.Honeywell.Security.ISOM.Sites.Relations\x12\x10\n\x08\x65ntityId\x18\r \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"Q\n\x10SiteRelationList\x12=\n\x08relation\x18\x0b \x03(\x0b\x32+.Honeywell.Security.ISOM.Sites.SiteRelation\"\xc2\x01\n\x0fSiteIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t\x12\x37\n\x08location\x18\x0f \x01(\x0b\x32%.Honeywell.Security.ISOM.IsomLocation\x12\x10\n\x08photoRef\x18\x10 \x01(\x0c\x12\x0c\n\x04\x63ode\x18\x11 \x01(\t\x12\x0f\n\x07refLink\x18\x12 \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\x9a\x01\n\nSiteConfig\x12\x43\n\x0bidentifiers\x18\x0b \x01(\x0b\x32..Honeywell.Security.ISOM.Sites.SiteIdentifiers\x12=\n\x08relation\x18\x0c \x03(\x0b\x32+.Honeywell.Security.ISOM.Sites.SiteRelation*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"Y\n\x0eSiteConfigList\x12=\n\nsiteConfig\x18\x0b \x03(\x0b\x32).Honeywell.Security.ISOM.Sites.SiteConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"Q\n\nSiteEntity\x12\x39\n\x06\x63onfig\x18\x15 \x01(\x0b\x32).Honeywell.Security.ISOM.Sites.SiteConfig*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"U\n\x0eSiteEntityList\x12\x39\n\x06\x65ntity\x18\x0b \x03(\x0b\x32).Honeywell.Security.ISOM.Sites.SiteEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xd2\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*[\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN\x12\x12\n\nMax_Events\x10\x80\x80\x80\x80\x04*\x84\x04\n\tRelations\x12\x14\n\x10SiteOwnsRecorder\x10\x0b\x12\x12\n\x0eSiteOwnsCamera\x10\x0c\x12\x12\n\x0eSiteOwnsOutput\x10\x0e\x12\x11\n\rSiteOwnsInput\x10\x0f\x12\x15\n\x11SiteOwnsPartition\x10\x10\x12\x0e\n\nSiteOwnsPM\x10\x11\x12\x18\n\x14SiteOwnsPMCollection\x10\x12\x12\x12\n\x0eSiteOwnsDevice\x10\x13\x12\x13\n\x0fSiteOwnsHoliday\x10\x14\x12\x14\n\x10SiteOwnsSchedule\x10\x15\x12\x16\n\x12SiteOwnsPermission\x10\x18\x12\x16\n\x12SiteOwnsCredential\x10\x19\x12\x1c\n\x18SiteOwnsCredentialHolder\x10\x1a\x12\x13\n\x0fSiteOwnedBySite\x10\x1b\x12\x10\n\x0cSiteOwnsSite\x10\x1c\x12\x16\n\x12SiteOwnedByAccount\x10\x1d\x12\x1f\n\x1bSiteOwnedByCredentialHolder\x10\x1e\x12\x10\n\x0cSiteOwnsDoor\x10\x1f\x12\"\n\x1eSiteAssociatedWithLogicalGroup\x10 \x12\x13\n\x0fSiteOwnsAccount\x10!\x12\x16\n\x12SiteOwnsPeripheral\x10#\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.Sites.Resources',
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
  serialized_start=1140,
  serialized_end=1350,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.Sites.Events',
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
  serialized_start=1352,
  serialized_end=1443,
)
_sym_db.RegisterEnumDescriptor(_EVENTS)

Events = enum_type_wrapper.EnumTypeWrapper(_EVENTS)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.Sites.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsRecorder', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsCamera', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsOutput', index=2, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsInput', index=3, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsPartition', index=4, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsPM', index=5, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsPMCollection', index=6, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsDevice', index=7, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsHoliday', index=8, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsSchedule', index=9, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsPermission', index=10, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsCredential', index=11, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsCredentialHolder', index=12, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnedBySite', index=13, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsSite', index=14, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnedByAccount', index=15, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnedByCredentialHolder', index=16, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsDoor', index=17, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteAssociatedWithLogicalGroup', index=18, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsAccount', index=19, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SiteOwnsPeripheral', index=20, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=21, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1446,
  serialized_end=1962,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
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
SiteOwnsRecorder = 11
SiteOwnsCamera = 12
SiteOwnsOutput = 14
SiteOwnsInput = 15
SiteOwnsPartition = 16
SiteOwnsPM = 17
SiteOwnsPMCollection = 18
SiteOwnsDevice = 19
SiteOwnsHoliday = 20
SiteOwnsSchedule = 21
SiteOwnsPermission = 24
SiteOwnsCredential = 25
SiteOwnsCredentialHolder = 26
SiteOwnedBySite = 27
SiteOwnsSite = 28
SiteOwnedByAccount = 29
SiteOwnedByCredentialHolder = 30
SiteOwnsDoor = 31
SiteAssociatedWithLogicalGroup = 32
SiteOwnsAccount = 33
SiteOwnsPeripheral = 35
Max_Relations = 1073741824



_SITEOPERATIONS = _descriptor.Descriptor(
  name='SiteOperations',
  full_name='Honeywell.Security.ISOM.Sites.SiteOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.Sites.SiteOperations.resources', index=0,
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
  serialized_start=64,
  serialized_end=151,
)


_SITESUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='SiteSupportedRelations',
  full_name='Honeywell.Security.ISOM.Sites.SiteSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.Sites.SiteSupportedRelations.relations', index=0,
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
  serialized_start=153,
  serialized_end=248,
)


_SITEEVENTS = _descriptor.Descriptor(
  name='SiteEvents',
  full_name='Honeywell.Security.ISOM.Sites.SiteEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.Sites.SiteEvents.events', index=0,
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
  serialized_start=250,
  serialized_end=327,
)


_SITERELATION = _descriptor.Descriptor(
  name='SiteRelation',
  full_name='Honeywell.Security.ISOM.Sites.SiteRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.Sites.SiteRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.Sites.SiteRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.Sites.SiteRelation.entityId', index=2,
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
  serialized_start=329,
  serialized_end=439,
)


_SITERELATIONLIST = _descriptor.Descriptor(
  name='SiteRelationList',
  full_name='Honeywell.Security.ISOM.Sites.SiteRelationList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.Sites.SiteRelationList.relation', index=0,
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
  serialized_start=441,
  serialized_end=522,
)


_SITEIDENTIFIERS = _descriptor.Descriptor(
  name='SiteIdentifiers',
  full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.name', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.description', index=3,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.location', index=4,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='photoRef', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.photoRef', index=5,
      number=16, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.code', index=6,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refLink', full_name='Honeywell.Security.ISOM.Sites.SiteIdentifiers.refLink', index=7,
      number=18, type=9, cpp_type=9, label=1,
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
  serialized_start=525,
  serialized_end=719,
)


_SITECONFIG = _descriptor.Descriptor(
  name='SiteConfig',
  full_name='Honeywell.Security.ISOM.Sites.SiteConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.Sites.SiteConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.Sites.SiteConfig.relation', index=1,
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
  extension_ranges=[(900000, 1100000), ],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=876,
)


_SITECONFIGLIST = _descriptor.Descriptor(
  name='SiteConfigList',
  full_name='Honeywell.Security.ISOM.Sites.SiteConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='siteConfig', full_name='Honeywell.Security.ISOM.Sites.SiteConfigList.siteConfig', index=0,
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
  serialized_start=878,
  serialized_end=967,
)


_SITEENTITY = _descriptor.Descriptor(
  name='SiteEntity',
  full_name='Honeywell.Security.ISOM.Sites.SiteEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.Sites.SiteEntity.config', index=0,
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
  serialized_start=969,
  serialized_end=1050,
)


_SITEENTITYLIST = _descriptor.Descriptor(
  name='SiteEntityList',
  full_name='Honeywell.Security.ISOM.Sites.SiteEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.Sites.SiteEntityList.entity', index=0,
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
  serialized_start=1052,
  serialized_end=1137,
)

_SITEOPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_SITESUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_SITEEVENTS.fields_by_name['events'].enum_type = _EVENTS
_SITERELATION.fields_by_name['name'].enum_type = _RELATIONS
_SITERELATIONLIST.fields_by_name['relation'].message_type = _SITERELATION
_SITEIDENTIFIERS.fields_by_name['location'].message_type = IsomStdDef__pb2._ISOMLOCATION
_SITECONFIG.fields_by_name['identifiers'].message_type = _SITEIDENTIFIERS
_SITECONFIG.fields_by_name['relation'].message_type = _SITERELATION
_SITECONFIGLIST.fields_by_name['siteConfig'].message_type = _SITECONFIG
_SITEENTITY.fields_by_name['config'].message_type = _SITECONFIG
_SITEENTITYLIST.fields_by_name['entity'].message_type = _SITEENTITY
DESCRIPTOR.message_types_by_name['SiteOperations'] = _SITEOPERATIONS
DESCRIPTOR.message_types_by_name['SiteSupportedRelations'] = _SITESUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['SiteEvents'] = _SITEEVENTS
DESCRIPTOR.message_types_by_name['SiteRelation'] = _SITERELATION
DESCRIPTOR.message_types_by_name['SiteRelationList'] = _SITERELATIONLIST
DESCRIPTOR.message_types_by_name['SiteIdentifiers'] = _SITEIDENTIFIERS
DESCRIPTOR.message_types_by_name['SiteConfig'] = _SITECONFIG
DESCRIPTOR.message_types_by_name['SiteConfigList'] = _SITECONFIGLIST
DESCRIPTOR.message_types_by_name['SiteEntity'] = _SITEENTITY
DESCRIPTOR.message_types_by_name['SiteEntityList'] = _SITEENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SiteOperations = _reflection.GeneratedProtocolMessageType('SiteOperations', (_message.Message,), {
  'DESCRIPTOR' : _SITEOPERATIONS,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteOperations)
  })
_sym_db.RegisterMessage(SiteOperations)

SiteSupportedRelations = _reflection.GeneratedProtocolMessageType('SiteSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _SITESUPPORTEDRELATIONS,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteSupportedRelations)
  })
_sym_db.RegisterMessage(SiteSupportedRelations)

SiteEvents = _reflection.GeneratedProtocolMessageType('SiteEvents', (_message.Message,), {
  'DESCRIPTOR' : _SITEEVENTS,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteEvents)
  })
_sym_db.RegisterMessage(SiteEvents)

SiteRelation = _reflection.GeneratedProtocolMessageType('SiteRelation', (_message.Message,), {
  'DESCRIPTOR' : _SITERELATION,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteRelation)
  })
_sym_db.RegisterMessage(SiteRelation)

SiteRelationList = _reflection.GeneratedProtocolMessageType('SiteRelationList', (_message.Message,), {
  'DESCRIPTOR' : _SITERELATIONLIST,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteRelationList)
  })
_sym_db.RegisterMessage(SiteRelationList)

SiteIdentifiers = _reflection.GeneratedProtocolMessageType('SiteIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _SITEIDENTIFIERS,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteIdentifiers)
  })
_sym_db.RegisterMessage(SiteIdentifiers)

SiteConfig = _reflection.GeneratedProtocolMessageType('SiteConfig', (_message.Message,), {
  'DESCRIPTOR' : _SITECONFIG,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteConfig)
  })
_sym_db.RegisterMessage(SiteConfig)

SiteConfigList = _reflection.GeneratedProtocolMessageType('SiteConfigList', (_message.Message,), {
  'DESCRIPTOR' : _SITECONFIGLIST,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteConfigList)
  })
_sym_db.RegisterMessage(SiteConfigList)

SiteEntity = _reflection.GeneratedProtocolMessageType('SiteEntity', (_message.Message,), {
  'DESCRIPTOR' : _SITEENTITY,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteEntity)
  })
_sym_db.RegisterMessage(SiteEntity)

SiteEntityList = _reflection.GeneratedProtocolMessageType('SiteEntityList', (_message.Message,), {
  'DESCRIPTOR' : _SITEENTITYLIST,
  '__module__' : 'Sites_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.Sites.SiteEntityList)
  })
_sym_db.RegisterMessage(SiteEntityList)


# @@protoc_insertion_point(module_scope)
