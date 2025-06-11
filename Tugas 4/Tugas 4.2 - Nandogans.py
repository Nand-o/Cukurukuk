# Membuat aplikasi algoritma sorting Insertion Sort dengan array

# Function
def printData(data):
    for item in data:
        # jika data adalah bilangan bulat dalam type float, tampilkan dengan format yang sesuai
        if item == int(item):
            print(f"{int(item)}", end=", " if item != data[-1] else "\n")
        else:
            print(f"{item:.2f}", end=", " if item != data[-1] else "\n")
    print()

def insertionSort(data, ascending=True):
    if len(data) == 0:
        print("Data kosong, tidak ada yang bisa diurutkan.")
        return
    
    if ascending:
        print("Mengurutkan data secara menaik...")
        print("Data awal:")
        printData(data)
            
        for i in range(1, len(data)):
            key = data[i]  # Elemen yang akan diposisikan
            j = i - 1     # Index elemen sebelumnya
            
            print("=================================================")
            print(f"Tahap ke-{i}")
            print(f"Array saat ini:", end=" ")
            printData(data)
            print(f"Elemen yang akan disisipkan: {key}")
            
            # Geser elemen yang lebih besar dari key ke kanan
            perbandingan = 0
            while j >= 0:
                perbandingan += 1
                print(f"  Perbandingan {perbandingan}: {data[j]} vs {key}")
                
                if data[j] > key:
                    print(f"    {data[j]} > {key} = True, geser {data[j]} ke kanan")
                    data[j + 1] = data[j]  # Geser ke kanan
                    data[j] = key  # Tempatkan key pada posisi yang tepat
                    print(f"    Array setelah geser:", end=" ")
                    printData(data)
                    j -= 1
                else:
                    print(f"    {data[j]} > {key} = False, berhenti")
                    break
        
            # Tempatkan key pada posisi yang tepat
            data[j + 1] = key
            print(f"  Sisipkan {key} pada index {j + 1}")
            
            print()
            print(f"Data yang sudah terurut dari indeks 0 sampai {i} yaitu", end=" ")
            printData(data[0:i + 1])
            # Menampilkan data sementara yang sudah terurut
            print('Hasil sorting sementara:', end=" ") 
            printData(data)
            
    else:
        print("Mengurutkan data secara menurun...")
        print("Data awal:")
        printData(data)
        
        for i in range(1, len(data)):
            key = data[i]  # Elemen yang akan diposisikan
            j = i - 1     # Index elemen sebelumnya
            
            print("=================================================")
            print(f"Tahap ke-{i}")
            print(f"Array saat ini:", end=" ")
            printData(data)
            print(f"Elemen yang akan disisipkan: {key}")
            
            # Geser elemen yang lebih besar dari key ke kanan
            perbandingan = 0
            while j >= 0:
                perbandingan += 1
                print(f"  Perbandingan {perbandingan}: {data[j]} vs {key}")
                
                if data[j] < key:
                    print(f"    {data[j]} < {key} = True, geser {data[j]} ke kanan")
                    data[j + 1] = data[j]  # Geser ke kanan
                    data[j] = key  # Tempatkan key pada posisi yang tepat
                    print(f"    Array setelah geser:", end=" ")
                    printData(data)
                    j -= 1
                else:
                    print(f"    {data[j]} < {key} = False, berhenti")
                    break
        
            # Tempatkan key pada posisi yang tepat
            data[j + 1] = key
            print(f"  Sisipkan {key} pada index {j + 1}")
            
            print()
            print(f"Data yang sudah terurut dari indeks 0 sampai {i} yaitu", end=" ")
            printData(data[0:i + 1])
            # Menampilkan data sementara yang sudah terurut
            print('Hasil sorting sementara:', end=" ") 
            printData(data)
        
    # Menampilkan hasil sorting
    print("Hasil akhir sorting menggunakan Insertion Sort:")
    printData(data)
    

# Program utama
ulang = True

data = []

while ulang == True:
    print("Menu Insertion Sort")
    print("1. Tambah data")
    print("2. Lihat data awal")
    print("3. Urutkan data")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan (1-4): ")
    
    if pilihan == '1':
        dataBaru = (input("Masukkan data baru (pisahkan dengan koma): "))
        # Memisahkan data jika ada koma
        dataBaru = dataBaru.split(",")
        for item in dataBaru:
            data.append(float(item.strip())) # Strip Menghapus spasi di awal dan akhir
        print("Data berhasil ditambahkan.")
        print()
    
    elif pilihan == '2':
        if len(data) > 0:
            print("Data saat ini:")
            printData(data)
        else:
            print("Tidak ada data yang tersedia.")
        print()
        
    elif pilihan == '3':
        print()
        print("Pilihan pengurutan:")
        print("1. Urutkan secara menaik")
        print("2. Urutkan secara menurun")
        print("3. Urutkan secara hybrid (menaik dan menurun)")
        print("4. Kembali ke menu utama")
        
        pilihanUrut = input("Masukkan pilihan (1-4): ")
        if pilihanUrut == '1':
            dataMenaik = data.copy()
            insertionSort(dataMenaik, ascending=True)
            
        elif pilihanUrut == '2':
            dataMenurun = data.copy()
            insertionSort(dataMenurun, ascending=False)
            
        elif pilihanUrut == '3':
            print("Mengurutkan data secara hybrid...")
            print()
            # Mengurutkan secara menaik
            dataMenaik = data.copy()
            insertionSort(dataMenaik, ascending=True)
            
            # Mengurutkan secara menurun
            dataMenurun = data.copy()
            insertionSort(dataMenurun, ascending=False)
            
            print("==========================================")
            print("Data yang sudah diurutkan secara hybrid (menaik dan menurun):")
            print("Data menaik:", end=" ")
            printData(dataMenaik)
            print("Data menurun:", end=" ")
            printData(dataMenurun)
    
        elif pilihanUrut == '4':
            print("Kembali ke menu utama.")
            print()
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            print()
            
    elif pilihan == '4':
        # Menanyakan pengguna untuk mengulangi program
        ulang = input("Apakah Anda ingin mengulangi program? (y/n): ").lower()
        ulang = True if ulang == 'y' else False
        if ulang == True:
            data = []
            print("Data diulang.")
            print()
        else:
            print("Terima kasih telah menggunakan program ini.")
            print()
            
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        print()