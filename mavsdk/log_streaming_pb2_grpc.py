# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import log_streaming_pb2 as log__streaming_dot_log__streaming__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in log_streaming/log_streaming_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class LogStreamingServiceStub(object):
    """Provide log streaming data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartLogStreaming = channel.unary_unary(
                '/mavsdk.rpc.log_streaming.LogStreamingService/StartLogStreaming',
                request_serializer=log__streaming_dot_log__streaming__pb2.StartLogStreamingRequest.SerializeToString,
                response_deserializer=log__streaming_dot_log__streaming__pb2.StartLogStreamingResponse.FromString,
                _registered_method=True)
        self.StopLogStreaming = channel.unary_unary(
                '/mavsdk.rpc.log_streaming.LogStreamingService/StopLogStreaming',
                request_serializer=log__streaming_dot_log__streaming__pb2.StopLogStreamingRequest.SerializeToString,
                response_deserializer=log__streaming_dot_log__streaming__pb2.StopLogStreamingResponse.FromString,
                _registered_method=True)
        self.SubscribeLogStreamingRaw = channel.unary_stream(
                '/mavsdk.rpc.log_streaming.LogStreamingService/SubscribeLogStreamingRaw',
                request_serializer=log__streaming_dot_log__streaming__pb2.SubscribeLogStreamingRawRequest.SerializeToString,
                response_deserializer=log__streaming_dot_log__streaming__pb2.LogStreamingRawResponse.FromString,
                _registered_method=True)


class LogStreamingServiceServicer(object):
    """Provide log streaming data.
    """

    def StartLogStreaming(self, request, context):
        """Start streaming logging data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopLogStreaming(self, request, context):
        """Stop streaming logging data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeLogStreamingRaw(self, request, context):
        """Subscribe to logging messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogStreamingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartLogStreaming': grpc.unary_unary_rpc_method_handler(
                    servicer.StartLogStreaming,
                    request_deserializer=log__streaming_dot_log__streaming__pb2.StartLogStreamingRequest.FromString,
                    response_serializer=log__streaming_dot_log__streaming__pb2.StartLogStreamingResponse.SerializeToString,
            ),
            'StopLogStreaming': grpc.unary_unary_rpc_method_handler(
                    servicer.StopLogStreaming,
                    request_deserializer=log__streaming_dot_log__streaming__pb2.StopLogStreamingRequest.FromString,
                    response_serializer=log__streaming_dot_log__streaming__pb2.StopLogStreamingResponse.SerializeToString,
            ),
            'SubscribeLogStreamingRaw': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeLogStreamingRaw,
                    request_deserializer=log__streaming_dot_log__streaming__pb2.SubscribeLogStreamingRawRequest.FromString,
                    response_serializer=log__streaming_dot_log__streaming__pb2.LogStreamingRawResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.log_streaming.LogStreamingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.log_streaming.LogStreamingService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LogStreamingService(object):
    """Provide log streaming data.
    """

    @staticmethod
    def StartLogStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.log_streaming.LogStreamingService/StartLogStreaming',
            log__streaming_dot_log__streaming__pb2.StartLogStreamingRequest.SerializeToString,
            log__streaming_dot_log__streaming__pb2.StartLogStreamingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StopLogStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.log_streaming.LogStreamingService/StopLogStreaming',
            log__streaming_dot_log__streaming__pb2.StopLogStreamingRequest.SerializeToString,
            log__streaming_dot_log__streaming__pb2.StopLogStreamingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeLogStreamingRaw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.log_streaming.LogStreamingService/SubscribeLogStreamingRaw',
            log__streaming_dot_log__streaming__pb2.SubscribeLogStreamingRawRequest.SerializeToString,
            log__streaming_dot_log__streaming__pb2.LogStreamingRawResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)