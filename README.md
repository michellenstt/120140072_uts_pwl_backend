# 120140072 UTS BACKEND

## Cara menjalankan program

1. Pastikan python sudah terinstall di komputer anda `python --version`

## Cara menjalankan server gRPC

1. Masuk ke folder `server` dengan perintah `cd server`
2. Buat virtual environment dengan perintah `python -m venv venv`
3. Aktifkan virtual environment dengan perintah `.\env\Scripts\activate`
4. Buat database dengan nama `uts_pwl` di MySQL
5. Install semua dependencies dengan perintah `.\env\Scripts\pip install -e .`
6. Jalankan migrasi dengan perintah `.\env\Scripts\alembic upgrade head`
7. Jalankan server dengan perintah `.\env\Scripts\python -m server`
8. Server akan berjalan di port 6000

## Cara menjalankan client gRPC atau REST API

1. Masuk ke folder `client_produk` dengan perintah `cd client_produk`
2. Buat virtual environment dengan perintah `python -m venv venv`
3. Aktifkan virtual environment dengan perintah `.\env\Scripts\activate`
4. Install semua dependencies dengan perintah `.\env\Scripts\pip install -e .`
5. Jalankan client dengan perintah `.\env\Scripts\pserve development.ini --reload`
6. Client akan berjalan di port 6543
