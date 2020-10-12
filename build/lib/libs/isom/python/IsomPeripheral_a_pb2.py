# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IsomPeripheral_a.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import IsomStdDef_pb2 as IsomStdDef__pb2
import IsomPeripheral_pb2 as IsomPeripheral__pb2
import BatteryPeripheral_pb2 as BatteryPeripheral__pb2
import PowerPeripheral_pb2 as PowerPeripheral__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='IsomPeripheral_a.proto',
  package='Honeywell.Security.ISOM.Peripheral',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x16IsomPeripheral_a.proto\x12\"Honeywell.Security.ISOM.Peripheral\x1a\x10IsomStdDef.proto\x1a\x14IsomPeripheral.proto\x1a\x17\x42\x61tteryPeripheral.proto\x1a\x15PowerPeripheral.proto:\xa0\x01\n\x1bisomBatteryPeripheralConfig\x12\x34.Honeywell.Security.ISOM.Peripheral.PeripheralConfig\x18\x81\xea\x30 \x01(\x0b\x32\x43.Honeywell.Security.ISOM.BatteryPeripherals.BatteryPeripheralConfig:\x9d\x01\n\x1aisomBatteryPeripheralState\x12\x33.Honeywell.Security.ISOM.Peripheral.PeripheralState\x18\x81\xea\x30 \x01(\x0b\x32\x42.Honeywell.Security.ISOM.BatteryPeripherals.BatteryPeripheralState:\x97\x01\n\x18isomPowerPeripheralState\x12\x33.Honeywell.Security.ISOM.Peripheral.PeripheralState\x18\x82\xea\x30 \x01(\x0b\x32>.Honeywell.Security.ISOM.PowerPeripherals.PowerPeripheralState')
  ,
  dependencies=[IsomStdDef__pb2.DESCRIPTOR,IsomPeripheral__pb2.DESCRIPTOR,BatteryPeripheral__pb2.DESCRIPTOR,PowerPeripheral__pb2.DESCRIPTOR,])


ISOMBATTERYPERIPHERALCONFIG_FIELD_NUMBER = 800001
isomBatteryPeripheralConfig = _descriptor.FieldDescriptor(
  name='isomBatteryPeripheralConfig', full_name='Honeywell.Security.ISOM.Peripheral.isomBatteryPeripheralConfig', index=0,
  number=800001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ISOMBATTERYPERIPHERALSTATE_FIELD_NUMBER = 800001
isomBatteryPeripheralState = _descriptor.FieldDescriptor(
  name='isomBatteryPeripheralState', full_name='Honeywell.Security.ISOM.Peripheral.isomBatteryPeripheralState', index=1,
  number=800001, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
ISOMPOWERPERIPHERALSTATE_FIELD_NUMBER = 800002
isomPowerPeripheralState = _descriptor.FieldDescriptor(
  name='isomPowerPeripheralState', full_name='Honeywell.Security.ISOM.Peripheral.isomPowerPeripheralState', index=2,
  number=800002, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['isomBatteryPeripheralConfig'] = isomBatteryPeripheralConfig
DESCRIPTOR.extensions_by_name['isomBatteryPeripheralState'] = isomBatteryPeripheralState
DESCRIPTOR.extensions_by_name['isomPowerPeripheralState'] = isomPowerPeripheralState
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

isomBatteryPeripheralConfig.message_type = BatteryPeripheral__pb2._BATTERYPERIPHERALCONFIG
IsomPeripheral__pb2.PeripheralConfig.RegisterExtension(isomBatteryPeripheralConfig)
isomBatteryPeripheralState.message_type = BatteryPeripheral__pb2._BATTERYPERIPHERALSTATE
IsomPeripheral__pb2.PeripheralState.RegisterExtension(isomBatteryPeripheralState)
isomPowerPeripheralState.message_type = PowerPeripheral__pb2._POWERPERIPHERALSTATE
IsomPeripheral__pb2.PeripheralState.RegisterExtension(isomPowerPeripheralState)

# @@protoc_insertion_point(module_scope)
