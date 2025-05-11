from TabelHash import TabelHash

# Contoh Penggunaan

ulang = True

modulus = False

while ulang:
    
    # Membuat if jika modulus false atau dibawah 0
    if modulus == False:
        # Meminta input untuk modulus tabel hash
        modulus = int(input("Masukkan modulus untuk tabel hash (angka positif): "))
        if modulus <= 0:
            print("Modulus harus angka positif. Silakan coba lagi.")
            continue
        else:
            print(f"Modulus tabel hash yang valid: {modulus}")
            # Membuat objek tabel hash dengan ukuran modulus
            Tabel2b = TabelHash(modulus)
            print()
                
    else:
        print("Menu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Cek Data")
        print("4. Ubah Data")
        print("5. Tampilkan Data")
        print("6. Keluar")

        # Meminta input untuk modulus tabel hash
        pilihan = input("Silahkan pilih (1, 2, 3, atau 4) lalu Enter: ")

        # Menambahkan data ke dalam tabel hash
        if pilihan == '1':
            dataBaru = input("Masukkan data yang ingin anda tambahkan dengan format (data, key): ")
            # Memisahkan data jika ada koma
            dataBaru = dataBaru.split(",")
            if len(dataBaru) != 2:
                print("Format input tidak valid. Harus dalam format (data, key).")
                continue
            value = dataBaru[0].strip()
            key = dataBaru[1].strip()
            
            if key.isdigit():
                key = int(key)
            
            Tabel2b.insert(key, value)
            print(f"Data '{value}' dengan key '{key}' berhasil ditambahkan.")
            print()

        # Menghapus data dari tabel hash
        elif pilihan == '2':
            dataHapus = input("Masukkan data yang ingin dihapus: ")
            key = Tabel2b.searchKey(dataHapus)
            result = Tabel2b.remove(key)
            
            if result:
                print(f"Data '{dataHapus}' berhasil dihapus.")
            else:
                print(f"Data '{dataHapus}' tidak ditemukan.")
            print()

        # Mengecek apakah data ada dalam tabel hash
        elif pilihan == '3':
            dataCek = input("Masukkan data yang ingin dicek: ")
            key = Tabel2b.searchKey(dataCek)
            if key != None:
                print(f"Data '{dataCek}' ditemukan dengan key '{key}'.")
            else:
                print(f"Data '{dataCek}' tidak ditemukan.")
            print()
            
        # Mengubah data dalam tabel hash
        elif pilihan == '4':
            dataUbah = input("Masukkan data yang ingin diubah dengan format (data, key): ")
            # Memisahkan data jika ada koma
            dataUbah = dataUbah.split(",")
            if len(dataUbah) != 2:
                print("Format input tidak valid. Harus dalam format (data, key).")
                continue
            value = dataUbah[0].strip()
            key = int(dataUbah[1].strip())
            Tabel2b.insert(key, value)
            print(f"Data dengan key '{key}' berhasil diubah.")

        # Menampilkan data dalam antrian
        elif pilihan == '5':
            Tabel2b.display()
            print()
            
        # Keluar dari program
        elif pilihan == '6':
            print("Data akhir:")
            print()
            Tabel2b.display()
            print()
            
            print("Terima kasih telah menggunakan program ini.")
            # Menanyakan pengguna apakah ingin mencoba lagi menggunakan ternary operator
            ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
            ulang = True if ulang == 'y' else False
            if ulang == True:
                modulus = False
                print("Tabel Hash diulang.")
                print()
            else:
                print("Program selesai.")
                print()
            
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
            print()