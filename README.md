# BabyCry AI

Website mobile-first untuk membantu pengasuh memeriksa kemungkinan kebutuhan bayi melalui konteks perawatan dan rekaman audio.

## Status saat ini

**Prototype frontend, belum memakai model AI pengenal tangisan.** Audio dapat direkam atau dipilih dan diputar kembali secara lokal di browser. Hasil yang ditampilkan berasal dari konteks yang dimasukkan pengguna (misalnya waktu menyusu, tidur, dan popok), bukan dari analisis suara. Jangan menyebut hasil ini sebagai prediksi AI atau akurasi model.

## Fitur

- Tampilan responsif untuk HP dan desktop.
- Rekam audio melalui mikrofon browser (membutuhkan HTTPS dan izin mikrofon).
- Pilih file audio untuk pratinjau.
- Form konteks bayi dan daftar pemeriksaan berbasis aturan sederhana.
- Peringatan keselamatan dan batasan penggunaan.
- Audio tidak dikirim ke server oleh implementasi frontend ini.

## Jalankan lokal

Buka `index.html` di browser modern. Untuk izin mikrofon yang lebih konsisten, jalankan melalui server lokal atau gunakan GitHub Pages (HTTPS).

## Deploy dengan GitHub Pages

1. Buka **Settings → Pages** pada repository.
2. Di **Build and deployment**, pilih **Deploy from a branch**.
3. Pilih branch `main` dan folder `/ (root)`, lalu klik **Save**.
4. Tunggu deployment selesai. URL biasanya berbentuk `https://filzazyah.github.io/Babycry-ai/`.

## Roadmap AI

1. Audit sumber data dan lisensi dataset.
2. Buat pipeline audio dan baseline klasifikasi.
3. Pisahkan bayi/identitas rekaman antara train, validation, dan test untuk menghindari data leakage.
4. Laporkan macro-F1, precision/recall per kelas, confusion matrix, dan kalibrasi; jangan hanya melaporkan accuracy.
5. Uji pada rekaman yang benar-benar terpisah dan lingkungan nyata sebelum menyebut model siap digunakan.
6. Integrasikan backend inferensi atau model browser yang sudah diuji.

## Keselamatan dan privasi

- Aplikasi ini bukan alat diagnosis dan tidak menentukan apakah bayi sehat.
- Jangan menunda pertolongan medis karena aplikasi.
- Tangisan tidak biasa atau kekhawatiran pengasuh perlu ditangani dengan pemeriksaan langsung. Kesulitan bernapas, bibir membiru, kejang, atau sulit dibangunkan memerlukan pertolongan darurat. Bayi di bawah 3 bulan dengan suhu 38°C atau lebih perlu penilaian medis segera.
- Jangan commit rekaman bayi, data identitas, token, atau informasi pribadi ke repository.

## Referensi awal

- Donate-a-Cry Corpus: https://github.com/gveres/donateacry-corpus
- Penelitian interpretasi tangisan bayi (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC10882089/
- Tinjauan sistematis klasifikasi tangisan bayi: https://pmc.ncbi.nlm.nih.gov/articles/PMC12804663/
- Deteksi tangisan di lingkungan nyata: https://arxiv.org/abs/2005.07036
