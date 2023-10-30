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
        try:
            with engine.connect() as conn:
                conn.begin()
                stmt = select(Produk)

                res = conn.execute(stmt).fetchall()

                produk = []

                for row in res:
                    produk.append(
                        produk_pb2.Produk(
                            id=row[0],
                            nama=row[1],
                            harga=row[2],
                            deskripsi=row[3],
                            stok=row[4],
                            gambar=row[5],
                        )
                    )

                conn.commit()

            return produk_pb2.ProdukListResponse(produk=produk)

        except Exception as e:
            print(e)
            return produk_pb2.ProdukListResponse()

    def Detail(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                stmt = select(Produk).where(Produk.id == request.id)

                res = conn.execute(stmt).fetchone()

                produk = produk_pb2.Produk(
                    id=res[0],
                    nama=res[1],
                    harga=res[2],
                    deskripsi=res[3],
                    stok=res[4],
                    gambar=res[5],
                )

                conn.commit()

            return produk_pb2.ProdukDetailResponse(Produk=produk)

        except Exception as e:
            print(e)
            return produk_pb2.ProdukDetailResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                stmt = insert(Produk).values(
                    nama=request.nama,
                    harga=request.harga,
                    stok=request.stok,
                    gambar=request.gambar,
                    deskripsi=request.deskripsi,
                )

                conn.execute(stmt)

                conn.commit()
            return produk_pb2.ProdukCreateResponse(
                produk=produk_pb2.Produk(
                    nama=request.nama,
                    harga=request.harga,
                    stok=request.stok,
                    gambar=request.gambar,
                    deskripsi=request.deskripsi,
                )
            )

        except Exception as e:
            print(e)
            return produk_pb2.ProdukCreateResponse()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                stmt = (
                    update(Produk)
                    .where(Produk.id == request.id)
                    .values(
                        nama=request.nama,
                        harga=request.harga,
                        stok=request.stok,
                        gambar=request.gambar,
                        deskripsi=request.deskripsi,
                    )
                )

                conn.execute(stmt)

                conn.commit()

            return produk_pb2.ProdukUpdateResponse(
                Produk=produk_pb2.Produk(
                    id=request.id,
                    nama=request.nama,
                    harga=request.harga,
                    stok=request.stok,
                    gambar=request.gambar,
                    deskripsi=request.deskripsi,
                )
            )

        except Exception as e:
            print(e)
            return produk_pb2.ProdukUpdateResponse()

    def HitungHarga(self, request, context):
        try:
            harga = 0
            ids = request.id

            for id in ids:
                with engine.connect() as conn:
                    conn.begin()
                    stmt = select(Produk).where(Produk.id == id)

                    res = conn.execute(stmt).fetchone()

                    harga += res[2]

                    conn.commit()

            return produk_pb2.HitungHargaResponse(harga=harga)

        except Exception as e:
            print(e)
            return produk_pb2.ProdukDetailResponse()

    def Delete(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()
                stmt = delete(Produk).where(Produk.id == request.id)

                conn.execute(stmt)

                conn.commit()

            return produk_pb2.ProdukDeleteResponse()

        except Exception as e:
            print(e)
            return produk_pb2.ProdukDeleteResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    produk_pb2_grpc.add_ProdukServiceServicer_to_server(ProductsServicer(), server)
    port = 6000
    server.add_insecure_port("localhost:{port}".format(port=port))
    server.start()
    print("Server started at localhost:{port}".format(port=port))
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
