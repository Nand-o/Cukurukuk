def selection_sort(data, mode='1'):
    n = len(data)
    print("\nData awal:", "; ".join(map(str, data)) + ";")

    for pos_awal in range(n - 1):
        print(f"\nTahap ke-{pos_awal+1}:")
        pos_min = pos_awal
        for j in range(pos_awal + 1, n):
            print(f"  Iterasi ke-{j - pos_awal}: membandingkan {data[pos_min]} dan {data[j]}", end="")

            if (mode == '1' and data[pos_min] > data[j]) or (mode == '2' and data[pos_min] < data[j]):
                pos_min = j
                print(f" -> {data[pos_min]} lebih {'kecil' if mode == '1' else 'besar'}, jadi dipilih")
            else:
                print(" -> tidak dipilih")

        if pos_awal != pos_min:
            data[pos_awal], data[pos_min] = data[pos_min], data[pos_awal]
            print(f"  Tukar elemen: {data[pos_min]} dengan {data[pos_awal]}")
        else:
            print("  Tidak perlu tukar elemen")

        print("  " + "; ".join(map(str, data)) + ";")

    print("\nData sudah terurut.")
    hasil = "; ".join(map(str, data)) + ";"
    print(f"\nHasil akhir ({'menaik' if mode == '1' else 'menurun'}): {hasil}")


# Program utama
while True:
    print("\nProgram Selection Sort")
    print("Pilih metode input atau (3) jika ingin keluar:")
    print("1. Masukkan jumlah data")
    print("2. Masukkan data bebas ('selesai' untuk berhenti)")
    print("3. Exit")
    pilihan = input("Pilihan (1/2/3): ")


    data = []
    if pilihan == '1':
        jumlah = int(input("Jumlah data: "))
        for i in range(jumlah):
            angka = int(input(f"Data ke-{i+1}: "))
            data.append(angka)
    elif pilihan == '2':
        while True:
            masukan = input("Masukkan data (atau ketik 'selesai'): ")
            if masukan.lower() == 'selesai':
                break
            data.append(int(masukan))
    elif pilihan == '3':
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid.")
        continue

    print("\nPilih mode pengurutan:")
    print("1. Menaik")
    print("2. Menurun")
    print("3. Keduanya")
    mode = input("Pilihan (1/2): ")
    if mode == '1' or mode == '2':
        selection_sort(data.copy(), mode)
    elif mode == '3':
        print("\n Mode Menaik ")
        selection_sort(data.copy(), '1')
        print("\n Mode Menurun ")
        selection_sort(data.copy(), '2')
    else:
        print("Pilihan tidak valid.")
        continue

    lanjut = input("\nIngin lanjut? (y/n): ")
    if lanjut.lower() != 'y':
        break