# Tipe data numerik
angka_bulat = 10  # Integer
angka_desimal = 3.14  # Float
kompleks = 1j + 2  # Complex

print("=" * 40)

print(f"Tipe data angka bulat: {type(angka_bulat)}")
print(f"Tipe data angka desimal: {type(angka_desimal)}")
print(f"Tipe data kompleks: {type(kompleks)}\n")

print("=" * 40)

# Tipe data string
teks = "Hello, World!"
kutipan = '"Python is fun!"'
karakter = 'c'

print(f"Tipe data teks: {type(teks)}")
print(f"Tipe data kutipan: {type(kutipan)}")
print(f"Tipe data karakter: {type(karakter)}\n")

print("=" * 40)

# Tipe data Boolean
benar = True
salah = False

print(f"Tipe data benar: {type(benar)}")
print(f"Tipe data salah: {type(salah)}\n")

print("=" * 40)

# Tipe data list
daftar_angka = [1, 2, 3, 4, 5]
daftar_campuran = ["Hello", 10, True]

print(f"Tipe data daftar angka: {type(daftar_angka)}")
print(f"Tipe data daftar campuran: {type(daftar_campuran)}\n")

print("=" * 40)

# Tipe data tuple
tupel_angka = (1, 2, 3, 4, 5)
tupel_campuran = ("Hello", 10, True)

print(f"Tipe data tupel angka: {type(tupel_angka)}")
print(f"Tipe data tupel campuran: {type(tupel_campuran)}\n")

print("=" * 40)

# Tipe data dictionary
kamus = {"nama": "Budi", "umur": 20, "jurusan": "Teknik Informatika"}

print(f"Tipe data kamus: {type(kamus)}\n")

print("=" * 40)

# Konversi tipe data
angka_str = str(angka_bulat)
desimal_int = int(angka_desimal)
teks_bool = bool(teks)

print(f"Konversi angka bulat ke string: {angka_str}")
print(f"Konversi angka desimal ke integer: {desimal_int}")
print(f"Konversi teks ke boolean: {teks_bool}")

print("=" * 40)
