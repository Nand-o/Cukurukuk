print("=== Program Bubble Sort ===")

def format_angka(x):
    return str(int(x)) if x == int(x) else str(x).replace('.', ',')

def bubble_sort(data, mode):
    hasil = data.copy()
    n = len(hasil)
    print("\nData awal:", "; ".join(format_angka(x) for x in hasil))
    for i in range(n):
        print(f"\nTahap ke-{i+1}:")
        tukar = False
        for j in range(n - i - 1):
            a, b = format_angka(hasil[j]), format_angka(hasil[j+1])
            print(f"  Iterasi ke-{j+1}: membandingkan {a} dan {b}", end="")
            if (mode == 'a' and hasil[j] > hasil[j+1]) or (mode == 'd' and hasil[j] < hasil[j+1]):
                hasil[j], hasil[j+1] = hasil[j+1], hasil[j]
                tukar = True
                print(" -> ditukar")
            else:
                print(" -> tidak ditukar")
            print("   ", "; ".join(format_angka(x) for x in hasil))
        if not tukar:
            print("  Data sudah terurut.")
            break
    return hasil

while True:
    data = []
    print("\nPilih metode input atau (3) jika ingin keluar:")
    print("1. Masukkan jumlah data")
    print("2. Masukkan data bebas ('selesai' untuk berhenti)")
    print("3. Exit")
    metode = input("Pilihan (1/2/3): ")

    if metode == '1':
        try:
            n = int(input("Jumlah data: "))
            for i in range(n):
                while True:
                    try:
                        inp = input(f"Data ke-{i+1}: ").replace(',', '.')
                        data.append(float(inp))
                        break
                    except:
                        print("  Masukkan angka yang valid!")
        except:
            print("Jumlah tidak valid.")
            continue
    elif metode == '2':
        while True:
            inp = input(f"Data ke-{len(data)+1}: ").replace(',', '.')
            if inp.lower() == 'selesai': break
            try:
                data.append(float(inp))
            except:
                print("  Masukkan angka yang valid!")
    elif metode == '3':
        break;         
    else:
        print("Pilihan tidak valid.")
        continue

    if not data:
        print("Tidak ada data.")
        continue

    print("\nPilih mode pengurutan:")
    print("1. Menaik")
    print("2. Menurun")
    print("3. Keduanya")
    mode = input("Pilihan (1/2/3): ")

    if mode == '1':
        hasil_asc = bubble_sort(data, 'a')
        print("\nHasil akhir (menaik):", "; ".join(format_angka(x) for x in hasil_asc))
    elif mode == '2':
        hasil_desc = bubble_sort(data, 'd')
        print("\nHasil akhir (menurun):", "; ".join(format_angka(x) for x in hasil_desc))
    elif mode == '3':
        print("\n=== Proses Pengurutan Menaik ===")
        hasil_asc = bubble_sort(data, 'a')
        print("\n=== Proses Pengurutan Menurun ===")
        hasil_desc = bubble_sort(data, 'd')
        print("\nHasil akhir:")
        print("  - Menaik :", "; ".join(format_angka(x) for x in hasil_asc))
        print("  - Menurun:", "; ".join(format_angka(x) for x in hasil_desc))
    else:
        print("Pilihan mode tidak valid.")

    if input("\nIngin lanjut? (y/n): ").lower() != 'y':
        print("Terima kasih! Program selesai.")
        break