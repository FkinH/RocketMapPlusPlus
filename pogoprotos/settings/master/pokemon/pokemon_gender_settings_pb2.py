# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon/pokemon_gender_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon/pokemon_gender_settings.proto',
  package='pogoprotos.settings.master.pokemon',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@pogoprotos/settings/master/pokemon/pokemon_gender_settings.proto\x12\"pogoprotos.settings.master.pokemon\"a\n\x15PokemonGenderSettings\x12\x14\n\x0cmale_percent\x18\x01 \x01(\x02\x12\x16\n\x0e\x66\x65male_percent\x18\x02 \x01(\x02\x12\x1a\n\x12genderless_percent\x18\x03 \x01(\x02\x62\x06proto3')
)




_POKEMONGENDERSETTINGS = _descriptor.Descriptor(
  name='PokemonGenderSettings',
  full_name='pogoprotos.settings.master.pokemon.PokemonGenderSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='male_percent', full_name='pogoprotos.settings.master.pokemon.PokemonGenderSettings.male_percent', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='female_percent', full_name='pogoprotos.settings.master.pokemon.PokemonGenderSettings.female_percent', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genderless_percent', full_name='pogoprotos.settings.master.pokemon.PokemonGenderSettings.genderless_percent', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=104,
  serialized_end=201,
)

DESCRIPTOR.message_types_by_name['PokemonGenderSettings'] = _POKEMONGENDERSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonGenderSettings = _reflection.GeneratedProtocolMessageType('PokemonGenderSettings', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONGENDERSETTINGS,
  __module__ = 'pogoprotos.settings.master.pokemon.pokemon_gender_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.pokemon.PokemonGenderSettings)
  ))
_sym_db.RegisterMessage(PokemonGenderSettings)


# @@protoc_insertion_point(module_scope)
