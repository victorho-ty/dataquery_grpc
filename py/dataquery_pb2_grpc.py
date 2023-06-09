# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dataquery_pb2 as dataquery__pb2


class DataQueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetData = channel.unary_unary(
                '/dataquery.DataQuery/GetData',
                request_serializer=dataquery__pb2.GetDataRequest.SerializeToString,
                response_deserializer=dataquery__pb2.GetDataResponse.FromString,
                )
        self.InspectMetadata = channel.unary_unary(
                '/dataquery.DataQuery/InspectMetadata',
                request_serializer=dataquery__pb2.MetadataRequest.SerializeToString,
                response_deserializer=dataquery__pb2.MetadataResponse.FromString,
                )


class DataQueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InspectMetadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataQueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=dataquery__pb2.GetDataRequest.FromString,
                    response_serializer=dataquery__pb2.GetDataResponse.SerializeToString,
            ),
            'InspectMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.InspectMetadata,
                    request_deserializer=dataquery__pb2.MetadataRequest.FromString,
                    response_serializer=dataquery__pb2.MetadataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dataquery.DataQuery', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataQuery(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataquery.DataQuery/GetData',
            dataquery__pb2.GetDataRequest.SerializeToString,
            dataquery__pb2.GetDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InspectMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dataquery.DataQuery/InspectMetadata',
            dataquery__pb2.MetadataRequest.SerializeToString,
            dataquery__pb2.MetadataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
