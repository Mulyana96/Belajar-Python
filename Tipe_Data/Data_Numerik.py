# Tipe data numerik
angka_bulat = 10  # Integer
angka_desimal = 3.14  # Float
kompleks = 1j + 2  # Complex

print("Tipe data numerik:")
print(f"Angka bulat: {angka_bulat} ({type(angka_bulat)})")
print(f"Angka desimal: {angka_desimal} ({type(angka_desimal)})")
print(f"Bilangan kompleks: {kompleks} ({type(kompleks)})\n")

# Operasi pada tipe data numerik
hasil_tambah = angka_bulat + angka_desimal
hasil_kali = angka_bulat * angka_desimal
hasil_bagi = angka_bulat / angka_desimal
hasil_pangkat = angka_bulat ** 2

print("Operasi pada tipe data numerik:")
print(f"Penjumlahan: {angka_bulat} + {angka_desimal} = {hasil_tambah}")
print(f"Perkalian: {angka_bulat} * {angka_desimal} = {hasil_kali}")
print(f"Pembagian: {angka_bulat} / {angka_desimal} = {hasil_bagi}")
print(f"Pangkat: {angka_bulat} ** 2 = {hasil_pangkat}\n")

# Fungsi pada tipe data numerik
abs_bulat = abs(angka_bulat)
pow_desimal = pow(angka_desimal, 2)
sqrt_kompleks = cmath.sqrt(kompleks)

print("Fungsi pada tipe data numerik:")
print(f"Nilai absolut bilangan bulat: abs({angka_bulat}) = {abs_bulat}")
print(f"Pangkat dua bilangan desimal: pow({angka_desimal}, 2) = {pow_desimal}")
print(f"Akar kuadrat bilangan kompleks: cmath.sqrt({kompleks}) = {sqrt_kompleks}")
