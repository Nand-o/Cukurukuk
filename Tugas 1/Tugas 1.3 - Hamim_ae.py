max = int(input("Masukkan Maximum stack nya: "))
stack = []

while True:
    if len(stack) >= max:
        print("\nPilihan: pop | peek | tampil | exit")
    else:
        print("\nPilihan: push | pop | peek | tampil | exit")

    pilihan = input("Apa yang ingin kamu lakukan: ")

    if pilihan == "push":
        if len(stack) >= max:
            print("stack penuh, tidak bisa push!")
        else:
            data = input("Masukkan data yang ingin dipush: ")
            stack.append(data)
            print(f"{data} berhasil ditambahkan ke stack.")

    elif pilihan == "pop":
        if len(stack) == 0:
            print("Stack kosong, tidak bisa pop.")
        else:
            popped = stack.pop()
            print(f"{popped} berhasil dipop dari stack.")

    elif pilihan == "peek":
        if len(stack) == 0:
            print("Stack kosong.")
        else:
            print(f"Elemen paling atas: {stack[-1]}")

    elif pilihan == "tampil":
        print("Isi stack saat ini:", stack)

    elif pilihan == "exit":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak dikenal, coba lagi.")
