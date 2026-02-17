# Queens Game - N-Queens Solver

## Penjelasan Program

Program ini adalah visualisasi interaktif untuk menyelesaikan masalah N-Queens dengan batasan warna menggunakan dua algoritma:

1. **Pure Brute Force** - Pencarian exhaustive dengan optimasi color groups
2. **Backtracking** - Pencarian dengan pruning untuk efisiensi lebih tinggi

Program memiliki fitur:
- Input board dari file text atau manual paste
- Visualisasi real-time proses pencarian solusi
- Export hasil ke format TXT dan PNG

---

## Requirement Program

### Software yang Diperlukan

1. **Python 3.8 atau lebih tinggi**
   - Download dari: https://www.python.org/downloads/

2. **pip** (Python package manager)
   - Biasanya sudah terinstall dengan Python

### Library Python yang Diperlukan

```
flet>=0.24.0
pillow>=10.0.0
```

---

## Instalasi

### 1. Clone atau Download Repository

```bash
# Jika menggunakan git
git clone 
cd Tucil1_13524075/src

# Atau extract ZIP file
unzip queens-game.zip
cd Tucil1_13524075/src
```

### 2. Install Dependencies

**Windows:**
```bash
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip3 install -r requirements.txt
```

**Atau install manual:**
```bash
pip install flet pillow
```

---

## Struktur File

```
  Tucil1_13524075/
├── doc/            # Laporan Tugas Kecil
├── src/            # Source Code program
│   ├── app.py      # Main GUI Entry Point (Flet)
│   ├── logic.py    # Implementasi Algoritma
│   ├── utils.py    # Fungsi utilitas & validasi
│   ├── requirements.txt
├── test/           # File uji kasus (.txt)
└── README.md 
```

---

## Cara Menjalankan Program

### Method 1: Via Command Line

**Windows:**
```bash
flet run --web --port 8550 app.py
```

**Linux/Mac:**
```bash
flet run --web --port 8550 app.py
```

### Method 2: Direct Python Execution

```bash
python app.py
```

### Akses Program

Setelah program berjalan, buka browser dan akses:
```
http://localhost:8550
```

**Catatan:** 
- Jika browser tidak terbuka otomatis, copy URL dari terminal
- Port 8550 bisa diganti sesuai kebutuhan

---

## Cara Menggunakan Program

### 1. Input Board

#### **Opsi A: Load dari File**
1. Siapkan file `.txt` dengan format:
   ```
   AABBC
   ABBDC
   ADDDC
   ABBBC
   EEEEE
   ```
2. Masukkan nama file di field "Nama File" (contoh: `tc1.txt`)
3. Klik tombol "Load Board"

#### **Opsi B: Manual Paste**
1. Paste board langsung di text area "Atau Paste Board di sini"
2. Format sama seperti file (baris per baris)
3. Klik tombol "Load Board"

**Syarat Board Valid:**
- Berbentuk persegi (NxN)
- Hanya mengandung huruf A-Z Pastikan Kapital
- Jumlah warna N 
- Satu Warna tidak terpecah atau terpisah

### 2. Pilih Algoritma

- **Centang switch** untuk Pure Brute Force (tanpa backtrack)
- **Tidak centang** untuk Backtracking (lebih cepat)

### 3. Jalankan Pencarian

1. Klik tombol **"MULAI PENCARIAN"**
2. Program akan menampilkan:
   - Visualisasi real-time proses pencarian
   - Status pencarian (sedang berjalan/selesai)
   - Durasi eksekusi
   - Jumlah konfigurasi yang dicek

### 4. Export Hasil

#### **Export ke TXT:**
- Klik "Ekspor ke File Txt"
- File tersimpan: `queens_solution_YYYYMMDD_HHMMSS.txt`
- Berisi board original dan solusi

#### **Export ke PNG:**
- Klik "Ekspor ke Gambar"  
- File tersimpan: `queens_solution_YYYYMMDD_HHMMSS.png`
- Berisi visualisasi board berwarna dengan posisi Queens

---

## Format Input

### File Text (`.txt`)

**Contoh 1: Board 5x5**
```
AABBC
ABBDC
ADDDC
ABBBC
EEEEE
```

**Contoh 2: Board 8x8**
```
AABBBBBC
AABBBBCC
AAABBBCC
AAADDBCC
EAAAAACC
EEEEAFFF
EEEAAGFF
HHEEEGGG
```

**Aturan:**
- Satu baris = satu row board
- Tanpa spasi antar karakter
- Hanya huruf kapital A-Z
- Jumlah warna unik harus tepat N (untuk board NxN)

---

## Contoh Output

### Output TXT
```
AABBBBBC
AABBBBCC
AAABBBCC
AAADDBCC
EAAAAACC
EEEEAFFF
EEEAAGFF
HHEEEGGG

Solution (# = Queen):
AAB#BBBC
AABBBB#C
AA#BBBCC
AAAD#BCC
#AAAAACC
EEEEAFF#
EEEAA#FF
H#EEEGGG
```

### Output PNG
- Grid berwarna sesuai karakter (A=Merah, B=Biru, dst)
- Label karakter di pojok kiri atas setiap cell
- "Q" putih besar di center cell yang berisi Queen
- Border hitam antar cell

## Author

**Nama:** Hakam Avicena Mustain 

**NIM:** 13524075

**Mata Kuliah:** Strategi Algoritma  

**Tanggal:** 11-18 Februari 2026

---

## Lisensi

Program ini dibuat untuk keperluan tugas akademik.

---

## Catatan Tambahan

- Program menggunakan Flet framework untuk GUI
- Visualisasi berjalan di web browser
- Export image menggunakan Pillow (PIL)
- Tidak ada compilation diperlukan (interpreted language)

---


Untuk pertanyaan atau bug report:
- Repository: https://github.com/hakamavicena/Tucil1_13524075