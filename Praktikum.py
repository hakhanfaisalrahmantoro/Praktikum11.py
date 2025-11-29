## 1. Program Daftar Nilai Mahasiswa


### *Kode Program (Python)*

data_mahasiswa = {}

def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai: "))
    data_mahasiswa[nama] = nilai
    print("Data berhasil ditambahkan!\n")

def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data.\n")
    else:
        print("Daftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"{nama}: {nilai}")
        print()

def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus!\n")
    else:
        print("Nama tidak ditemukan.\n")

def ubah(nama):
    if nama in data_mahasiswa:
        nilai_baru = float(input("Masukkan nilai baru: "))
        data_mahasiswa[nama] = nilai_baru
        print("Data berhasil diubah!\n")
    else:
        print("Nama tidak ditemukan.\n")

# Menu utama
while True:
    print("=== MENU UTAMA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampilkan()
    elif pilih == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        hapus(nama)
    elif pilih == "4":
        nama = input("Masukkan nama yang akan diubah: ")
        ubah(nama)
    elif pilih == "5":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid!\n")
