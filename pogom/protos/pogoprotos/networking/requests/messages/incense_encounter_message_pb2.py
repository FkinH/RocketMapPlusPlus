# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/incense_encounter_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/incense_encounter_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGpogoprotos/networking/requests/messages/incense_encounter_message.proto\x12\'pogoprotos.networking.requests.messages\"K\n\x17IncenseEncounterMessage\x12\x14\n\x0c\x65ncounter_id\x18\x01 \x01(\x04\x12\x1a\n\x12\x65ncounter_location\x18\x02 \x01(\tb\x06proto3')
)




_INCENSEENCOUNTERMESSAGE = _descriptor.Descriptor(
  name='IncenseEncounterMessage',
  full_name='pogoprotos.networking.requests.messages.IncenseEncounterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.requests.messages.IncenseEncounterMessage.encounter_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encounter_location', full_name='pogoprotos.networking.requests.messages.IncenseEncounterMessage.encounter_location', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=116,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['IncenseEncounterMessage'] = _INCENSEENCOUNTERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncenseEncounterMessage = _reflection.GeneratedProtocolMessageType('IncenseEncounterMessage', (_message.Message,), dict(
  DESCRIPTOR = _INCENSEENCOUNTERMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.incense_encounter_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.IncenseEncounterMessage)
  ))
_sym_db.RegisterMessage(IncenseEncounterMessage)


# @@protoc_insertion_point(module_scope)
