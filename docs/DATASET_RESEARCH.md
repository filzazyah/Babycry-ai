# Audit Dataset AI BabyCry

Tanggal audit: 19 Oktober 2026

Dokumen ini menilai kandidat data untuk eksperimen awal. Tidak ada dataset yang diunduh atau dimasukkan ke repository pada tahap audit ini. File audio bayi jangan di-commit ke GitHub.

## Ringkasan keputusan

Mulai eksperimen baseline dengan Donate-a-Cry setelah memeriksa data dan ketentuan lisensi secara lokal. Dataset ini memiliki label alasan tangisan yang cocok untuk eksperimen klasifikasi awal, tetapi label diberikan oleh kontributor dan korpus aslinya disebut belum diperiksa. Karena itu, label bukan ground truth klinis dan tidak boleh dipakai untuk klaim diagnosis.

Untuk model BabyCry, jangan langsung menyamakan kelas dataset dengan kebutuhan bayi yang benar-benar diketahui. Hasil hanya boleh dijelaskan sebagai kemiripan pola audio dengan label yang tersedia pada dataset.

## Kandidat yang diverifikasi

### 1. Donate-a-Cry Corpus — kandidat baseline utama

- Sumber: https://github.com/gveres/donateacry-corpus
- Kegunaan: audio tangisan dengan tag alasan seperti hungry (hu), needs burping (bu), belly pain (bp), discomfort (dc), tired (ti), dan tag lainnya.
- Lisensi yang dicantumkan README sumber: Open Database License (ODbL); hak pada konten individual disebut Database Contents License (DBCL).
- Keterbatasan: README menyebut audio merupakan unggahan pengguna dalam bentuk asli, tidak dimodifikasi dan tidak diperiksa. Tag alasan diambil dari nama file dan dibuat oleh kontributor. Distribusi kelas sangat mungkin tidak seimbang; lakukan inventarisasi sebelum melatih.
- Langkah wajib: baca ODbL/DBCL dan syarat penggunaan yang menyertai sumber, catat atribusi, jangan redistribusikan audio mentah tanpa memahami kewajiban lisensinya, hitung jumlah sampel per kelas, cek duplikat dan audio yang bukan tangisan, serta dokumentasikan hasil audit.

### 2. InfantCry-DBL (Mendeley Data, versi 2, September 2026) — data tambahan, bukan label kebutuhan

- Sumber: https://data.mendeley.com/datasets/x493z8nmwc/2
- Keterangan sumber: 1.551 baris metadata/klip; dua tier yaitu 337 klip studio dari materi instruksional dan 1.214 klip in-the-wild. Label berupa kategori vokalisasi Dunstan Baby Language (eairh, eh, heh, neh, owh), bukan label klinis terverifikasi seperti lapar atau sakit.
- Lisensi yang dicantumkan: CC BY 4.0; sertakan atribusi dan sitasi bila digunakan.
- Kegunaan: eksperimen terpisah tentang klasifikasi kategori vokalisasi, atau menguji generalisasi lintas domain. Jangan gabungkan label DBL dengan label Donate-a-Cry seolah-olah kelasnya setara.
- Perhatian: sumber menganjurkan pemisahan train/validation/test berdasarkan bayi dan melaporkan macro-F1, F1 per kelas, balanced accuracy serta confusion matrix.

### 3. BABYCRY-UJM-AXA (Zenodo, 2026) — data akustik skala besar

- Sumber: https://zenodo.org/records/19205929
- Keterangan sumber: 107.312 segmen tangisan dari 1.000 bayi cukup bulan, usia sekitar 1–3 hari, audio WAV 44,1 kHz; arsip audio dilaporkan berukuran 81 GB dan menyertakan metadata serta 176 deskriptor akustik.
- Kegunaan: penelitian akustik tangisan neonatal dan deteksi/karakterisasi suara; bukan pilihan praktis pertama untuk eksperimen gratis di perangkat terbatas.
- Batasan: metadata akustik bukan label kebutuhan (lapar, mengantuk, popok, dan sebagainya). Periksa ketentuan akses dan lisensi secara langsung sebelum penggunaan; halaman yang diaudit tidak menampilkan lisensi dengan jelas, jadi jangan menganggapnya bebas digunakan.

### 4. Hugging Face owlgebra-ai/babycry — dataset gabungan, perlu audit per sumber

- Sumber: https://huggingface.co/datasets/owlgebra-ai/babycry
- Keterangan sumber: kartu dataset menyebut 7.574 klip untuk tugas valence positif vs distress, audio dan embedding; setiap baris mempertahankan lisensi sumber.
- Lisensi: per sumber, bukan satu lisensi global. Kartu menyebut ada bagian ESC-50 dengan CC BY-NC 3.0 yang tidak cocok untuk penggunaan komersial. Periksa source_license per baris sebelum memilih subset.
- Kegunaan: riset valence umum, bukan klasifikasi kebutuhan bayi. Jangan menganggap seluruh dataset boleh digunakan ulang dengan syarat yang sama.

## Rencana baseline yang aman dan hemat biaya

1. Jangan menyimpan data audio ke repository atau mengunggah rekaman pengguna ke layanan eksternal tanpa persetujuan yang jelas.
2. Buat skrip audit lokal untuk menghitung kelas dari nama file, format/durasi, file rusak, duplikat, dan distribusi kelas; simpan hanya ringkasan statistik yang tidak mengidentifikasi subjek.
3. Untuk baseline pertama, pilih tugas yang benar-benar didukung label. Jika memakai Donate-a-Cry, gunakan label sebagai alasan yang dilaporkan kontributor, bukan fakta medis.
4. Pisahkan train/validation/test berdasarkan identitas sumber/bayi bila identitas tersedia. Jangan membagi potongan dari bayi yang sama ke train dan test.
5. Laporkan macro-F1, balanced accuracy, precision/recall per kelas, confusion matrix dan jumlah sampel per kelas. Jangan klaim akurasi sebelum eksperimen benar-benar dijalankan.
6. Sediakan mekanisme tidak yakin / di luar distribusi dan jangan memaksa prediksi.
7. Uji domain shift dari rekaman asli ke rekaman HP di rumah. Hasil riset offline tidak membuktikan keamanan untuk keputusan perawatan.
8. Pertahankan GitHub Pages sebagai frontend. Backend gratis hanya untuk eksperimen; cek batas pemakaian, masa tidur, privasi, dan aturan penyimpanan sebelum mengirim audio ke layanan hosting.

## Batas keselamatan

Model ini tidak boleh mendiagnosis penyakit atau menyarankan menunda perawatan. Tangisan bayi tidak cukup untuk memastikan lapar, nyeri, atau kondisi medis. Jika bayi sulit bernapas, membiru, kejang, sulit dibangunkan, tampak sangat sakit, atau bayi di bawah 3 bulan memiliki suhu 38°C atau lebih, cari pertolongan medis segera.

## Sumber yang ditinjau

- Donate-a-Cry README dan lisensi: https://github.com/gveres/donateacry-corpus
- InfantCry-DBL v2: https://data.mendeley.com/datasets/x493z8nmwc/2
- BABYCRY-UJM-AXA: https://zenodo.org/records/19205929
- Hugging Face babycry: https://huggingface.co/datasets/owlgebra-ai/babycry