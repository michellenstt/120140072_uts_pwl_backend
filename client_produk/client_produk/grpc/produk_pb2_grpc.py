# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import client_produk.grpc.produk_pb2 as produk__pb2


class ProdukServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
            "/paroduk.ProdukService/List",
            request_serializer=produk__pb2.ProdukListRequest.SerializeToString,
            response_deserializer=produk__pb2.ProdukListResponse.FromString,
        )
        self.Detail = channel.unary_unary(
            "/paroduk.ProdukService/Detail",
            request_serializer=produk__pb2.ProdukDetailRequest.SerializeToString,
            response_deserializer=produk__pb2.ProdukDetailResponse.FromString,
        )
        self.Create = channel.unary_unary(
            "/paroduk.ProdukService/Create",
            request_serializer=produk__pb2.ProdukCreateRequest.SerializeToString,
            response_deserializer=produk__pb2.ProdukCreateResponse.FromString,
        )
        self.Update = channel.unary_unary(
            "/paroduk.ProdukService/Update",
            request_serializer=produk__pb2.ProdukUpdateRequest.SerializeToString,
            response_deserializer=produk__pb2.ProdukUpdateResponse.FromString,
        )
        self.Delete = channel.unary_unary(
            "/paroduk.ProdukService/Delete",
            request_serializer=produk__pb2.ProdukDeleteRequest.SerializeToString,
            response_deserializer=produk__pb2.ProdukDeleteResponse.FromString,
        )
        self.HitungHarga = channel.unary_unary(
            "/paroduk.ProdukService/HitungHarga",
            request_serializer=produk__pb2.HitungHargaRequest.SerializeToString,
            response_deserializer=produk__pb2.HitungHargaResponse.FromString,
        )


class ProdukServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Detail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def HitungHarga(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ProdukServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "List": grpc.unary_unary_rpc_method_handler(
            servicer.List,
            request_deserializer=produk__pb2.ProdukListRequest.FromString,
            response_serializer=produk__pb2.ProdukListResponse.SerializeToString,
        ),
        "Detail": grpc.unary_unary_rpc_method_handler(
            servicer.Detail,
            request_deserializer=produk__pb2.ProdukDetailRequest.FromString,
            response_serializer=produk__pb2.ProdukDetailResponse.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=produk__pb2.ProdukCreateRequest.FromString,
            response_serializer=produk__pb2.ProdukCreateResponse.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=produk__pb2.ProdukUpdateRequest.FromString,
            response_serializer=produk__pb2.ProdukUpdateResponse.SerializeToString,
        ),
        "Delete": grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=produk__pb2.ProdukDeleteRequest.FromString,
            response_serializer=produk__pb2.ProdukDeleteResponse.SerializeToString,
        ),
        "HitungHarga": grpc.unary_unary_rpc_method_handler(
            servicer.HitungHarga,
            request_deserializer=produk__pb2.HitungHargaRequest.FromString,
            response_serializer=produk__pb2.HitungHargaResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "paroduk.ProdukService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ProdukService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/paroduk.ProdukService/List",
            produk__pb2.ProdukListRequest.SerializeToString,
            produk__pb2.ProdukListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Detail(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/paroduk.ProdukService/Detail",
            produk__pb2.ProdukDetailRequest.SerializeToString,
            produk__pb2.ProdukDetailResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/paroduk.ProdukService/Create",
            produk__pb2.ProdukCreateRequest.SerializeToString,
            produk__pb2.ProdukCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/paroduk.ProdukService/Update",
            produk__pb2.ProdukUpdateRequest.SerializeToString,
            produk__pb2.ProdukUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Delete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/paroduk.ProdukService/Delete",
            produk__pb2.ProdukDeleteRequest.SerializeToString,
            produk__pb2.ProdukDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def HitungHarga(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/paroduk.ProdukService/HitungHarga",
            produk__pb2.HitungHargaRequest.SerializeToString,
            produk__pb2.HitungHargaResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
