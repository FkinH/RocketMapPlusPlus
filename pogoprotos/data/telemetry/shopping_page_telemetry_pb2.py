# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/shopping_page_telemetry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import telemetry_ids_pb2 as pogoprotos_dot_enums_dot_telemetry__ids__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/shopping_page_telemetry.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7pogoprotos/data/telemetry/shopping_page_telemetry.proto\x12\x19pogoprotos.data.telemetry\x1a$pogoprotos/enums/telemetry_ids.proto\"c\n\x15ShoppingPageTelemetry\x12J\n\x16shopping_page_click_id\x18\x01 \x01(\x0e\x32*.pogoprotos.enums.ShoppingPageTelemetryIdsb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_telemetry__ids__pb2.DESCRIPTOR,])




_SHOPPINGPAGETELEMETRY = _descriptor.Descriptor(
  name='ShoppingPageTelemetry',
  full_name='pogoprotos.data.telemetry.ShoppingPageTelemetry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shopping_page_click_id', full_name='pogoprotos.data.telemetry.ShoppingPageTelemetry.shopping_page_click_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=223,
)

_SHOPPINGPAGETELEMETRY.fields_by_name['shopping_page_click_id'].enum_type = pogoprotos_dot_enums_dot_telemetry__ids__pb2._SHOPPINGPAGETELEMETRYIDS
DESCRIPTOR.message_types_by_name['ShoppingPageTelemetry'] = _SHOPPINGPAGETELEMETRY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ShoppingPageTelemetry = _reflection.GeneratedProtocolMessageType('ShoppingPageTelemetry', (_message.Message,), dict(
  DESCRIPTOR = _SHOPPINGPAGETELEMETRY,
  __module__ = 'pogoprotos.data.telemetry.shopping_page_telemetry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.ShoppingPageTelemetry)
  ))
_sym_db.RegisterMessage(ShoppingPageTelemetry)


# @@protoc_insertion_point(module_scope)
