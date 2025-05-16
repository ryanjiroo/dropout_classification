# Proyek Akhir: Memprediksi Risiko Dropout di Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat permasalahan serius terkait tingginya jumlah siswa yang tidak menyelesaikan pendidikannya alias **dropout**.

Jumlah dropout yang tinggi ini menjadi masalah besar bagi institusi pendidikan karena dapat menurunkan reputasi, menimbulkan kerugian finansial, dan menurunkan efektivitas proses pembelajaran. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi sedini mungkin siswa yang berisiko melakukan dropout agar dapat diberikan bimbingan khusus dan intervensi tepat waktu.
---

### Permasalahan Bisnis

- Tingginya angka **dropout** siswa di Jaya Jaya Institut.
- Kesulitan dalam mengidentifikasi siswa berisiko secara dini.
- Kurangnya pemantauan terhadap faktor-faktor yang mempengaruhi dropout.
- Minimnya informasi berbasis data untuk pengambilan keputusan akademik.

---

### Cakupan Proyek

- Melakukan **analisis faktor-faktor** yang mempengaruhi dropout siswa, antara lain:
  - Age (Umur saat enrollment)
  - Gender (Jenis kelamin)
  - Scholarship_holder (Status penerima beasiswa)
  - Curricular_units_1st_sem_grade (Nilai semester 1)
  - Curricular_units_2nd_sem_grade (Nilai semester 2)
- Membangun **model prediksi** untuk mendeteksi risiko dropout siswa.
- Membuat **dashboard interaktif** untuk membantu pihak akademik memonitor performa dan risiko dropout siswa.
- Memberikan **rekomendasi strategis** berdasarkan hasil analisis.

---

### Persiapan

**Sumber Data:** Dataset performa siswa dari Jaya Jaya Institut (contoh: students' performance)

**Setup Environment:**

```bash
pip install -r requirements.txt
```
## Business Dashboard

**Deskripsi:**  
Dashboard yang dibuat berfungsi untuk:

- Memantau faktor-faktor utama yang mempengaruhi risiko dropout seperti:
  - Umur saat enrollment
  - Jenis kelamin
  - Status penerima beasiswa
  - Nilai semester pertama dan kedua
- Menyediakan visualisasi interaktif yang memudahkan staf akademik dalam memahami performa siswa dan potensi risiko dropout.

*Link dashboard (misal Tableau Public, Power BI, Metabase) dapat ditambahkan jika tersedia.*

---

## Kesimpulan

Berdasarkan hasil analisis data dan pemodelan:

1. Dropout terbanyak terjadi pada siswa dengan **umur 20-25 tahun** saat enrollment.
2. **Perempuan** menjadi kelompok dengan jumlah dropout tertinggi.
3. Siswa yang mengalami **penurunan nilai pada semester kedua** memiliki kecenderungan lebih tinggi untuk dropout.
4. Siswa yang **tidak menerima beasiswa** memiliki risiko dropout lebih besar dibanding yang menerima beasiswa.

Model prediksi terbaik yang digunakan adalah **Random Forest Classifier** dengan akurasi yang baik untuk mendukung proses identifikasi risiko dropout.

---

## Rekomendasi Action Items

Untuk menekan angka dropout, beberapa langkah yang direkomendasikan adalah:

- Mengadakan program **bimbingan khusus** bagi siswa berusia 20-25 tahun sejak awal semester.
- Memberikan **dukungan dan konseling khusus bagi mahasiswa perempuan** untuk mengurangi risiko dropout.
- Melakukan **monitoring dan pendampingan intensif** bagi siswa yang mengalami penurunan nilai di semester kedua.
- Memperluas dan meningkatkan program **beasiswa** agar lebih banyak siswa dapat terbantu secara finansial.
- Menggunakan **dashboard secara rutin** untuk memantau performa siswa dan mengambil tindakan preventif secara cepat.

> **Deployment:**  
> Aplikasi ini telah dideploy menggunakan [Streamlit](https://dropoutclassification.streamlit.app/)
