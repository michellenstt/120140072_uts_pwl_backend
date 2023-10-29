from concurrent import futures
import logging
import grpc
import produk_pb2
import produk_pb2_grpc

from database.config import engine
from sqlalchemy import insert, select, update, delete, desc

from models.produk import Produk


class ProductsServicer(produk_pb2_grpc.ProdukServiceServicer):
    def List(self, request, context):
        with engine.connect() as conn:
            stmt = select(Produk)
            rs = conn.execute(stmt)
            all_products = []
            for row in rs:
                product = produk_pb2.ProdukResponse()
                product.id = row["id"]
                product.nama = row["nama"]
                product.harga = row["harga"]
                product.deskripsi = row["deskripsi"]
                product.stok = row["stok"]
                product.gambar = row["gambar"]
                all_products.append(product)
            return produk_pb2.ProdukListResponse(data=all_products)

    def Detail(self, request, context):
        with engine.connect() as conn:
            stmt = select(Produk).where(Produk.id == request.id)
            rs = conn.execute(stmt)
            row = rs.fetchone()
            product = produk_pb2.ProdukResponse()
            product.id = row["id"]
            product.nama = row["nama"]
            product.harga = row["harga"]
            product.deskripsi = row["deskripsi"]
            product.stok = row["stok"]
            product.gambar = row["gambar"]
            return product

    def Create(self, request, context):
        with engine.connect() as conn:
            stmt = insert(Produk).values(
                nama=request.nama,
                harga=request.harga,
                deskripsi=request.deskripsi,
                stok=request.stok,
                gambar=request.gambar,
            )
            conn.execute(stmt)
            return produk_pb2.ProdukCreateResponse(
                message="Produk berhasil ditambahkan"
            )

    def Update(self, request, context):
        with engine.connect() as conn:
            stmt = (
                update(Produk)
                .where(Produk.id == request.id)
                .values(
                    nama=request.nama,
                    harga=request.harga,
                    deskripsi=request.deskripsi,
                    stok=request.stok,
                    gambar=request.gambar,
                )
            )
            conn.execute(stmt)
            return produk_pb2.ProdukUpdateResponse(message="Produk berhasil diupdate")

    def Delete(self, request, context):
        with engine.connect() as conn:
            stmt = delete(Produk).where(Produk.id == request.id)
            conn.execute(stmt)
            return produk_pb2.ProdukDeleteResponse(message="Produk berhasil dihapus")

    def HitungHarga(self, request, context):
        with engine.connect() as conn:
            stmt = select(Produk).where(Produk.id == request.id)
            rs = conn.execute(stmt)
            row = rs.fetchone()
            product = produk_pb2.HitungHargaResponse()
            product.harga = row["harga"]
            product.jumlah = request.jumlah
            product.total = row["harga"] * request.jumlah
            return product


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produk_pb2_grpc.add_ProdukServiceServicer_to_server(ProductsServicer(), server)
    server.add_insecure_port("localhost:5000")
    server.start()
    print("Server started at localhost:5000")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
