# AI & Data Science Portfolio 🚀

Selamat datang di repositori portofolio saya! Repositori ini berisi kumpulan proyek di bidang *Data Science*, *Machine Learning*, dan *AI Engineering*, yang mendemonstrasikan kemampuan saya mulai dari eksplorasi data, pengembangan model prediktif, hingga implementasi sistem ke *production* (Deployment).

---

## 📂 Daftar Proyek

### 1. 🍫 Chocolate Sales Clustering & API Deployment (Unsupervised Learning)
* **Deskripsi**: Proyek analisis data penjualan cokelat menggunakan teknik klasterisasi untuk mengelompokkan pola pembelian, yang kemudian di-deploy menjadi REST API siap pakai.
* **Tech Stack**: Python, Scikit-Learn (K-Means), FastAPI, Uvicorn, Pandas, Joblib.
* **Fitur Utama**:
  * Menentukan jumlah klaster optimal menggunakan metode *Unsupervised Learning*.
  * Membangun REST API interaktif untuk prediksi klaster secara *real-time*.
  * Menyimpan model menggunakan `joblib` (`kmeans_chocolate.pkl`).
* **📁 Folder Proyek**: `01-chocolate-sales-clustering-api/`

### 2. 🛡️ Insurance Cross-Sell Prediction (Supervised Learning)
* **Deskripsi**: Proyek klasifikasi biner untuk memprediksi ketertarikan nasabah terhadap produk asuransi tambahan (*cross-sell*), dengan fokus menangani data yang tidak seimbang (*imbalanced data*).
* **Tech Stack**: Python, XGBoost, Scikit-Learn, Matplotlib, Pandas.
* **Fitur Utama**:
  * Mengatasi *class imbalance* menggunakan teknik `scale_pos_weight` pada algoritma XGBoost.
  * Evaluasi performa model yang komprehensif menghasilkan **ROC-AUC Score 0.8579** dan **Recall tinggi (0.92)** untuk kelas target.
  * Analisis pola fitur prediktif untuk mendukung *data-driven decision making*.
  * Menyimpan model menggunakan `joblib` (`insurance_model.pkl`).
* **📁 Folder Proyek**: `02-insurance-cross-sell-xgboost/`

---

## 🛠️ Skills & Tools
* **Languages**: Python
* **Machine Learning**: Scikit-Learn, XGBoost, K-Means Clustering
* **Deployment & MLOps**: FastAPI, Uvicorn, RESTful APIs
* **Data Handling & Visualization**: Pandas, NumPy, Matplotlib

---
*Dibuat dan dikembangkan oleh Avifah Dian Safitri, AI & Data Science Enthusiast.*
