# Menjalankan audit lokal dan menyiapkan baseline

Dokumen ini menjelaskan prosedur eksperimen; ini bukan bukti model telah dilatih. Dataset dan laporan audit tidak otomatis diunduh, di-commit, atau diunggah oleh skrip.

## 1. Siapkan dataset

1. Buka sumber Donate-a-Cry: https://github.com/gveres/donateacry-corpus
2. Baca README, ODbL, DBCL, dan ketentuan penggunaan sebelum mengunduh atau menggunakan data.
3. Simpan dataset di folder lokal di luar repository Babycry-ai.
4. Pastikan path yang diberikan adalah folder hasil ekstraksi dataset yang benar.

Jangan unggah rekaman bayi pribadi ke Colab atau layanan eksternal tanpa persetujuan yang jelas dan peninjauan kebijakan privasi.

## 2. Jalankan skrip audit

Skrip menggunakan standard library Python. ffprobe dari FFmpeg bersifat opsional dan dipakai untuk mencoba membaca durasi serta codec.

Windows PowerShell, contoh:

```powershell
py .\scripts\audit_donateacry.py "D:\datasets\donate-a-cry"
```

Lewati pemeriksaan hash untuk proses yang lebih cepat:

```powershell
py .\scripts\audit_donateacry.py "D:\datasets\donate-a-cry" --skip-hashes
```

Laporan `dataset_audit_report.json` memuat statistik agregat: jumlah label dari tag nama file, ekstensi, ukuran file, hasil probe, dan duplikat SHA-256. Nama file dan path tidak dimasukkan. Simpan laporan lokal dahulu dan tinjau sebelum dibagikan.

**Penting:** parsing tag nama file bersifat heuristik. Tag seperti `hu` atau `bp` merupakan laporan kontributor, bukan diagnosis atau ground truth klinis. Skrip belum memastikan isi audio benar-benar tangisan.

## 3. Kriteria sebelum membuat baseline

- Audit lisensi dan catat atribusi yang diwajibkan.
- Tinjau distribusi kelas, file kosong/rusak, format, durasi, dan duplikat.
- Jika identitas bayi/sumber tersedia, gunakan untuk group split; rekaman dari bayi/sumber yang sama tidak boleh masuk train dan test sekaligus.
- Tetapkan train/validation/test sebelum memilih model atau menyetel hyperparameter.
- Laporkan macro-F1, precision dan recall per kelas, confusion matrix, jumlah sampel per kelas, dan baseline sederhana.
- Sediakan opsi “tidak yakin” untuk skor rendah atau audio di luar distribusi; jangan memaksa setiap rekaman menjadi satu label.
- Catat versi data, kode, konfigurasi, random seed, model, dan metrik agar eksperimen bisa direproduksi.

## 4. Batas klaim

Jangan menyebut model sebagai alat diagnosis atau mengklaim dapat mengetahui kebutuhan bayi secara pasti. Evaluasi offline tidak membuktikan performa pada rekaman HP di rumah. Jika bayi tampak sakit atau pengasuh khawatir, cari saran tenaga kesehatan; jangan menunda pertolongan berdasarkan hasil aplikasi.
