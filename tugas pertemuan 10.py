# 1. a. Membuat tuple mahasiswa (ganti dengan data dirimu)
mahasiswa = ("Muhammad Novel Nur Fahmi", "2605060069", "Teknologi Informasi")
print(mahasiswa)

# b. Menampilkan NIM dan Prodi dengan mengakses indeks
print("NIM  :", mahasiswa[1])
print("Prodi:", mahasiswa[2])

# c. Mengubah elemen tuple (akan menimbulkan error)
# Hapus tanda # di bawah ini untuk mencoba dan melihat errornya
mahasiswa[2] = "Teknologi Informasi"

# d. Membuat set dari barisan angka
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)

#2. a. Membuat dictionary data_mahasiswa
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)

# b. Mengubah nilai prodi sekaligus menambah key angkatan
data_mahasiswa.update({"prodi": "Sastra Mesin", "angkatan": 2026})
print(data_mahasiswa)

# c. Menghapus data nim lalu menampilkan hasil akhir
del data_mahasiswa["nim"]
print(data_mahasiswa)

#3. a. Membuat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# b. Menampilkan setiap barang dan harganya
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")

# c. Menampilkan total belanja
total = 0
for harga in keranjang.values():
    total += harga
print(f"Total belanja: Rp {total}")

# Alternatif lebih singkat:
print(f"Total belanja: Rp {sum(keranjang.values())}")