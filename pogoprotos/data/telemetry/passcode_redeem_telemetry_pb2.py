# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/passcode_redeem_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/passcode_redeem_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/data/telemetry/passcode_redeem_telemetry.proto\x12\x19pogoprotos.data.telemetry\"\x80\x01\n\x17PasscodeRedeemTelemetry\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x10\n\x08passcode\x18\x02 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x03 \x01(\t\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12\x16\n\x0e\x62undle_version\x18\x05 \x01(\tb\x06proto3')
)




_PASSCODEREDEEMTELEMETRY = _descriptor.Descriptor(
  name='PasscodeRedeemTelemetry',
  full_name='pogoprotos.data.telemetry.PasscodeRedeemTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.telemetry.PasscodeRedeemTelemetry.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passcode', full_name='pogoprotos.data.telemetry.PasscodeRedeemTelemetry.passcode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='pogoprotos.data.telemetry.PasscodeRedeemTelemetry.country_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='pogoprotos.data.telemetry.PasscodeRedeemTelemetry.language_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle_version', full_name='pogoprotos.data.telemetry.PasscodeRedeemTelemetry.bundle_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['PasscodeRedeemTelemetry'] = _PASSCODEREDEEMTELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PasscodeRedeemTelemetry = _reflection.GeneratedProtocolMessageType('PasscodeRedeemTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _PASSCODEREDEEMTELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.passcode_redeem_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.PasscodeRedeemTelemetry)
  ))
_sym_db.RegisterMessage(PasscodeRedeemTelemetry)


# @@protoc_insertion_point(module_scope)
