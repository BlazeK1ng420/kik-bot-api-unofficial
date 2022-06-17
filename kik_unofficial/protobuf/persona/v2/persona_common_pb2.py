# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: persona/v2/persona_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import kik_unofficial.protobuf.protobuf_validation_pb2 as protobuf__validation__pb2
import kik_unofficial.protobuf.asset.v1_pb2 as asset_common


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpersona/v2/persona_common.proto\x12\x11\x63ommon.persona.v2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19protobuf_validation.proto\x1a\x1b\x61sset/v1/asset_common.proto\x1a\x15\x63ommon/v2/model.proto\"\xe0\x02\n\x0cPersonaShort\x12(\n\npersona_id\x18\x01 \x01(\x0b\x32\x14.common.v2.PersonaId\x12\x1b\n\x13signalling_disabled\x18\x02 \x01(\x08\x12-\n\x08username\x18\x03 \x01(\x0b\x32\x1b.common.persona.v2.Username\x12\x34\n\x0c\x64isplay_name\x18\x04 \x01(\x0b\x32\x1e.common.persona.v2.DisplayName\x12\x36\n\rdisplay_image\x18\x05 \x01(\x0b\x32\x1f.common.persona.v2.DisplayImage\x12\x34\n\x0c\x65moji_status\x18\x06 \x01(\x0b\x32\x1e.common.persona.v2.EmojiStatus\x12\x36\n\rbot_extension\x18\x07 \x01(\x0b\x32\x1f.common.persona.v2.BotExtension\"\xca\x02\n\x0bPersonaFull\x12.\n\x05short\x18\x01 \x01(\x0b\x32\x1f.common.persona.v2.PersonaShort\x12#\n\x03\x62io\x18\x02 \x01(\x0b\x32\x16.common.persona.v2.Bio\x12=\n\x14original_display_pic\x18\x03 \x01(\x0b\x32\x1f.common.persona.v2.DisplayImage\x12?\n\x16\x62\x61\x63kground_display_pic\x18\x04 \x01(\x0b\x32\x1f.common.persona.v2.DisplayImage\x12\x35\n\x0cregistration\x18\x05 \x01(\x0b\x32\x1f.common.persona.v2.Registration\x12/\n\tinterests\x18\x06 \x01(\x0b\x32\x1c.common.persona.v2.Interests\"%\n\x08Username\x12\x19\n\x08username\x18\x01 \x01(\tB\x07\xca\x9d%\x03\x30\x80\x08\",\n\x0b\x44isplayName\x12\x1d\n\x0c\x64isplay_name\x18\x01 \x01(\tB\x07\xca\x9d%\x03\x30\x80\x08\"\xae\x01\n\x0c\x44isplayImage\x12,\n\x05image\x18\x01 \x01(\x0b\x32\x1d.common.asset.v1.MediaContent\x12\x34\n\rimage_preview\x18\x02 \x01(\x0b\x32\x1d.common.asset.v1.MediaContent\x12:\n\x16last_updated_timestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\'\n\x0c\x42otExtension\x12\x17\n\x0fis_kin_verified\x18\x01 \x01(\x08\",\n\x0b\x45mojiStatus\x12\x1d\n\x0ckik_asset_id\x18\x01 \x01(\tB\x07\xca\x9d%\x03\x30\xf4\x03\"\x1b\n\x03\x42io\x12\x14\n\x03\x62io\x18\x01 \x01(\tB\x07\xca\x9d%\x03\x30\x88\'\"A\n\x0cRegistration\x12\x31\n\rcreation_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9c\x01\n\tInterests\x12\x45\n\tinterests\x18\x01 \x03(\x0b\x32).common.persona.v2.Interests.InterestItemB\x07\xca\x9d%\x03\x80\x01\x14\x1aH\n\x0cInterestItem\x12\x13\n\x02id\x18\x01 \x01(\tB\x07\xca\x9d%\x03\x30\x88\'\x12#\n\x12localized_verbiage\x18\x02 \x01(\tB\x07\xca\x9d%\x03\x30\x88\'B}\n\x16\x63om.kik.gen.persona.v2ZNgithub.com/kikinteractive/xiphias-model-common/generated/go/persona/v2;persona\xa2\x02\x12KPBCommonPersonaV2b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'persona.v2.persona_common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.kik.gen.persona.v2ZNgithub.com/kikinteractive/xiphias-model-common/generated/go/persona/v2;persona\242\002\022KPBCommonPersonaV2'
  _USERNAME.fields_by_name['username']._options = None
  _USERNAME.fields_by_name['username']._serialized_options = b'\312\235%\0030\200\010'
  _DISPLAYNAME.fields_by_name['display_name']._options = None
  _DISPLAYNAME.fields_by_name['display_name']._serialized_options = b'\312\235%\0030\200\010'
  _EMOJISTATUS.fields_by_name['kik_asset_id']._options = None
  _EMOJISTATUS.fields_by_name['kik_asset_id']._serialized_options = b'\312\235%\0030\364\003'
  _BIO.fields_by_name['bio']._options = None
  _BIO.fields_by_name['bio']._serialized_options = b'\312\235%\0030\210\''
  _INTERESTS_INTERESTITEM.fields_by_name['id']._options = None
  _INTERESTS_INTERESTITEM.fields_by_name['id']._serialized_options = b'\312\235%\0030\210\''
  _INTERESTS_INTERESTITEM.fields_by_name['localized_verbiage']._options = None
  _INTERESTS_INTERESTITEM.fields_by_name['localized_verbiage']._serialized_options = b'\312\235%\0030\210\''
  _INTERESTS.fields_by_name['interests']._options = None
  _INTERESTS.fields_by_name['interests']._serialized_options = b'\312\235%\003\200\001\024'
  _PERSONASHORT._serialized_start=167
  _PERSONASHORT._serialized_end=519
  _PERSONAFULL._serialized_start=522
  _PERSONAFULL._serialized_end=852
  _USERNAME._serialized_start=854
  _USERNAME._serialized_end=891
  _DISPLAYNAME._serialized_start=893
  _DISPLAYNAME._serialized_end=937
  _DISPLAYIMAGE._serialized_start=940
  _DISPLAYIMAGE._serialized_end=1114
  _BOTEXTENSION._serialized_start=1116
  _BOTEXTENSION._serialized_end=1155
  _EMOJISTATUS._serialized_start=1157
  _EMOJISTATUS._serialized_end=1201
  _BIO._serialized_start=1203
  _BIO._serialized_end=1230
  _REGISTRATION._serialized_start=1232
  _REGISTRATION._serialized_end=1297
  _INTERESTS._serialized_start=1300
  _INTERESTS._serialized_end=1456
  _INTERESTS_INTERESTITEM._serialized_start=1384
  _INTERESTS_INTERESTITEM._serialized_end=1456
# @@protoc_insertion_point(module_scope)
