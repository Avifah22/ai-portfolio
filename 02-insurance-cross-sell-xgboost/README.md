# Insurance Cross-Sell Prediction (XGBoost)

Proyek ini bertujuan untuk membangun model *Supervised Machine Learning* menggunakan algoritma **XGBoost** untuk memprediksi apakah seorang pelanggan asuransi kendaraan yang sudah ada tertarik untuk membeli produk asuransi tambahan (*cross-sell* asuransi kesehatan/kecelakaan).

## 🚀 Fitur Proyek
- **Supervised Learning & Classification**: Memanfaatkan data historis pelanggan untuk melakukan klasifikasi biner (Tertarik vs. Tidak Tertarik).
- **Model Optimization**: Menggunakan algoritma **XGBoost (Extreme Gradient Boosting)** yang handal untuk menangani data tabular dan klasifikasi kompleks.
- **Evaluation Metric**: Mengukur performa model menggunakan metrik seperti *ROC-AUC* untuk memastikan kehandalan prediksi.
- 
## 📸 Bukti Eksekusi & Uji Coba API (menggunakan Google Collaboratory)
<img width="515" height="185" alt="14" src="https://github.com/user-attachments/assets/ae68e7bf-b485-4c01-9578-e4e4625ccbd8" /> 
> *Gambar Dataset. **Disclaimer**: Dataset ini bersifat publik dan diambil dari [Kaggle Health Insurance Cross Sell Prediction](https://www.kaggle.com).*
<img width="445" height="229" alt="15" src="https://github.com/user-attachments/assets/28f3ccb2-f2bb-4012-81ae-ca3336c5bca2" />
> *Gambar proses training (pelatihan) model XGBoost untuk menangani data yang tidak seimbang (imbalanced data)*
<img width="287" height="169" alt="16" src="https://github.com/user-attachments/assets/2a1e9479-0513-4c5c-a6d7-59e528e9b747" />
> *Model XGBoost berhasil dilatih dengan menangani data tidak seimbang menggunakan scale_pos_weight. Model ini mencatatkan ROC-AUC Score sebesar 0.8579, yang menunjukkan performa prediktif yang kuat, serta memiliki nilai Recall 0.92 pada kelas minoritas, menandakan model sangat efektif dalam menangkap potensi nasabah yang ingin melakukan cross-sell*
## 📂 Struktur Folder
```text
├── 02-insurance-cross-sell-xgboost/
│   ├── insurance_model.pkl     # Model XGBoost yang sudah dilatih (opsional/jika ada)
│   ├── insurance_notebook.ipynb# Jupyter Notebook berisi eksplorasi dan training
│   └── README.md               # Dokumentasi proyek

---
Dibuat sebagai bagian dari Portofolio AI Engineer.
