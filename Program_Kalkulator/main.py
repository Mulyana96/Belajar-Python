def main():
  """Fungsi utama untuk menjalankan kalkulator."""

  while True:
    # Menampilkan menu operasi
    print("\nKalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    # Meminta masukan operasi dari pengguna
    pilihan = input("Masukkan pilihan Anda (1-5): ")

    # Memvalidasi input
    if not pilihan.isdigit() or int(pilihan) < 1 or int(pilihan) > 5:
      print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 5.")
      continue

    # Mengambil bilangan pertama
    bil1 = float(input("Masukkan bilangan pertama: "))

    # Mengambil bilangan kedua
    bil2 = float(input("Masukkan bilangan kedua: "))

    # Melakukan operasi berdasarkan pilihan
    if pilihan == "1":
      hasil = bil1 + bil2
      operasi = "+"
    elif pilihan == "2":
      hasil = bil1 - bil2
      operasi = "-"
    elif pilihan == "3":
      hasil = bil1 * bil2
      operasi = "*"
    elif pilihan == "4":
      hasil = bil1 / bil2
      operasi = "/"

    # Menampilkan hasil
    print(f"{bil1} {operasi} {bil2} = {hasil}")

    # Menanyakan apakah pengguna ingin melanjutkan
    lanjut = input("Apakah Anda ingin menghitung lagi? (y/t): ")
    if lanjut.lower() != "y":
      break

if __name__ == "__main__":
  main()
