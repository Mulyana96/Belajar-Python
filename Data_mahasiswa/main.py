class Mahasiswa:
  def __init__(self, nama, nim, jurusan, ipk):
    self.nama = nama
    self.nim = nim
    self.jurusan = jurusan
    self.ipk = ipk

  def tampilkan_data(self):
    print(f"Nama: {self.nama}")
    print(f"NIM: {self.nim}")
    print(f"Jurusan: {self.jurusan}")
    print(f"IPK: {self.ipk}")

def tambah_mahasiswa():
  nama = input("Masukkan nama: ")
  nim = input("Masukkan NIM: ")
  jurusan = input("Masukkan jurusan: ")
  ipk = float(input("Masukkan IPK: "))

  mahasiswa_baru = Mahasiswa(nama, nim, jurusan, ipk)
  data_mahasiswa.append(mahasiswa_baru)
  print("Mahasiswa baru telah ditambahkan!")

def lihat_data_mahasiswa():
  if not data_mahasiswa:
    print("Data mahasiswa masih kosong.")
  else:
    for mahasiswa in data_mahasiswa:
      mahasiswa.tampilkan_data()
      print("-" * 20)

def ubah_data_mahasiswa():
  if not data_mahasiswa:
    print("Data mahasiswa masih kosong.")
    return

  nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
  index = -1
  for i, mahasiswa in enumerate(data_mahasiswa):
    if mahasiswa.nim == nim:
      index = i
      break

  if index == -1:
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
  else:
    nama_baru = input("Masukkan nama baru: ")
    jurusan_baru = input("Masukkan jurusan baru: ")
    ipk_baru = float(input("Masukkan IPK baru: "))

    data_mahasiswa[index].nama = nama_baru
    data_mahasiswa[index].jurusan = jurusan_baru
    data_mahasiswa[index].ipk = ipk_baru
    print("Data mahasiswa telah diubah!")

def hapus_data_mahasiswa():
  if not data_mahasiswa:
    print("Data mahasiswa masih kosong.")
    return

  nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
  index = -1
  for i, mahasiswa in enumerate(data_mahasiswa):
    if mahasiswa.nim == nim:
      index = i
      break

  if index == -1:
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
  else:
    del data_mahasiswa[index]
    print("Data mahasiswa telah dihapus!")

# Inisiasi data mahasiswa
data_mahasiswa = []

# Menu utama
while True:
  print("\nMenu Pengelolaan Data Mahasiswa:")
  print("1. Tambah Mahasiswa")
  print("2. Lihat Data Mahasiswa")
  print("3. Ubah Data Mahasiswa")
  print("4. Hapus Data Mahasiswa")
  print("0. Keluar")

  print("==============================")

  pilihan = input("Masukkan pilihan Anda: ")

  if pilihan == "1":
    tambah_mahasiswa()
  elif pilihan == "2":
    lihat_data_mahasiswa()
  elif pilihan == "3":
    ubah_data_mahasiswa()
  elif pilihan == "4":
    hapus_data_mahasiswa()
  elif pilihan == "0":
    print("Terima kasih telah menggunakan program ini!")
    break
  else:
    print("Pilihan tidak valid. Silakan coba lagi.")
