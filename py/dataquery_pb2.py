# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataquery.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dataquery.proto',
  package='dataquery',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x64\x61taquery.proto\x12\tdataquery\"n\n\x0eGetDataRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nuser_token\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61ta_id\x18\x03 \x01(\t\x12\x11\n\tdata_type\x18\x04 \x01(\t\x12\x13\n\x0breturn_type\x18\x05 \x01(\r\">\n\x0fGetDataResponse\x12\x15\n\rresponse_code\x18\x01 \x01(\r\x12\x14\n\x0c\x64\x61ta_payload\x18\x02 \x01(\t\"Z\n\x0fMetadataRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nuser_token\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x61ta_id\x18\x03 \x01(\t\x12\x11\n\tdata_type\x18\x04 \x01(\t\"<\n\x10MetadataResponse\x12\x15\n\rresponse_code\x18\x01 \x01(\r\x12\x11\n\tmeta_data\x18\x02 \x03(\t2\x99\x01\n\tDataQuery\x12@\n\x07GetData\x12\x19.dataquery.GetDataRequest\x1a\x1a.dataquery.GetDataResponse\x12J\n\x0fInspectMetadata\x12\x1a.dataquery.MetadataRequest\x1a\x1b.dataquery.MetadataResponseb\x06proto3'
)




_GETDATAREQUEST = _descriptor.Descriptor(
  name='GetDataRequest',
  full_name='dataquery.GetDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='dataquery.GetDataRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_token', full_name='dataquery.GetDataRequest.user_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_id', full_name='dataquery.GetDataRequest.data_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='dataquery.GetDataRequest.data_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_type', full_name='dataquery.GetDataRequest.return_type', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=30,
  serialized_end=140,
)


_GETDATARESPONSE = _descriptor.Descriptor(
  name='GetDataResponse',
  full_name='dataquery.GetDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_code', full_name='dataquery.GetDataResponse.response_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_payload', full_name='dataquery.GetDataResponse.data_payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=142,
  serialized_end=204,
)


_METADATAREQUEST = _descriptor.Descriptor(
  name='MetadataRequest',
  full_name='dataquery.MetadataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='dataquery.MetadataRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_token', full_name='dataquery.MetadataRequest.user_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_id', full_name='dataquery.MetadataRequest.data_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='dataquery.MetadataRequest.data_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=206,
  serialized_end=296,
)


_METADATARESPONSE = _descriptor.Descriptor(
  name='MetadataResponse',
  full_name='dataquery.MetadataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_code', full_name='dataquery.MetadataResponse.response_code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='dataquery.MetadataResponse.meta_data', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=298,
  serialized_end=358,
)

DESCRIPTOR.message_types_by_name['GetDataRequest'] = _GETDATAREQUEST
DESCRIPTOR.message_types_by_name['GetDataResponse'] = _GETDATARESPONSE
DESCRIPTOR.message_types_by_name['MetadataRequest'] = _METADATAREQUEST
DESCRIPTOR.message_types_by_name['MetadataResponse'] = _METADATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDataRequest = _reflection.GeneratedProtocolMessageType('GetDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAREQUEST,
  '__module__' : 'dataquery_pb2'
  # @@protoc_insertion_point(class_scope:dataquery.GetDataRequest)
  })
_sym_db.RegisterMessage(GetDataRequest)

GetDataResponse = _reflection.GeneratedProtocolMessageType('GetDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATARESPONSE,
  '__module__' : 'dataquery_pb2'
  # @@protoc_insertion_point(class_scope:dataquery.GetDataResponse)
  })
_sym_db.RegisterMessage(GetDataResponse)

MetadataRequest = _reflection.GeneratedProtocolMessageType('MetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _METADATAREQUEST,
  '__module__' : 'dataquery_pb2'
  # @@protoc_insertion_point(class_scope:dataquery.MetadataRequest)
  })
_sym_db.RegisterMessage(MetadataRequest)

MetadataResponse = _reflection.GeneratedProtocolMessageType('MetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _METADATARESPONSE,
  '__module__' : 'dataquery_pb2'
  # @@protoc_insertion_point(class_scope:dataquery.MetadataResponse)
  })
_sym_db.RegisterMessage(MetadataResponse)



_DATAQUERY = _descriptor.ServiceDescriptor(
  name='DataQuery',
  full_name='dataquery.DataQuery',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=361,
  serialized_end=514,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetData',
    full_name='dataquery.DataQuery.GetData',
    index=0,
    containing_service=None,
    input_type=_GETDATAREQUEST,
    output_type=_GETDATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InspectMetadata',
    full_name='dataquery.DataQuery.InspectMetadata',
    index=1,
    containing_service=None,
    input_type=_METADATAREQUEST,
    output_type=_METADATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAQUERY)

DESCRIPTOR.services_by_name['DataQuery'] = _DATAQUERY

# @@protoc_insertion_point(module_scope)
