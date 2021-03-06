# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IsomDeviceMgmt.proto

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
  name='IsomDeviceMgmt.proto',
  package='Honeywell.Security.ISOM.DeviceMgmt',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x14IsomDeviceMgmt.proto\x12\"Honeywell.Security.ISOM.DeviceMgmt\x1a\x10IsomStdDef.proto\":\n\x0f\x44iscoveryConfig\x12\x0b\n\x03ids\x18\x0b \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x0c \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xba\x02\n\x12IpInterfaceAddress\x12@\n\tipVersion\x18\x0b \x01(\x0e\x32-.Honeywell.Security.ISOM.DeviceMgmt.IpVersion\x12L\n\x0e\x61\x64\x64ressingType\x18\x0c \x01(\x0e\x32\x34.Honeywell.Security.ISOM.DeviceMgmt.IpAddressingType\x12\x11\n\tipAddress\x18\r \x01(\t\x12\x0e\n\x06ipMask\x18\x0e \x01(\t\x12\x16\n\x0e\x64\x65\x66\x61ultGateway\x18\x0f \x01(\t\x12\x12\n\nprimaryDns\x18\x10 \x01(\t\x12\x14\n\x0csecondaryDns\x18\x11 \x01(\t\x12\x13\n\x0bipv6Address\x18\x12 \x01(\t\x12\x10\n\x08ipv6Mask\x18\x13 \x01(\t*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"w\n\x16IpInterfaceAddressList\x12S\n\x13ipInterfaceAddesses\x18\x0b \x03(\x0b\x32\x36.Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"\xb5\x01\n\x14IpV6InterfaceAddress\x12\x11\n\tipAddress\x18\x0b \x01(\t\x12L\n\x0e\x61\x64\x64ressingType\x18\x0c \x01(\x0e\x32\x34.Honeywell.Security.ISOM.DeviceMgmt.IpAddressingType\x12\x16\n\x0e\x64\x65\x66\x61ultGateway\x18\r \x01(\t\x12\x1a\n\x12subnetPrefixLength\x18\x0e \x01(\x04*\x08\x08\xc0\x84=\x10\xe0\x91\x43\"}\n\x18IpV6InterfaceAddressList\x12W\n\x15ipv6InterfaceAddesses\x18\x0b \x03(\x0b\x32\x38.Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress*\x08\x08\xc0\x84=\x10\xe0\x91\x43*F\n\x10IpAddressingType\x12\n\n\x06Static\x10\x0b\x12\x08\n\x04\x44HCP\x10\x0c\x12\x1c\n\x14Max_IpAddressingType\x10\x80\x80\x80\x80\x04*<\n\tIpVersion\x12\x06\n\x02V4\x10\x0b\x12\x06\n\x02V6\x10\x0c\x12\x08\n\x04\x44ual\x10\r\x12\x15\n\rMax_IpVersion\x10\x80\x80\x80\x80\x04')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,])

_IPADDRESSINGTYPE = _descriptor.EnumDescriptor(
  name='IpAddressingType',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.IpAddressingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Static', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DHCP', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_IpAddressingType', index=2, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=887,
  serialized_end=957,
)
_sym_db.RegisterEnumDescriptor(_IPADDRESSINGTYPE)

IpAddressingType = enum_type_wrapper.EnumTypeWrapper(_IPADDRESSINGTYPE)
_IPVERSION = _descriptor.EnumDescriptor(
  name='IpVersion',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.IpVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='V4', index=0, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V6', index=1, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Dual', index=2, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Max_IpVersion', index=3, number=1073741824,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=959,
  serialized_end=1019,
)
_sym_db.RegisterEnumDescriptor(_IPVERSION)

IpVersion = enum_type_wrapper.EnumTypeWrapper(_IPVERSION)
Static = 11
DHCP = 12
Max_IpAddressingType = 1073741824
V4 = 11
V6 = 12
Dual = 13
Max_IpVersion = 1073741824



_DISCOVERYCONFIG = _descriptor.Descriptor(
  name='DiscoveryConfig',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.DiscoveryConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='Honeywell.Security.ISOM.DeviceMgmt.DiscoveryConfig.ids', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='Honeywell.Security.ISOM.DeviceMgmt.DiscoveryConfig.deviceId', index=1,
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
  serialized_start=78,
  serialized_end=136,
)


_IPINTERFACEADDRESS = _descriptor.Descriptor(
  name='IpInterfaceAddress',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipVersion', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.ipVersion', index=0,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addressingType', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.addressingType', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipAddress', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.ipAddress', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipMask', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.ipMask', index=3,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultGateway', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.defaultGateway', index=4,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primaryDns', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.primaryDns', index=5,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondaryDns', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.secondaryDns', index=6,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6Address', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.ipv6Address', index=7,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ipv6Mask', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress.ipv6Mask', index=8,
      number=19, type=9, cpp_type=9, label=1,
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
  serialized_start=139,
  serialized_end=453,
)


_IPINTERFACEADDRESSLIST = _descriptor.Descriptor(
  name='IpInterfaceAddressList',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddressList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipInterfaceAddesses', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddressList.ipInterfaceAddesses', index=0,
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
  serialized_start=455,
  serialized_end=574,
)


_IPV6INTERFACEADDRESS = _descriptor.Descriptor(
  name='IpV6InterfaceAddress',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipAddress', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress.ipAddress', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addressingType', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress.addressingType', index=1,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=11,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defaultGateway', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress.defaultGateway', index=2,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subnetPrefixLength', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress.subnetPrefixLength', index=3,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=577,
  serialized_end=758,
)


_IPV6INTERFACEADDRESSLIST = _descriptor.Descriptor(
  name='IpV6InterfaceAddressList',
  full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddressList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ipv6InterfaceAddesses', full_name='Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddressList.ipv6InterfaceAddesses', index=0,
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
  serialized_start=760,
  serialized_end=885,
)

_IPINTERFACEADDRESS.fields_by_name['ipVersion'].enum_type = _IPVERSION
_IPINTERFACEADDRESS.fields_by_name['addressingType'].enum_type = _IPADDRESSINGTYPE
_IPINTERFACEADDRESSLIST.fields_by_name['ipInterfaceAddesses'].message_type = _IPINTERFACEADDRESS
_IPV6INTERFACEADDRESS.fields_by_name['addressingType'].enum_type = _IPADDRESSINGTYPE
_IPV6INTERFACEADDRESSLIST.fields_by_name['ipv6InterfaceAddesses'].message_type = _IPV6INTERFACEADDRESS
DESCRIPTOR.message_types_by_name['DiscoveryConfig'] = _DISCOVERYCONFIG
DESCRIPTOR.message_types_by_name['IpInterfaceAddress'] = _IPINTERFACEADDRESS
DESCRIPTOR.message_types_by_name['IpInterfaceAddressList'] = _IPINTERFACEADDRESSLIST
DESCRIPTOR.message_types_by_name['IpV6InterfaceAddress'] = _IPV6INTERFACEADDRESS
DESCRIPTOR.message_types_by_name['IpV6InterfaceAddressList'] = _IPV6INTERFACEADDRESSLIST
DESCRIPTOR.enum_types_by_name['IpAddressingType'] = _IPADDRESSINGTYPE
DESCRIPTOR.enum_types_by_name['IpVersion'] = _IPVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DiscoveryConfig = _reflection.GeneratedProtocolMessageType('DiscoveryConfig', (_message.Message,), {
  'DESCRIPTOR' : _DISCOVERYCONFIG,
  '__module__' : 'IsomDeviceMgmt_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DeviceMgmt.DiscoveryConfig)
  })
_sym_db.RegisterMessage(DiscoveryConfig)

IpInterfaceAddress = _reflection.GeneratedProtocolMessageType('IpInterfaceAddress', (_message.Message,), {
  'DESCRIPTOR' : _IPINTERFACEADDRESS,
  '__module__' : 'IsomDeviceMgmt_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddress)
  })
_sym_db.RegisterMessage(IpInterfaceAddress)

IpInterfaceAddressList = _reflection.GeneratedProtocolMessageType('IpInterfaceAddressList', (_message.Message,), {
  'DESCRIPTOR' : _IPINTERFACEADDRESSLIST,
  '__module__' : 'IsomDeviceMgmt_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DeviceMgmt.IpInterfaceAddressList)
  })
_sym_db.RegisterMessage(IpInterfaceAddressList)

IpV6InterfaceAddress = _reflection.GeneratedProtocolMessageType('IpV6InterfaceAddress', (_message.Message,), {
  'DESCRIPTOR' : _IPV6INTERFACEADDRESS,
  '__module__' : 'IsomDeviceMgmt_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddress)
  })
_sym_db.RegisterMessage(IpV6InterfaceAddress)

IpV6InterfaceAddressList = _reflection.GeneratedProtocolMessageType('IpV6InterfaceAddressList', (_message.Message,), {
  'DESCRIPTOR' : _IPV6INTERFACEADDRESSLIST,
  '__module__' : 'IsomDeviceMgmt_pb2'
  # @@protoc_insertion_point(class_scope:Honeywell.Security.ISOM.DeviceMgmt.IpV6InterfaceAddressList)
  })
_sym_db.RegisterMessage(IpV6InterfaceAddressList)


# @@protoc_insertion_point(module_scope)
