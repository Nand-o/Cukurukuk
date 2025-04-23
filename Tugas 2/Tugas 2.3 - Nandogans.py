# Membuat program Antrian (queue) menggunakan bahasa Python

data = []

ulang = True

# Membuat kondisi untuk mengulangi program
while ulang == True:  
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    
    # Menggunakan input untuk pengguna memilih menu
    pilihan = (input("Silahkan pilih (1, 2, 3, atau 4) lalu Enter: "))

    # Menambahkan data ke dalam antrian
    if pilihan == '1':
        dataBaru = input("Masukkan data yang ingin anda tambahkan: ")
        # Memisahkan data jika ada koma
        dataBaru = dataBaru.split(",")
        for item in dataBaru:
            data.append(item.strip()) # (Strip) Menghapus spasi di awal dan akhir
        print("Data berhasil ditambahkan.")
        print()
        
    # Menghapus data dari antrian
    elif pilihan == '2':
        dataHapus = input("Masukkan data yang ingin anda hapus: ")
        if dataHapus in data: # Cek apakah data ada dalam antrian
            data.remove(dataHapus)
            print(f"Data '{dataHapus}' berhasil dihapus.")
        else:
            print(f"Data '{dataHapus}' tidak ditemukan dalam antrian.")
        print()
        
    # Menampilkan data dalam antrian
    elif pilihan == '3':
        # Mengurutkan data dalam antrian
        data.sort()
        if len(data) > 0:
            # Menampilkan data dalam antrian
            print("Data dalam antrian:")
            for i in range(len(data)):
                if i != len(data) - 1:
                    print(f"{data[i]} - ", end="")
                else:
                    print(f"{data[i]}.")
        else:
            print("Antrian kosong.")
        print()
        
    # Keluar dari program
    elif pilihan == '4':
        print("Data akhir dalam antrian:")
        # Menampilkan data dalam antrian
        if len(data) > 0:
            print("Data dalam antrian:")
            for i in range(len(data)):
                if i != len(data) - 1:
                    print(f"{data[i]} - ", end="")
                else:
                    print(f"{data[i]}.")
        else:
            print("Antrian kosong.")
            
        print("Terima kasih telah menggunakan program ini.")
        print()
        
        # Menggunakan ternary operator untuk menanyakan kepada pengguna apakah ingin mencoba lagi
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        ulang = True if ulang == 'y' else False
        if ulang == True:
            data = [] # Mengosongkan data
            print("Data diulang.")
            print()
            
        print("Program diulang.")
        print()
        
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")
        print()