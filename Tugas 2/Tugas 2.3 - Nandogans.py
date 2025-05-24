# Membuat program Antrian (queue) menggunakan bahasa Python

class ArrayListAntrian:
    def __init__(self):
        self.data = []  # Inisialisasi antrian sebagai list kosong

    def tambahData(self, item):
        self.data.append(item)
        
    def hapusData(self, item):
        # Mengecek apakah data merupakan urutan pertama
        if len(self.data) > 0 and self.data[0] == item:
            self.data.pop(0)
            print(f"Data '{item}' berhasil dihapus dari antrian.")
            
        elif len(self.data) > 0:
            # Mencari urutan data yang ingin dihapus
            for i in range(len(self.data)):
                if self.data[i] == item:
                    urutanData = i
                    print(f"Data '{item}' tidak bisa dihapus karena data tersebut berada di urutan ke-{urutanData + 1}.")
                    return None
            else:
                print(f"Data '{item}' tidak ditemukan dalam antrian.")
                return None
            
        else:
            print("Antrian kosong, tidak ada data yang dapat dihapus.")
            return None

    def tampilkanData(self, urutkan=False):
        dataTampil = self.data.copy()  # Membuat salinan data untuk ditampilkan
        
        if urutkan:
            #mengurutkan data dalam antrian tak peduli kapital huruf
            dataTampil.sort(key=lambda x: x.lower())
        
        if len(dataTampil) > 0:
            print("Data dalam antrian:")
            for i in range(len(dataTampil)):
                if i != len(dataTampil) - 1:
                    print(f"{dataTampil[i]} - ", end="")
                else:
                    print(f"{dataTampil[i]}.")
        else:
            print("Antrian kosong.")
            
    def lihatAntrianAwal(self):
        if len(self.data) > 0:
            print("Data awal dalam antrian:")
            print(self.data[0])
        else:
            print("Antrian kosong.")
            
    def lihatAntrianAkhir(self):
        if len(self.data) > 0:
            print("Data akhir dalam antrian:")
            print(self.data[-1])
        else:
            print("Antrian kosong.")
            
    def mencariData(self, item):
        for i in range(len(self.data)):
            if self.data[i] == item:
                urutanData = i
        
        if item in self.data:
            print(f"Data '{item}' ditemukan dalam antrian urutan ke-{urutanData + 1}.")
        else:
            print(f"Data '{item}' tidak ditemukan dalam antrian.")
            
    def jumlahAntrian(self):
        return len(self.data)

# Program utama

contohData = ArrayListAntrian()  # Membuat objek antrian

ulang = True

# Membuat kondisi untuk mengulangi program
while ulang == True:  
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Melihat Antrian Awal")
    print("5. Melihat Antrian Akhir")
    print("6. Mencari Data")
    print("7. Jumlah Antrian")
    print("8. Keluar")
    
    # Menggunakan input untuk pengguna memilih menu
    pilihan = (input("Silahkan pilih (1, 2, 3, atau 4) lalu Enter: "))

    # Menambahkan data ke dalam antrian
    if pilihan == '1':
        dataBaru = input("Masukkan data yang ingin anda tambahkan: ")
        # Memisahkan data jika ada koma
        dataBaru = dataBaru.split(",")
        for item in dataBaru:
            contohData.tambahData(item.strip()) # (Strip) Menghapus spasi di awal dan akhir
        print("Data berhasil ditambahkan.")
        print()
        
    # Menghapus data dari antrian
    elif pilihan == '2':
        dataHapus = input("Masukkan data yang ingin anda hapus: ")
        contohData.hapusData(dataHapus.strip()) # (Strip) Menghapus spasi di awal dan akhir
        print()
        
    # Menampilkan data dalam antrian
    elif pilihan == '3':
        urutkan = input("Apakah Anda ingin menampilkan data yang sudah terurut? (y/n): ").lower()
        if urutkan == 'y':
            contohData.tampilkanData(urutkan=True)
        else:
            contohData.tampilkanData()
        print()
    
    # Melihat data awal dalam antrian 
    elif pilihan == '4':
        contohData.lihatAntrianAwal()
        print()
       
    # Melihat data akhir dalam antrian 
    elif pilihan == '5':
        contohData.lihatAntrianAkhir()
        print()
        
    # Mencari data dalam antrian
    elif pilihan == '6':
        dataCari = input("Masukkan data yang ingin anda cari: ")
        contohData.mencariData(dataCari.strip())
        print()
        
    # Menampilkan jumlah antrian
    elif pilihan == '7':
        dataJumlah = contohData.jumlahAntrian()
        print(f"Jumlah antrian saat ini: {dataJumlah}")
        print()
        
    # Keluar dari program
    elif pilihan == '8':
        print("Data akhir dalam antrian:")
        # Menampilkan data dalam antrian
        contohData.tampilkanData()
        
        # Menggunakan ternary operator untuk menanyakan kepada pengguna apakah ingin mencoba lagi
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        ulang = True if ulang == 'y' else False
        if ulang == True:
            # Mengulangi program dan menghapus data dalam antrian
            contohData.data.clear()
            print("Data dalam antrian telah dihapus.")
            print("mengulang program...")
            print()
            
        else:
            print("Terima kasih telah menggunakan program ini.")
            print()
        
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")
        print()