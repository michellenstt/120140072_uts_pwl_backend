import logging

import grpc
import client_produk.grpc.produk_pb2_grpc as products_pb2_grpc
import client_produk.grpc.produk_pb2 as products_pb2


class ProductClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 6000

        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = products_pb2_grpc.ProdukServiceStub(self.channel)

    def get_all(self):
        response = self.stub.List(products_pb2.ProdukListRequest())

        if len(response.produk) == 0:
            return None

        return [
            dict(
                id=product.id,
                nama=product.nama,
                deskripsi=product.deskripsi,
                harga=product.harga,
                gambar=product.gambar,
                stok=product.stok,
            )
            for product in response.produk
        ]

    def get_by_id(self, id):
        response = self.stub.Detail(products_pb2.ProdukDetailRequest(id=id))

        if response.Produk == None:
            return None

        return dict(
            id=response.Produk.id,
            nama=response.Produk.nama,
            deskripsi=response.Produk.deskripsi,
            harga=response.Produk.harga,
            gambar=response.Produk.gambar,
            stok=response.Produk.stok,
        )

    def create(self, nama, deskripsi, harga, gambar, stok):
        response = self.stub.Create(
            products_pb2.ProdukCreateRequest(
                nama=nama,
                deskripsi=deskripsi,
                harga=harga,
                gambar=gambar,
                stok=stok,
            )
        )

        return dict(
            nama=response.produk.nama,
            deskripsi=response.produk.deskripsi,
            harga=response.produk.harga,
            gambar=response.produk.gambar,
            stok=response.produk.stok,
        )

    def update(self, id, nama, deskripsi, harga, gambar, stok):
        response = self.stub.Update(
            products_pb2.ProdukUpdateRequest(
                deskripsi=deskripsi,
                harga=harga,
                gambar=gambar,
                stok=stok,
                id=id,
                nama=nama,
            )
        )

        if response.Produk is None:
            return None

        return dict(
            id=response.Produk.id,
            nama=response.Produk.nama,
            deskripsi=response.Produk.deskripsi,
            harga=response.Produk.harga,
            gambar=response.Produk.gambar,
            stok=response.Produk.stok,
        )

    def delete(self, id):
        response = self.stub.Delete(products_pb2.ProdukDeleteRequest(id=id))

        if response is None:
            return None

        return dict(message="Produk berhasil dihapus")

    def jumlah_harga(self, id):
        response = self.stub.HitungHarga(products_pb2.HitungHargaRequest(id=id))

        if response.harga is None:
            return None

        return dict(
            harga=response.harga,
        )
