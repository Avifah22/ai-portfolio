# Chocolate Sales Clustering & FastAPI Deployment

Proyek ini bertujuan untuk melakukan segmentasi (clustering) data penjualan cokelat menggunakan algoritma Machine Learning unsupervised, yaitu **K-Means Clustering**, dan menyajikannya dalam bentuk REST API menggunakan **FastAPI**.

## 🚀 Fitur Proyek
- **Unsupervised Learning**: Mengelompokkan data penjualan berdasarkan jumlah transaksi (`amount`) dan total barang yang dikirim (`boxes_shipped`).
- **FastAPI Deployment**: Menyediakan endpoint `/predict` berbasis web service untuk melakukan prediksi klaster data penjualan secara *real-time*.
## 🛠️ Cara Menjalankan API (Lokal)

Pastikan library yang dibutuhkan sudah terinstal:
pip install fastapi uvicorn scikit-learn pandas joblib

Jalankan server FastAPI menggunakan Uvicorn:
uvicorn main:app --reload

Buka dokumentasi interaktif di browser:
http://127.0.0.1:8000/docs

## 📸 Bukti Eksekusi & Uji Coba API (menggunakan Google Collaboratory)
<img width="404" height="272" alt="11" src="https://github.com/user-attachments/assets/71a143ae-715a-4eec-9ed1-9db58517e8d6" />
**> *Gambar Dataset.Disclaimer: Dataset ini bersifat publik dan diambil dari https://www.kaggle.com/datasets/saidaminsaidaxmadov/chocolate-sales***
<img width="364" height="305" alt="12" src="https://github.com/user-attachments/assets/6f51b081-5e1d-43da-bc3c-8c9f059ba07a" />
**> *Gambar grafik Elbow Method untuk menentukan jumlah klaster (k) yang paling optimal***
<img width="283" height="365" alt="13" src="https://github.com/user-attachments/assets/2ed8dd34-7292-4ff8-8a4f-ef584bc9bc59" />
**> *Gambar di atas menunjukkan pengujian POST request secara lokal ke endpoint `/predict` menggunakan FastAPI dan Uvicorn. API berhasil menerima input data penjualan (`amount` dan `boxes_shipped`) dan mengembalikan hasil prediksi klaster secara real-time.***

## 📂 Struktur Folder
```text
├── 01-chocolate-sales-clustering-api/
│   ├── main.py                 # Script utama FastAPI
│   ├── kmeans_chocolate.pkl    # Model Machine Learning yang sudah di-train
│   ├── Chocolate Sales (2).csv # Dataset penjualan cokelat
│   └── README.md               # Dokumentasi proyek



Dibuat sebagai bagian dari Portofolio AI Engineer.


