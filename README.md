# BabyCry AI

Website mobile-first untuk merekam dan mempratinjau audio bayi sebagai dasar eksperimen AI yang bertanggung jawab.

## Status saat ini

**Prototype frontend, belum memakai model AI pengenal tangisan.** Audio dapat direkam atau dipilih dan diputar kembali secara lokal di browser. Form konteks bayi telah dihapus sesuai keputusan produk. Model AI belum terintegrasi dan audio belum dianalisis. Jangan menyebut hasil ini sebagai prediksi AI atau akurasi model.

## Fitur

- Tampilan responsif untuk HP dan desktop.
- Rekam audio melalui mikrofon browser (membutuhkan HTTPS dan izin mikrofon).
- Pilih file audio untuk pratinjau.
- Tidak mengirim audio ke server pada versi frontend saat ini.
- Peringatan keselamatan dan batasan penggunaan.
- Audio tidak dikirim ke server oleh implementasi frontend ini.

## Jalankan lokal

Buka `index.html` di browser modern. Untuk izin mikrofon yang lebih konsisten, jalankan melalui server lokal atau gunakan GitHub Pages (HTTPS).

## Deploy dengan GitHub Pages

1. Workflow GitHub Actions di `.github/workflows/pages.yml` men-deploy situs dari branch `main`.
2. Pada **Settings → Pages**, pilih **GitHub Actions** sebagai source.
3. Periksa tab **Actions** sampai workflow berstatus sukses.
4. Situs: https://filzazyah.github.io/Babycry-ai/

## Roadmap AI

1. Audit sumber data dan lisensi dataset — lihat [audit dataset](docs/DATASET_RESEARCH.md).
2. Buat skrip audit lokal untuk distribusi kelas, format audio, duplikasi, dan sampel rusak.
3. Buat pipeline audio dan baseline klasifikasi.
4. Pisahkan bayi/identitas rekaman antara train, validation, dan test untuk menghindari data leakage.
5. Laporkan macro-F1, precision/recall per kelas, confusion matrix, dan kalibrasi; jangan hanya melaporkan accuracy.
6. Uji pada rekaman yang benar-benar terpisah dan lingkungan nyata sebelum menyebut model siap digunakan.
7. Integrasikan backend inferensi atau model browser yang sudah diuji.

## Keselamatan dan privasi

- Aplikasi ini bukan alat diagnosis dan tidak menentukan apakah bayi sehat.
- Jangan menunda pertolongan medis karena aplikasi.
- Tangisan tidak biasa atau kekhawatiran pengasuh perlu ditangani dengan pemeriksaan langsung. Kesulitan bernapas, bibir membiru, kejang, atau sulit dibangunkan memerlukan pertolongan darurat. Bayi di bawah 3 bulan dengan suhu 38°C atau lebih perlu penilaian medis segera.
- Jangan commit rekaman bayi, data identitas, token, atau informasi pribadi ke repository.

## Referensi awal

- Audit kandidat dataset: [docs/DATASET_RESEARCH.md](docs/DATASET_RESEARCH.md)
- Donate-a-Cry Corpus: https://github.com/gveres/donateacry-corpus
- InfantCry-DBL v2: https://data.mendeley.com/datasets/x493z8nmwc/2
- BABYCRY-UJM-AXA: https://zenodo.org/records/19205929
- Hugging Face babycry: https://huggingface.co/datasets/owlgebra-ai/babycry
- Penelitian interpretasi tangisan bayi (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC10882089/
- Tinjauan sistematis klasifikasi tangisan bayi: https://pmc.ncbi.nlm.nih.gov/articles/PMC12804663/
- Deteksi tangisan di lingkungan nyata: https://arxiv.org/abs/2005.07036
