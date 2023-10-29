from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from client_produk.grpc.produk_grpc_client import ProductClient


@view_defaults(route_name="produk", renderer="json")
class ProdukController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET", renderer="json")
    def get_all(self):
        try:
            # if "id" in self.request.params:
            if self.request.params.get("id") is not None:
                client = ProductClient()
                produk = client.get_by_id(int(self.request.params.get("id")))

                if produk is None:
                    return Response(
                        status=404,
                        json_body={"status": False, "message": "Not Found"},
                    )

                return Response(status=200, json_body={"status": True, "data": produk})

            client = ProductClient()
            produk = client.get_all()

            if produk is None:
                return Response(
                    status=404, json_body={"status": False, "message": "Not Found"}
                )

            return Response(status=200, json_body={"status": True, "data": produk})
        except Exception as e:
            return Response(status=500, json_body={"status": False, "message": str(e)})

    @view_config(request_method="POST", renderer="json")
    def create(self):
        try:
            if (
                "nama" not in self.request.json_body
                or "deskripsi" not in self.request.json_body
                or "harga" not in self.request.json_body
                or "gambar" not in self.request.json_body
                or "stok" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Bad Request"},
                )

            client = ProductClient()
            produk = client.create(
                self.request.json_body["nama"],
                self.request.json_body["deskripsi"],
                self.request.json_body["harga"],
                self.request.json_body["gambar"],
                self.request.json_body["stok"],
            )

            return Response(status=200, json_body={"status": True, "data": produk})
        except Exception as e:
            return Response(status=500, json_body={"status": False, "message": str(e)})

    @view_config(request_method="PUT", renderer="json")
    def update(self):
        try:
            if (
                "id" not in self.request.json_body
                or "nama" not in self.request.json_body
                or "deskripsi" not in self.request.json_body
                or "harga" not in self.request.json_body
                or "gambar" not in self.request.json_body
                or "stok" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Bad Request"},
                )

            client = ProductClient()
            produk = client.update(
                self.request.json_body["id"],
                self.request.json_body["nama"],
                self.request.json_body["deskripsi"],
                self.request.json_body["harga"],
                self.request.json_body["gambar"],
                self.request.json_body["stok"],
            )

            print(produk)

            if produk is None:
                return Response(
                    status=404,
                    json_body={"status": False, "message": "Not Found"},
                )

            return Response(status=200, json_body={"status": True, "data": produk})

        except Exception as e:
            return Response(status=500, json_body={"status": False, "message": str(e)})

    @view_config(request_method="DELETE", renderer="json")
    def delete(self):
        try:
            if "id" not in self.request.params:
                return Response(
                    status=400,
                    json_body={"status": False, "message": "Bad Request"},
                )

            client = ProductClient()
            produk = client.delete(id=int(self.request.params.get("id")))

            print(produk)

            if produk is None:
                return Response(
                    status=404,
                    json_body={"status": False, "message": "Not Found"},
                )

            return Response(status=200, json_body={"status": True, "data": produk})
        except Exception as e:
            return Response(status=500, json_body={"status": False, "message": str(e)})


@view_config(route_name="jumlah_harga", request_method="POST", renderer="json")
def jumlah_harga(request):
    try:
        if request.json_body["id"] == None:
            return Response(json_body={"error": {"message": "OTL"}}, status=400)
        if len(request.json_body["id"]) == 0:
            return Response(
                json_body={"error": {"message": "id is required"}}, status=400
            )

        client = ProductClient()

        result = client.jumlah_harga(id=request.json_body["id"])
        return result

    except Exception as e:
        return Response(status=500, json_body={"status": False, "message": str(e)})
