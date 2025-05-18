class ContohStack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None  # Ubah jadi None agar lebih fleksibel
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack kosong!"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def count(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()

    # def print_stack(self):
    #     if self.is_empty():
    #         print("Stack kosong!")
    #     else:
    #         for item in reversed(self.stack):
    #             print(item)

    def print_stack(self):
        if self.is_empty():
            print("Stack kosong!")
        else:
            for item in self.stack:
                print(item)

def main():
    stack = ContohStack()

    while True:
        print("\nSilakan pilih : ")
        print("1. Push (Tambah Item)")
        print("2. Pop (Hapus Item)")
        print("3. Peek (Lihat Item Terakhir)")
        print("4. Is Empty (Cek Apakah Stack Kosong)")
        print("5. Count (Jumlah Item)")
        print("6. Clear")
        print("7. Print Stack (Tampilkan Isi)")
        print("8. Exit")
        pilihan = input("Pilih: ")

        if pilihan == "1":
            try:
                jumlah = int(input("Berapa banyak data yang ingin dimasukkan? "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0.")
                    continue
                for i in range(jumlah):
                    data = input(f"Masukkan data ke-{i+1}: ")
                    stack.push(data)
                print(f"{jumlah} item berhasil dimasukkan.")
                print(f"Total item sekarang: {stack.count()}")
            except ValueError:
                print("Masukkan angka yang valid!")
        elif pilihan == "2":
            data = stack.pop()
            if data is None:
                print("Stack kosong! Tidak bisa menghapus apa apa.")
            else:
                print(f"Item '{data}' dihapus dari stack.")
                print(f"Total item sekarang: {stack.count()}")
        elif pilihan == "3":
            print("Item Terakhir:", stack.peek())
        elif pilihan == "4":
            print("Apakah Kosong?", stack.is_empty())
        elif pilihan == "5":
            print("Jumlah Item:", stack.count())
        elif pilihan == "6":
            stack.clear()
            print("Stack dikosongkan.")
        elif pilihan == "7":
            print("Isi Stack :")
            stack.print_stack()
        elif pilihan == "8":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
