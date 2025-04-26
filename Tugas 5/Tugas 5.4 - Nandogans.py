# Menggunakan algoritma Quick Sort untuk mengurutkan array


# Fungsi quickSort untuk mengurutkan array
def quickSort(arr, indexAwal, indexAkhir):
    if indexAwal < indexAkhir:
        # Memanggil fungsi partisi untuk membagi array
        indexPivot = partition(arr, indexAwal, indexAkhir)
        # Mengurutkan bagian kiri dan kanan dari pivot
        quickSort(arr, indexAwal, indexPivot - 1)
        quickSort(arr, indexPivot + 1, indexAkhir)


# Fungsi partisi untuk membagi array menjadi dua bagian
def partition(arr, indexAwal, indexAkhir):
    # Memilih elemen terakhir sebagai pivot
    pivot = arr[indexAkhir]

    # Inisialisasi index untuk elemen yang lebih kecil dari pivot
    i = indexAwal - 1

    # Melakukan partisi array
    for j in range(indexAwal, indexAkhir):
        if arr[j] <= pivot:
            i += 1
            # Menukar posisi arr[i] dan arr[j] dengan temporary variable
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    # Menukar posisi arr[i + 1] dan arr[indexAkhir] dengan temporary variable
    temp = arr[i + 1]
    arr[i + 1] = arr[indexAkhir]
    arr[indexAkhir] = temp
    return i + 1


# Program utama

ulang = True

data = []

while ulang == True:
    dataBaru = input("Masukkan data baru: ")
    # Memisahkan data jika ada koma
    dataBaru = dataBaru.split(",")
    for item in dataBaru:
        data.append(int(item.strip()))  # (Strip) Menghapus spasi di awal dan akhir
    print("Data berhasil ditambahkan.")
    print()

    print("Data awal:")
    print(data)
    quickSort(data, 0, len(data) - 1)
    print("Data setelah diurutkan dengan Quick Sort:")
    print(data)

    # Menanyakan pengguna untuk mengulangi program
    ulang = input("Apakah Anda ingin mengulangi program? (y/n): ").lower()
    ulang = True if ulang == "y" else False
    if ulang == True:
        data = []
        print("Data diulang.")
        print()
    else:
        print("Terima kasih telah menggunakan program ini.")
        print()
