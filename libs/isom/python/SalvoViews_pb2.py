# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SalvoViews.proto

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
  name='SalvoViews.proto',
  package='Honeywell.Security.ISOM.SalvoViews',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10SalvoViews.proto\x12\"Honeywell.Security.ISOM.SalvoViews\x1a\x10IsomStdDef.proto\"a\n\x13SalvoViewOperations\x12@\n\tresources\x18\x0b \x03(\x0e\x32-.Honeywell.Security.ISOM.SalvoViews.Resources*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"i\n\x1bSalvoViewSupportedRelations\x12@\n\trelations\x18\x0b \x03(\x0e\x32-.Honeywell.Security.ISOM.SalvoViews.Relations*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"W\n\x0fSalvoViewEvents\x12:\n\x06\x65vents\x18\x0b \x03(\x0e\x32*.Honeywell.Security.ISOM.SalvoViews.Events*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"]\n\x14SalvoViewIdentifiers\x12\n\n\x02id\x18\x0b \x01(\t\x12\x0c\n\x04guid\x18\x0c \x01(\t\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"r\n\x18SalvoViewIdentifiersList\x12L\n\nidentifier\x18\x0b \x03(\x0b\x32\x38.Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"x\n\x11SalvoViewRelation\x12\n\n\x02id\x18\x0b \x01(\t\x12;\n\x04name\x18\x0c \x01(\x0e\x32-.Honeywell.Security.ISOM.SalvoViews.Relations\x12\x10\n\x08\x65ntityId\x18\x0e \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"k\n\x0eSalvoViewState\x12O\n\x0c\x64isplayState\x18\x0b \x01(\x0e\x32\x39.Honeywell.Security.ISOM.SalvoViews.SalvoViewDisplayState*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"a\n\x12SalvoViewStateList\x12\x41\n\x05state\x18\x0b \x03(\x0b\x32\x32.Honeywell.Security.ISOM.SalvoViews.SalvoViewState*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"<\n\nPaneSource\x12\x12\n\nentityType\x18\x0b \x01(\t\x12\x10\n\x08\x65ntityID\x18\x0c \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xb2\x01\n\nLayoutPane\x12\x14\n\x0clayoutPaneID\x18\x0b \x01(\r\x12\x39\n\x0elayoutPaneRect\x18\x0c \x01(\x0b\x32!.Honeywell.Security.ISOM.IsomRect\x12I\n\x11paneSourceDetails\x18\r \x03(\x0b\x32..Honeywell.Security.ISOM.SalvoViews.PaneSource*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xf8\x01\n\x0fSalvoViewConfig\x12M\n\x0bidentifiers\x18\x0b \x01(\x0b\x32\x38.Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers\x12G\n\x08relation\x18\x0c \x03(\x0b\x32\x35.Honeywell.Security.ISOM.SalvoViews.SalvoViewRelation\x12\x43\n\x0blayoutPanes\x18\r \x03(\x0b\x32..Honeywell.Security.ISOM.SalvoViews.LayoutPane*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"d\n\x13SalvoViewConfigList\x12\x43\n\x06\x63onfig\x18\x0b \x03(\x0b\x32\x33.Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xa3\x01\n\x0fSalvoViewEntity\x12\x43\n\x06\x63onfig\x18\x15 \x01(\x0b\x32\x33.Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig\x12\x41\n\x05state\x18\x1f \x01(\x0b\x32\x32.Honeywell.Security.ISOM.SalvoViews.SalvoViewState*\x08\x08\xa0\xf7\x36\x10\xe0\x91\x43\"d\n\x13SalvoViewEntityList\x12\x43\n\x06\x65ntity\x18\x0b \x03(\x0b\x32\x33.Honeywell.Security.ISOM.SalvoViews.SalvoViewEntity*\x08\x08\xc0\x84=\x10\xe0\x91\x43*\xe9\x01\n\tResources\x12\x18\n\x13supportedOperations\x10\xf2\x07\x12\x17\n\x12supportedRelations\x10\xf3\x07\x12\x14\n\x0fsupportedEvents\x10\xf4\x07\x12\x1a\n\x15supportedCapabilities\x10\xf5\x07\x12\x0f\n\nfullEntity\x10\xc2N\x12\t\n\x04info\x10\xc3N\x12\x0b\n\x06\x63onfig\x10\xd7N\x12\x10\n\x0bidentifiers\x10\xebN\x12\x0e\n\trelations\x10\xffN\x12\x15\n\x10supportedLayouts\x10\x88O\x12\x15\n\rMax_Resources\x10\x80\x80\x80\x80\x04*I\n\tRelations\x12%\n SalvoViewOwnedByCredentialHolder\x10\x9aN\x12\x15\n\rMax_Relations\x10\x80\x80\x80\x80\x04*G\n\x06\x45vents\x12\x11\n\x0c\x63onfig_p_add\x10\x9aN\x12\x14\n\x0f\x63onfig_p_modify\x10\x9bN\x12\x14\n\x0f\x63onfig_p_delete\x10\x9cN*U\n\x15SalvoViewDisplayState\x12\r\n\tDisplayed\x10\x0b\x12\n\n\x06Hidden\x10\x0c\x12!\n\x19Max_SalvoViewDisplayState\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_RESOURCES = _descriptor.EnumDescriptor(
  name='Resources',
  full_name='Honeywell.Security.ISOM.SalvoViews.Resources',
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
      name='supportedLayouts', index=9, number=10120,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Resources', index=10, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1775,
  serialized_end=2008,
)
_sym_db.RegisterEnumDescriptor(_RESOURCES)

Resources = enum_type_wrapper.EnumTypeWrapper(_RESOURCES)
_RELATIONS = _descriptor.EnumDescriptor(
  name='Relations',
  full_name='Honeywell.Security.ISOM.SalvoViews.Relations',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SalvoViewOwnedByCredentialHolder', index=0, number=10010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_Relations', index=1, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2010,
  serialized_end=2083,
)
_sym_db.RegisterEnumDescriptor(_RELATIONS)

Relations = enum_type_wrapper.EnumTypeWrapper(_RELATIONS)
_EVENTS = _descriptor.EnumDescriptor(
  name='Events',
  full_name='Honeywell.Security.ISOM.SalvoViews.Events',
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2085,
  serialized_end=2156,
)
_sym_db.RegisterEnumDescriptor(_EVENTS)

Events = enum_type_wrapper.EnumTypeWrapper(_EVENTS)
_SALVOVIEWDISPLAYSTATE = _descriptor.EnumDescriptor(
  name='SalvoViewDisplayState',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewDisplayState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Displayed', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Hidden', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_SalvoViewDisplayState', index=2, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2158,
  serialized_end=2243,
)
_sym_db.RegisterEnumDescriptor(_SALVOVIEWDISPLAYSTATE)

SalvoViewDisplayState = enum_type_wrapper.EnumTypeWrapper(_SALVOVIEWDISPLAYSTATE)
supportedOperations = 1010
supportedRelations = 1011
supportedEvents = 1012
supportedCapabilities = 1013
fullEntity = 10050
info = 10051
config = 10071
identifiers = 10091
relations = 10111
supportedLayouts = 10120
Max_Resources = 1073741824
SalvoViewOwnedByCredentialHolder = 10010
Max_Relations = 1073741824
config_p_add = 10010
config_p_modify = 10011
config_p_delete = 10012
Displayed = 11
Hidden = 12
Max_SalvoViewDisplayState = 1073741824



_SALVOVIEWOPERATIONS = _descriptor.Descriptor(
  name='SalvoViewOperations',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewOperations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewOperations.resources', index=0,
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
  serialized_start=74,
  serialized_end=171,
)


_SALVOVIEWSUPPORTEDRELATIONS = _descriptor.Descriptor(
  name='SalvoViewSupportedRelations',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewSupportedRelations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relations', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewSupportedRelations.relations', index=0,
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
  serialized_start=173,
  serialized_end=278,
)


_SALVOVIEWEVENTS = _descriptor.Descriptor(
  name='SalvoViewEvents',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEvents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEvents.events', index=0,
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
  serialized_start=280,
  serialized_end=367,
)


_SALVOVIEWIDENTIFIERS = _descriptor.Descriptor(
  name='SalvoViewIdentifiers',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guid', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers.guid', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers.name', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers.description', index=3,
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
  serialized_start=369,
  serialized_end=462,
)


_SALVOVIEWIDENTIFIERSLIST = _descriptor.Descriptor(
  name='SalvoViewIdentifiersList',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiersList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiersList.identifier', index=0,
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
  serialized_start=464,
  serialized_end=578,
)


_SALVOVIEWRELATION = _descriptor.Descriptor(
  name='SalvoViewRelation',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewRelation.id', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewRelation.name', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=10010,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityId', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewRelation.entityId', index=2,
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
  serialized_start=580,
  serialized_end=700,
)


_SALVOVIEWSTATE = _descriptor.Descriptor(
  name='SalvoViewState',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='displayState', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewState.displayState', index=0,
      number=11, type=14, cpp_type=8, label=1,
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
  serialized_start=702,
  serialized_end=809,
)


_SALVOVIEWSTATELIST = _descriptor.Descriptor(
  name='SalvoViewStateList',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewStateList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewStateList.state', index=0,
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
  serialized_start=811,
  serialized_end=908,
)


_PANESOURCE = _descriptor.Descriptor(
  name='PaneSource',
  full_name='Honeywell.Security.ISOM.SalvoViews.PaneSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entityType', full_name='Honeywell.Security.ISOM.SalvoViews.PaneSource.entityType', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityID', full_name='Honeywell.Security.ISOM.SalvoViews.PaneSource.entityID', index=1,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=910,
  serialized_end=970,
)


_LAYOUTPANE = _descriptor.Descriptor(
  name='LayoutPane',
  full_name='Honeywell.Security.ISOM.SalvoViews.LayoutPane',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='layoutPaneID', full_name='Honeywell.Security.ISOM.SalvoViews.LayoutPane.layoutPaneID', index=0,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layoutPaneRect', full_name='Honeywell.Security.ISOM.SalvoViews.LayoutPane.layoutPaneRect', index=1,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paneSourceDetails', full_name='Honeywell.Security.ISOM.SalvoViews.LayoutPane.paneSourceDetails', index=2,
      number=13, type=11, cpp_type=10, label=3,
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
  serialized_start=973,
  serialized_end=1151,
)


_SALVOVIEWCONFIG = _descriptor.Descriptor(
  name='SalvoViewConfig',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifiers', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig.identifiers', index=0,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relation', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig.relation', index=1,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='layoutPanes', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig.layoutPanes', index=2,
      number=13, type=11, cpp_type=10, label=3,
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
  serialized_start=1154,
  serialized_end=1402,
)


_SALVOVIEWCONFIGLIST = _descriptor.Descriptor(
  name='SalvoViewConfigList',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewConfigList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewConfigList.config', index=0,
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
  serialized_start=1404,
  serialized_end=1504,
)


_SALVOVIEWENTITY = _descriptor.Descriptor(
  name='SalvoViewEntity',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEntity.config', index=0,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEntity.state', index=1,
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
  serialized_start=1507,
  serialized_end=1670,
)


_SALVOVIEWENTITYLIST = _descriptor.Descriptor(
  name='SalvoViewEntityList',
  full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEntityList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity', full_name='Honeywell.Security.ISOM.SalvoViews.SalvoViewEntityList.entity', index=0,
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
  serialized_start=1672,
  serialized_end=1772,
)

_SALVOVIEWOPERATIONS.fields_by_name['resources'].enum_type = _RESOURCES
_SALVOVIEWSUPPORTEDRELATIONS.fields_by_name['relations'].enum_type = _RELATIONS
_SALVOVIEWEVENTS.fields_by_name['events'].enum_type = _EVENTS
_SALVOVIEWIDENTIFIERSLIST.fields_by_name['identifier'].message_type = _SALVOVIEWIDENTIFIERS
_SALVOVIEWRELATION.fields_by_name['name'].enum_type = _RELATIONS
_SALVOVIEWSTATE.fields_by_name['displayState'].enum_type = _SALVOVIEWDISPLAYSTATE
_SALVOVIEWSTATELIST.fields_by_name['state'].message_type = _SALVOVIEWSTATE
_LAYOUTPANE.fields_by_name['layoutPaneRect'].message_type = IsomStdDef__pb2._ISOMRECT
_LAYOUTPANE.fields_by_name['paneSourceDetails'].message_type = _PANESOURCE
_SALVOVIEWCONFIG.fields_by_name['identifiers'].message_type = _SALVOVIEWIDENTIFIERS
_SALVOVIEWCONFIG.fields_by_name['relation'].message_type = _SALVOVIEWRELATION
_SALVOVIEWCONFIG.fields_by_name['layoutPanes'].message_type = _LAYOUTPANE
_SALVOVIEWCONFIGLIST.fields_by_name['config'].message_type = _SALVOVIEWCONFIG
_SALVOVIEWENTITY.fields_by_name['config'].message_type = _SALVOVIEWCONFIG
_SALVOVIEWENTITY.fields_by_name['state'].message_type = _SALVOVIEWSTATE
_SALVOVIEWENTITYLIST.fields_by_name['entity'].message_type = _SALVOVIEWENTITY
DESCRIPTOR.message_types_by_name['SalvoViewOperations'] = _SALVOVIEWOPERATIONS
DESCRIPTOR.message_types_by_name['SalvoViewSupportedRelations'] = _SALVOVIEWSUPPORTEDRELATIONS
DESCRIPTOR.message_types_by_name['SalvoViewEvents'] = _SALVOVIEWEVENTS
DESCRIPTOR.message_types_by_name['SalvoViewIdentifiers'] = _SALVOVIEWIDENTIFIERS
DESCRIPTOR.message_types_by_name['SalvoViewIdentifiersList'] = _SALVOVIEWIDENTIFIERSLIST
DESCRIPTOR.message_types_by_name['SalvoViewRelation'] = _SALVOVIEWRELATION
DESCRIPTOR.message_types_by_name['SalvoViewState'] = _SALVOVIEWSTATE
DESCRIPTOR.message_types_by_name['SalvoViewStateList'] = _SALVOVIEWSTATELIST
DESCRIPTOR.message_types_by_name['PaneSource'] = _PANESOURCE
DESCRIPTOR.message_types_by_name['LayoutPane'] = _LAYOUTPANE
DESCRIPTOR.message_types_by_name['SalvoViewConfig'] = _SALVOVIEWCONFIG
DESCRIPTOR.message_types_by_name['SalvoViewConfigList'] = _SALVOVIEWCONFIGLIST
DESCRIPTOR.message_types_by_name['SalvoViewEntity'] = _SALVOVIEWENTITY
DESCRIPTOR.message_types_by_name['SalvoViewEntityList'] = _SALVOVIEWENTITYLIST
DESCRIPTOR.enum_types_by_name['Resources'] = _RESOURCES
DESCRIPTOR.enum_types_by_name['Relations'] = _RELATIONS
DESCRIPTOR.enum_types_by_name['Events'] = _EVENTS
DESCRIPTOR.enum_types_by_name['SalvoViewDisplayState'] = _SALVOVIEWDISPLAYSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SalvoViewOperations = _reflection.GeneratedProtocolMessageType('SalvoViewOperations', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWOPERATIONS,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewOperations)
  })
_sym_db.RegisterMessage(SalvoViewOperations)

SalvoViewSupportedRelations = _reflection.GeneratedProtocolMessageType('SalvoViewSupportedRelations', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWSUPPORTEDRELATIONS,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewSupportedRelations)
  })
_sym_db.RegisterMessage(SalvoViewSupportedRelations)

SalvoViewEvents = _reflection.GeneratedProtocolMessageType('SalvoViewEvents', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWEVENTS,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewEvents)
  })
_sym_db.RegisterMessage(SalvoViewEvents)

SalvoViewIdentifiers = _reflection.GeneratedProtocolMessageType('SalvoViewIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWIDENTIFIERS,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiers)
  })
_sym_db.RegisterMessage(SalvoViewIdentifiers)

SalvoViewIdentifiersList = _reflection.GeneratedProtocolMessageType('SalvoViewIdentifiersList', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWIDENTIFIERSLIST,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewIdentifiersList)
  })
_sym_db.RegisterMessage(SalvoViewIdentifiersList)

SalvoViewRelation = _reflection.GeneratedProtocolMessageType('SalvoViewRelation', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWRELATION,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewRelation)
  })
_sym_db.RegisterMessage(SalvoViewRelation)

SalvoViewState = _reflection.GeneratedProtocolMessageType('SalvoViewState', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWSTATE,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewState)
  })
_sym_db.RegisterMessage(SalvoViewState)

SalvoViewStateList = _reflection.GeneratedProtocolMessageType('SalvoViewStateList', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWSTATELIST,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewStateList)
  })
_sym_db.RegisterMessage(SalvoViewStateList)

PaneSource = _reflection.GeneratedProtocolMessageType('PaneSource', (_message.Message,), {
  'DESCRIPTOR' : _PANESOURCE,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.PaneSource)
  })
_sym_db.RegisterMessage(PaneSource)

LayoutPane = _reflection.GeneratedProtocolMessageType('LayoutPane', (_message.Message,), {
  'DESCRIPTOR' : _LAYOUTPANE,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.LayoutPane)
  })
_sym_db.RegisterMessage(LayoutPane)

SalvoViewConfig = _reflection.GeneratedProtocolMessageType('SalvoViewConfig', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWCONFIG,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewConfig)
  })
_sym_db.RegisterMessage(SalvoViewConfig)

SalvoViewConfigList = _reflection.GeneratedProtocolMessageType('SalvoViewConfigList', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWCONFIGLIST,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewConfigList)
  })
_sym_db.RegisterMessage(SalvoViewConfigList)

SalvoViewEntity = _reflection.GeneratedProtocolMessageType('SalvoViewEntity', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWENTITY,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewEntity)
  })
_sym_db.RegisterMessage(SalvoViewEntity)

SalvoViewEntityList = _reflection.GeneratedProtocolMessageType('SalvoViewEntityList', (_message.Message,), {
  'DESCRIPTOR' : _SALVOVIEWENTITYLIST,
  '__module__' : 'SalvoViews_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.SalvoViews.SalvoViewEntityList)
  })
_sym_db.RegisterMessage(SalvoViewEntityList)


# @@protoc_insertion_point(module_scope)
