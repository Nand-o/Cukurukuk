def custom_forward_insert_sort(data, ascending=True):
    steps = []
    for i in range(len(data)):
        selected_idx = i
        for j in range(i + 1, len(data)):
            if ascending:
                if data[j] < data[selected_idx]:
                    selected_idx = j
            else:
                if data[j] > data[selected_idx]:
                    selected_idx = j

        selected_val = data[selected_idx]
        for k in range(selected_idx, i, -1):
            data[k] = data[k - 1]
        data[i] = selected_val

        steps.append(data.copy())
    return steps


def input_manual():
    data = []
    print("Masukkan data satu per satu (ketik 'selesai' untuk mengakhiri):")
    while True:
        inp = input(f"Data ke-{len(data)+1}: ")
        if inp.lower() == "selesai":
            break
        try:
            data.append(float(inp))
        except ValueError:
            print("Harap masukkan angka atau 'selesai'.")
    return data


def input_jumlah():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah data: "))
            data = []
            for i in range(jumlah):
                angka = float(input(f"Data ke-{i+1}: "))
                data.append(angka)
            return data
        except ValueError:
            print("Input tidak valid, coba lagi.")


def main():
    while True:
        print("\nPilih metode input atau (3) jika ingin keluar:")
        print("1. Masukkan jumlah data")
        print("2. Masukkan data bebas ('selesai' untuk berhenti)")
        print("3. Exit")
        pilihan = input("Pilihan (1/2/3): ")

        if pilihan == '3':
            print("Keluar dari program.")
            break
        elif pilihan == '1':
            data = input_jumlah()
        elif pilihan == '2':
            data = input_manual()
        else:
            print("Pilihan tidak valid!")
            continue

        print("\nData yang dimasukkan:", data)
        print("\nPilih mode pengurutan:")
        print("1. Menaik")
        print("2. Menurun")
        print("3. Keduanya")
        mode = input("Pilihan (1/2/3): ")

        if mode == '1':
            print("\n=== Pengurutan Menaik ===")
            result = custom_forward_insert_sort(data.copy(), ascending=True)
            print("Input:", data)
            for i, step in enumerate(result):
                print(f"Step{i+1}:", step)
        elif mode == '2':
            print("\n=== Pengurutan Menurun ===")
            result = custom_forward_insert_sort(data.copy(), ascending=False)
            print("Input:", data)
            for i, step in enumerate(result):
                print(f"Step{i+1}:", step)
        elif mode == '3':
            print("\n=== Pengurutan Menaik ===")
            result_up = custom_forward_insert_sort(data.copy(), ascending=True)
            print("Input:", data)
            for i, step in enumerate(result_up):
                print(f"Step{i+1}:", step)
            print("\n=== Pengurutan Menurun ===")
            result_down = custom_forward_insert_sort(data.copy(), ascending=False)
            print("Input:", data)
            for i, step in enumerate(result_down):
                print(f"Step{i+1}:", step)
        else:
            print("Pilihan mode tidak valid.")


if __name__ == "__main__":
    main()
