# Chocolate Sales Clustering & FastAPI Deployment

Proyek ini bertujuan untuk melakukan segmentasi (clustering) data penjualan cokelat menggunakan algoritma Machine Learning unsupervised, yaitu **K-Means Clustering**, dan menyajikannya dalam bentuk REST API menggunakan **FastAPI**.

## 🚀 Fitur Proyek
- **Unsupervised Learning**: Mengelompokkan data penjualan berdasarkan jumlah transaksi (`amount`) dan total barang yang dikirim (`boxes_shipped`).
- **FastAPI Deployment**: Menyediakan endpoint `/predict` berbasis web service untuk melakukan prediksi klaster data penjualan secara *real-time*.

## 📂 Struktur Folder
```text
├── 01-chocolate-sales-clustering-api/
│   ├── main.py                 # Script utama FastAPI
│   ├── kmeans_chocolate.pkl    # Model Machine Learning yang sudah di-train
│   ├── Chocolate Sales (2).csv # Dataset penjualan cokelat
│   └── README.md               # Dokumentasi proyek


🛠️ Cara Menjalankan API (Lokal)

Pastikan library yang dibutuhkan sudah terinstal:
pip install fastapi uvicorn scikit-learn pandas joblib

Jalankan server FastAPI menggunakan Uvicorn:
uvicorn main:app --reload

Buka dokumentasi interaktif di browser:
http://127.0.0.1:8000/docs

Dibuat sebagai bagian dari Portofolio AI Engineer.