# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/user_messages.proto
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
from syft.proto.lib.python import dict_pb2 as proto_dot_lib_dot_python_dot_dict__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\'proto/grid/messages/user_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\x1a\x1bproto/lib/python/dict.proto"\x8f\x02\n\x11\x43reateUserMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07website\x18\t \x01(\t\x12\x13\n\x0binstitution\x18\n \x01(\t\x12\x0f\n\x07\x64\x61\x61_pdf\x18\x0b \x01(\x0c\x12\'\n\x08reply_to\x18\x0c \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0e\n\x06\x62udget\x18\r \x01(\x01"\x99\x01\n\x0eGetUserMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\xbb\x01\n\x1bProcessUserCandidateMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x14\n\x0c\x63\x61ndidate_id\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\t\x12&\n\x07\x61\x64\x64ress\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address"\x88\x01\n\x0fGetUserResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x15.syft.lib.python.Dict\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address"\x8e\x01\n\x14GetCandidatesMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x8e\x01\n\x15GetCandidatesResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x63ontent\x18\x02 \x03(\x0b\x32\x15.syft.lib.python.Dict\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address"\x89\x01\n\x0fGetUsersMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x89\x01\n\x10GetUsersResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x63ontent\x18\x02 \x03(\x0b\x32\x15.syft.lib.python.Dict\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address"\x9c\x01\n\x11\x44\x65leteUserMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"\x9f\x02\n\x11UpdateUserMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x0e\n\x06groups\x18\x07 \x01(\t\x12\x0c\n\x04name\x18\x08 \x01(\t\x12\x0e\n\x06\x62udget\x18\t \x01(\x01\x12\x13\n\x0binstitution\x18\n \x01(\t\x12\x0f\n\x07website\x18\x0b \x01(\t\x12\'\n\x08reply_to\x18\x0c \x01(\x0b\x32\x15.syft.core.io.Address"\xc7\x01\n\x12SearchUsersMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\t\x12\x0e\n\x06groups\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\'\n\x08reply_to\x18\x07 \x01(\x0b\x32\x15.syft.core.io.Address"\x8c\x01\n\x13SearchUsersResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x63ontent\x18\x02 \x03(\x0b\x32\x15.syft.lib.python.Dict\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3'
)


_CREATEUSERMESSAGE = DESCRIPTOR.message_types_by_name["CreateUserMessage"]
_GETUSERMESSAGE = DESCRIPTOR.message_types_by_name["GetUserMessage"]
_PROCESSUSERCANDIDATEMESSAGE = DESCRIPTOR.message_types_by_name[
    "ProcessUserCandidateMessage"
]
_GETUSERRESPONSE = DESCRIPTOR.message_types_by_name["GetUserResponse"]
_GETCANDIDATESMESSAGE = DESCRIPTOR.message_types_by_name["GetCandidatesMessage"]
_GETCANDIDATESRESPONSE = DESCRIPTOR.message_types_by_name["GetCandidatesResponse"]
_GETUSERSMESSAGE = DESCRIPTOR.message_types_by_name["GetUsersMessage"]
_GETUSERSRESPONSE = DESCRIPTOR.message_types_by_name["GetUsersResponse"]
_DELETEUSERMESSAGE = DESCRIPTOR.message_types_by_name["DeleteUserMessage"]
_UPDATEUSERMESSAGE = DESCRIPTOR.message_types_by_name["UpdateUserMessage"]
_SEARCHUSERSMESSAGE = DESCRIPTOR.message_types_by_name["SearchUsersMessage"]
_SEARCHUSERSRESPONSE = DESCRIPTOR.message_types_by_name["SearchUsersResponse"]
CreateUserMessage = _reflection.GeneratedProtocolMessageType(
    "CreateUserMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEUSERMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateUserMessage)
    },
)
_sym_db.RegisterMessage(CreateUserMessage)

GetUserMessage = _reflection.GeneratedProtocolMessageType(
    "GetUserMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetUserMessage)
    },
)
_sym_db.RegisterMessage(GetUserMessage)

ProcessUserCandidateMessage = _reflection.GeneratedProtocolMessageType(
    "ProcessUserCandidateMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROCESSUSERCANDIDATEMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.ProcessUserCandidateMessage)
    },
)
_sym_db.RegisterMessage(ProcessUserCandidateMessage)

GetUserResponse = _reflection.GeneratedProtocolMessageType(
    "GetUserResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERRESPONSE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetUserResponse)
    },
)
_sym_db.RegisterMessage(GetUserResponse)

GetCandidatesMessage = _reflection.GeneratedProtocolMessageType(
    "GetCandidatesMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCANDIDATESMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetCandidatesMessage)
    },
)
_sym_db.RegisterMessage(GetCandidatesMessage)

GetCandidatesResponse = _reflection.GeneratedProtocolMessageType(
    "GetCandidatesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCANDIDATESRESPONSE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetCandidatesResponse)
    },
)
_sym_db.RegisterMessage(GetCandidatesResponse)

GetUsersMessage = _reflection.GeneratedProtocolMessageType(
    "GetUsersMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERSMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetUsersMessage)
    },
)
_sym_db.RegisterMessage(GetUsersMessage)

GetUsersResponse = _reflection.GeneratedProtocolMessageType(
    "GetUsersResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERSRESPONSE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.GetUsersResponse)
    },
)
_sym_db.RegisterMessage(GetUsersResponse)

DeleteUserMessage = _reflection.GeneratedProtocolMessageType(
    "DeleteUserMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEUSERMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.DeleteUserMessage)
    },
)
_sym_db.RegisterMessage(DeleteUserMessage)

UpdateUserMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateUserMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEUSERMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateUserMessage)
    },
)
_sym_db.RegisterMessage(UpdateUserMessage)

SearchUsersMessage = _reflection.GeneratedProtocolMessageType(
    "SearchUsersMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHUSERSMESSAGE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SearchUsersMessage)
    },
)
_sym_db.RegisterMessage(SearchUsersMessage)

SearchUsersResponse = _reflection.GeneratedProtocolMessageType(
    "SearchUsersResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHUSERSRESPONSE,
        "__module__": "proto.grid.messages.user_messages_pb2"
        # @@protoc_insertion_point(class_scope:syft.grid.messages.SearchUsersResponse)
    },
)
_sym_db.RegisterMessage(SearchUsersResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _CREATEUSERMESSAGE._serialized_start = 161
    _CREATEUSERMESSAGE._serialized_end = 432
    _GETUSERMESSAGE._serialized_start = 435
    _GETUSERMESSAGE._serialized_end = 588
    _PROCESSUSERCANDIDATEMESSAGE._serialized_start = 591
    _PROCESSUSERCANDIDATEMESSAGE._serialized_end = 778
    _GETUSERRESPONSE._serialized_start = 781
    _GETUSERRESPONSE._serialized_end = 917
    _GETCANDIDATESMESSAGE._serialized_start = 920
    _GETCANDIDATESMESSAGE._serialized_end = 1062
    _GETCANDIDATESRESPONSE._serialized_start = 1065
    _GETCANDIDATESRESPONSE._serialized_end = 1207
    _GETUSERSMESSAGE._serialized_start = 1210
    _GETUSERSMESSAGE._serialized_end = 1347
    _GETUSERSRESPONSE._serialized_start = 1350
    _GETUSERSRESPONSE._serialized_end = 1487
    _DELETEUSERMESSAGE._serialized_start = 1490
    _DELETEUSERMESSAGE._serialized_end = 1646
    _UPDATEUSERMESSAGE._serialized_start = 1649
    _UPDATEUSERMESSAGE._serialized_end = 1936
    _SEARCHUSERSMESSAGE._serialized_start = 1939
    _SEARCHUSERSMESSAGE._serialized_end = 2138
    _SEARCHUSERSRESPONSE._serialized_start = 2141
    _SEARCHUSERSRESPONSE._serialized_end = 2281
# @@protoc_insertion_point(module_scope)
