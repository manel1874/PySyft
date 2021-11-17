# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/domain/service/request_message.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n4proto/core/node/domain/service/request_message.proto\x12\x1dsyft.core.node.domain.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\xbd\x02\n\x0eRequestMessage\x12)\n\nrequest_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12(\n\tobject_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bobject_tags\x18\x03 \x03(\t\x12\x1b\n\x13request_description\x18\x04 \x01(\t\x12-\n\x0etarget_address\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address\x12,\n\rowner_address\x18\x06 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x1c\n\x14requester_verify_key\x18\x07 \x01(\x0c\x12\x14\n\x0ctimeout_secs\x18\x08 \x01(\x05\x12\x13\n\x0bobject_type\x18\t \x01(\tb\x06proto3'
)


_REQUESTMESSAGE = DESCRIPTOR.message_types_by_name["RequestMessage"]
RequestMessage = _reflection.GeneratedProtocolMessageType(
    "RequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTMESSAGE,
        "__module__": "proto.core.node.domain.service.request_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.RequestMessage)
    },
)
_sym_db.RegisterMessage(RequestMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _REQUESTMESSAGE._serialized_start = 156
    _REQUESTMESSAGE._serialized_end = 473
# @@protoc_insertion_point(module_scope)
