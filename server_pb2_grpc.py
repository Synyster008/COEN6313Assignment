# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class AnalyserStub(object):
    """The analyse service description
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendRequest = channel.stream_stream(
                '/analyse.Analyser/SendRequest',
                request_serializer=server__pb2.RequestInfo.SerializeToString,
                response_deserializer=server__pb2.RequestReply.FromString,
                )


class AnalyserServicer(object):
    """The analyse service description
    """

    def SendRequest(self, request_iterator, context):
        """Both Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalyserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendRequest': grpc.stream_stream_rpc_method_handler(
                    servicer.SendRequest,
                    request_deserializer=server__pb2.RequestInfo.FromString,
                    response_serializer=server__pb2.RequestReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'analyse.Analyser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Analyser(object):
    """The analyse service description
    """

    @staticmethod
    def SendRequest(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/analyse.Analyser/SendRequest',
            server__pb2.RequestInfo.SerializeToString,
            server__pb2.RequestReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)