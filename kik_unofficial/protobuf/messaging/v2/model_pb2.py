# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messaging/v2/model.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import protobuf_validation_pb2 as protobuf__validation__pb2
import kik_unofficial.protobuf.common.v2_pb2 as model
import kik_unofficial.protobuf.chats.v2_pb2 as chats_common

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messaging.v2.model_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.kik.gen.messaging.v2ZRgithub.com/kikinteractive/xiphias-model-common/generated/go/messaging/v2;messaging\242\002\024KPBCommonMessagingV2'
  _MESSAGE.fields_by_name['chat_id']._options = None
  _MESSAGE.fields_by_name['chat_id']._serialized_options = b'\312\235%\002\010\001'
  _MESSAGE.fields_by_name['sender']._options = None
  _MESSAGE.fields_by_name['sender']._serialized_options = b'\312\235%\002\010\001'
  _MESSAGE.fields_by_name['client_sent']._options = None
  _MESSAGE.fields_by_name['client_sent']._serialized_options = b'\312\235%\002\010\001'
  _CHATUPDATE_TEXTPREVIEW.fields_by_name['preview_text']._options = None
  _CHATUPDATE_TEXTPREVIEW.fields_by_name['preview_text']._serialized_options = b'\312\235%\005\010\0010\200\010'
  _CHATUPDATE.fields_by_name['chat_id']._options = None
  _CHATUPDATE.fields_by_name['chat_id']._serialized_options = b'\312\235%\002\010\001'
  _CHAT._serialized_start=188
  _CHAT._serialized_end=449
  _MESSAGE._serialized_start=452
  _MESSAGE._serialized_end=692
  _MESSAGE_ID._serialized_start=669
  _MESSAGE_ID._serialized_end=692
  _POINTER._serialized_start=695
  _POINTER._serialized_end=926
  _POINTER_TYPE._serialized_start=883
  _POINTER_TYPE._serialized_end=926
  _CHATUPDATE._serialized_start=929
  _CHATUPDATE._serialized_end=1566
  _CHATUPDATE_TEXTPREVIEW._serialized_start=1351
  _CHATUPDATE_TEXTPREVIEW._serialized_end=1397
  _CHATUPDATE_IMAGEPREVIEW._serialized_start=1399
  _CHATUPDATE_IMAGEPREVIEW._serialized_end=1413
  _CHATUPDATE_NAMEUPDATE._serialized_start=1415
  _CHATUPDATE_NAMEUPDATE._serialized_end=1441
  _CHATUPDATE_PROFILEPICUPDATE._serialized_start=1443
  _CHATUPDATE_PROFILEPICUPDATE._serialized_end=1486
  _CHATUPDATE_PARTICIPANTSUPDATE._serialized_start=1488
  _CHATUPDATE_PARTICIPANTSUPDATE._serialized_end=1555
# @@protoc_insertion_point(module_scope)
