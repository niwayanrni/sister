# Pub-Sub Aggregator System (Docker-Based)

## Deskripsi Proyek
Proyek ini merupakan implementasi **Pub-Sub (Publisher–Subscriber) Aggregator**, yaitu sistem yang menerima pesan dari publisher, menyimpannya, dan menyediakan data agregasi kepada subscriber.  
Sistem ini dikembangkan untuk memenuhi tugas mata kuliah **Sistem Terdistribusi (SISTER)** dengan tujuan memahami komunikasi antar proses, arsitektur terdistribusi, serta penggunaan container dengan **Docker**.

---

## Tujuan
Tujuan dari proyek ini antara lain:
- Mengimplementasikan layanan **publisher–subscriber** sederhana berbasis web.  
- Menyediakan endpoint untuk **mengirim (publish)** dan **mengambil data agregasi (get stats)**.  
- Menerapkan **Docker containerization** agar sistem dapat dijalankan secara konsisten di berbagai lingkungan.  
- Melakukan **pengujian performa (stress test)** terhadap proses publikasi dan agregasi pesan.

---

## Arsitektur dan Fungsionalitas
Sistem terdiri dari satu service utama berbasis **Flask API** yang berperan sebagai **aggregator**.

### Fungsionalitas Utama
1. **/publish**  
   - Menerima sekumpulan event dari publisher dalam format JSON.  
   - Setiap event diproses dan disimpan oleh aggregator.  
   - Sistem mengenali event duplikat agar tidak dihitung dua kali.  

2. **/stats**  
   - Digunakan oleh subscriber untuk mendapatkan hasil agregasi.  
   - Menampilkan statistik jumlah event yang diterima, jumlah unik, dan jumlah duplikat.  
   - Tidak memerlukan body JSON (cukup metode GET).

Arsitektur pub-sub ini memisahkan peran antara:
- **Publisher** → pengirim data.  
- **Subscriber** → penerima hasil agregasi.  
- **Aggregator** → pengelola komunikasi dan penyimpanan data.

---

## Containerization
Proyek ini dikemas menggunakan **Docker** agar dapat dijalankan secara portabel di berbagai sistem operasi.

### Langkah-Langkah Utama
- Membuat `Dockerfile` untuk membangun image service Flask.  
- Menjalankan container aggregator menggunakan Docker CLI.  
- Menguji endpoint menggunakan Postman dari luar container.

Pendekatan ini memastikan **isolasi lingkungan** dan **kemudahan deployment** tanpa konflik dependensi lokal.

---

## Pengujian Fungsional
Tahapan pengujian dilakukan untuk memverifikasi bahwa sistem berfungsi sesuai konsep pub-sub:

- Publisher dapat mengirim data ke `/publish` dan menerima respon “ok”.  
- Subscriber dapat mengakses `/stats` untuk melihat hasil agregasi.  
- Sistem mampu menangani data duplikat dengan akurat.  

Pengujian dilakukan melalui **Postman** dan **skrip Python** secara lokal.

---

## Pengujian Beban (Stress Test)
Untuk mengukur performa sistem, dilakukan stress test dengan mengirimkan **5000 event**, termasuk **1000 event duplikat**, menggunakan skrip `stress_test.py`.

### Hasil Pengujian:
- **Status Respon:** 200 OK  
- **Statistik:**  
  - Received = 5000  
  - Unique Processed = 4000  
  - Duplicates = 1000  
- **Waktu Eksekusi:** ±26.6 detik  

Hasil ini menunjukkan sistem mampu memproses ribuan event secara stabil dengan mekanisme deduplikasi yang efektif.

---

## Kesimpulan
Berdasarkan hasil implementasi dan pengujian:
- Sistem **pub-sub aggregator** berhasil dikembangkan dan dijalankan di lingkungan Docker.  
- Proses **publish** dan **get stats** berjalan sesuai konsep komunikasi terdistribusi.  
- Sistem mampu **mendeteksi duplikasi** dan mengolah data secara efisien.  
- Pengujian beban menunjukkan performa yang **stabil dan tangguh** dalam menangani ribuan event.  

Proyek ini menjadi dasar yang baik untuk pengembangan sistem **distributed event processing** yang lebih kompleks di masa mendatang.

---

## Link Youtube
