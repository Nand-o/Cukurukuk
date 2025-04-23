# Membuat aplikasi algoritma sorting Insertion Sort dengan array

# Function
def printData(data):
    for item in range(len(data)):
        if item != len(data) - 1:
            print(f'{data[item]}, ', end="")
        else:
            print(data[item])
    print()

def insertionSort(data):
    print("Data awal:")
    printData(data)

    for i in range(1, len(data)):
        dataSementara = data[i]
        j = i - 1
        while j >= 0 and dataSementara < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = dataSementara
        
        print(f"Tahap ke-{i}")
        print(f"Data yang sudah terurut dari indeks 0 sampai {i} yaitu {data[0:i + 1]}")
        
        # Menampilkan data yang sudah terurut
        print('Hasil sorting sementara:', end=" ")
        printData(data)
        
    # Menampilkan hasil sorting
    print("Hasil akhir sorting menggunakan Insertion Sort:")
    printData(data)
    

# Program utama
ulang = True

data = []

while ulang == True:
    dataBaru = (input("Masukkan data baru: "))
    # Memisahkan data jika ada koma
    dataBaru = dataBaru.split(",")
    for item in dataBaru:
        data.append(int(item.strip())) # (Strip) Menghapus spasi di awal dan akhir
    print("Data berhasil ditambahkan.")
    print()
    
    insertionSort(data)
    
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