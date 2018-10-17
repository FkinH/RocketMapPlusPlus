# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/ditto/location_update_event_params.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/platform/ditto/location_update_event_params.proto',
  package='pogoprotos.networking.platform.ditto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGpogoprotos/networking/platform/ditto/location_update_event_params.proto\x12$pogoprotos.networking.platform.ditto\"\xb5\x01\n\x19LocationUpdateEventParams\x12\x14\n\x0clatitude_deg\x18\x01 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x02 \x01(\x01\x12\x12\n\naltitude_m\x18\x03 \x01(\x01\x12\x12\n\naccuracy_m\x18\x04 \x01(\x01\x12\x13\n\x0btimestamp_s\x18\x05 \x01(\x01\x12\x17\n\x0fprovider_status\x18\x06 \x01(\r\x12\x15\n\rlocation_type\x18\x07 \x01(\rb\x06proto3')
)




_LOCATIONUPDATEEVENTPARAMS = _descriptor.Descriptor(
  name='LocationUpdateEventParams',
  full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude_deg', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.latitude_deg', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude_deg', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.longitude_deg', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude_m', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.altitude_m', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy_m', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.accuracy_m', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_s', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.timestamp_s', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider_status', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.provider_status', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_type', full_name='pogoprotos.networking.platform.ditto.LocationUpdateEventParams.location_type', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=114,
  serialized_end=295,
)

DESCRIPTOR.message_types_by_name['LocationUpdateEventParams'] = _LOCATIONUPDATEEVENTPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationUpdateEventParams = _reflection.GeneratedProtocolMessageType('LocationUpdateEventParams', (_message.Message,), dict(
  DESCRIPTOR = _LOCATIONUPDATEEVENTPARAMS,
  __module__ = 'pogoprotos.networking.platform.ditto.location_update_event_params_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.ditto.LocationUpdateEventParams)
  ))
_sym_db.RegisterMessage(LocationUpdateEventParams)


# @@protoc_insertion_point(module_scope)
