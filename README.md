<div align="center">

<h1>🎨 UCD Usability Analytics</h1>

<h3>Prediksi Keberhasilan Pengguna & Analisis Beban Kognitif Antarmuka Berbasis Machine Learning</h3>

*Dari pengujian usability ➔ identifikasi beban kognitif ➔ prediksi kesuksesan tugas ➔ rekomendasi desain berbasis data.*

<br>

<!-- BAGIAN LOGO / BADGES -->
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python" />
<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
<img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
<img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" alt="Matplotlib" />

<br><br>

<!-- MENU NAVIGASI -->
- <a href="#-studi-kasus">📖 Studi Kasus</a>
- <a href="#-piramida-analitik">🔺 Piramida Analitik</a>
- <a href="#-arsitektur--alur-kerja">🏗️ Arsitektur</a>
- <a href="#-cara-menjalankan">🚀 Cara Menjalankan</a>
- <a href="#-contoh-output">📊 Contoh Output</a>

</div>

<br>

## 📖 Studi Kasus

Proyek ini menerapkan konsep **Interaksi Manusia Komputer (IMK)** dan **User-Centered Design (UCD)** yang dikombinasikan dengan pemodelan *Data Science*.

**Konteks Masalah:**
Aplikasi layanan "SehatInklusif" melakukan *redesign* antarmuka dari Graphical User Interface (GUI) konvensional ke desain inklusif baru. Tim produk ingin mengevaluasi apakah antarmuka baru berhasil menekan *Extraneous Load* (beban kognitif akibat navigasi yang buruk) serta meningkatkan *Success Rate* pengguna dari berbagai segmen persona (Gen Z, Profesional, dan Lansia).

**Tujuan Solusi:**
Membangun model *Machine Learning* menggunakan algoritma `RandomForestClassifier` untuk memprediksi probabilitas keberhasilan pengguna (*Task Success*) berdasarkan metrik *usability testing* (waktu penyelesaian dan jumlah *error*), serta mengidentifikasi fitur paling dominan yang memengaruhi pengalaman pengguna.

---

## 🔺 Piramida Analitik

Proyek ini mengadopsi 4 tingkat analisis data secara *end-to-end* dalam domain evaluasi UI/UX:

1. **Deskriptif (Apa yang terjadi?):** Mengukur rata-rata durasi penyelesaian tugas (*Task Time*) dan frekuensi kesalahan klik (*Jumlah Error*) di setiap versi UI.
2. **Diagnostik (Mengapa terjadi?):** *Extraneous Load* yang tinggi dan hirarki navigasi yang kompleks menyebabkan tingginya angka *error* serta kegagalan tugas pengguna.
3. **Prediktif (Apa yang akan terjadi?):** Model `RandomForestClassifier` memprediksi apakah seorang pengguna berpotensi berhasil (1) atau gagal/menyerah (0) dalam menyelesaikan transaksi.
4. **Preskriptif (Apa yang harus dilakukan?):** Berdasarkan analisis *Feature Importance*, manajemen UI/UX direkomendasikan untuk memangkas langkah navigasi (*Overview First*) dan mengoptimalkan elemen kontras/aksesibilitas khusus segmen Lansia.

---

## 🏗️ Arsitektur & Alur Kerja

Sistem ini memproses data uji *usability*, membersihkan anomali interaksi (seperti *user* yang AFK/tertinggal saat pengujian *remote*), melakukan pengkodean variabel kategorikal persona, dan mengekstrak bobot kepentingan fitur.

```mermaid
graph LR
    A[Usability Testing Data] --> B[Data Preprocessing & Outlier Removal]
    B --> C[One-Hot Encoding Persona & UI]
    C --> D[Train/Test Split]
    D --> E[Random Forest Classifier]
    E --> F[Feature Importance & Insight Bisnis]
