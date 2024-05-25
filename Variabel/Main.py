# Deklarasi variabel
nama = "Budi"
umur = 20
tinggi_badan = 170  # cm
sudah_menikah = False

# Mencetak nilai variabel
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Tinggi badan: {tinggi_badan} cm")
print(f"Sudah menikah: {sudah_menikah}")

# Mengubah nilai variabel
umur += 1
tinggi_badan = 171
sudah_menikah = True

# Mencetak nilai variabel yang telah diubah
print("\nSetelah diubah:")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Tinggi badan: {tinggi_badan} cm")
print(f"Sudah menikah: {sudah_menikah}")

# Tipe data variabel
print("\nTipe data variabel:")
print(f"Nama: {type(nama)}")  # str
print(f"Umur: {type(umur)}")  # int
print(f"Tinggi badan: {type(tinggi_badan)}")  # int
print(f"Sudah menikah: {type(sudah_menikah)}")  # bool

# Operasi pada variabel
hasil_tambah = umur + 5
hasil_kali = tinggi_badan * 2
hasil_bagi = tinggi_badan / umur

print("\nOperasi pada variabel:")
print(f"Umur + 5 = {hasil_tambah}")
print(f"Tinggi badan * 2 = {hasil_kali}")
print(f"Tinggi badan / Umur = {hasil_bagi}")
