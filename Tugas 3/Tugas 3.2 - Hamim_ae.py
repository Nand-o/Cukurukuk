class SimpulTumpukan:
    def __init__(self, data):
        self.data = data
        self.berikut = None

class ListTumpuk1:
    def __init__(self):
        self.puncak = None

    def push(self, data):
        ptrBaru = SimpulTumpukan(data)
        ptrBaru.berikut = self.puncak
        self.puncak = ptrBaru

    def empty(self):
        return self.puncak is None

    def pop(self):
        if self.empty():
            print("Tumpukan sudah kosong. Tidak bisa diambil lagi.")
            return None
        data = self.puncak.data
        self.puncak = self.puncak.berikut
        return data

    def peek(self):
        if self.empty():
            print("Tumpukan kosong.")
            return None
        return self.puncak.data

    def tampil(self):
        if self.empty():
            print("Tumpukan kosong.")
            return
        print("Isi tumpukan dari atas ke bawah:")
        current = self.puncak
        while current:
            print(current.data)
            current = current.berikut

# -------------------------
# Menu interaktif
# -------------------------
def menu():
    tumpukan = ListTumpuk1()

    while True:
        print("\n=== MENU TUMPUKAN ===")
        print("1. Push (Tambah data)")
        print("2. Pop (Ambil data)")
        print("3. Peek (Lihat data teratas)")
        print("4. Tampil semua isi tumpukan")
        print("5. Exit")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            data = input("Masukkan data (karakter): ")
            if data:
                tumpukan.push(data[0])  # Ambil karakter pertama saja
                print(f"'{data[0]}' berhasil ditambahkan ke tumpukan.")
        elif pilihan == '2':
            hasil = tumpukan.pop()
            if hasil is not None:
                print(f"Data '{hasil}' diambil dari tumpukan.")
        elif pilihan == '3':
            atas = tumpukan.peek()
            if atas is not None:
                print(f"Data teratas: '{atas}'")
        elif pilihan == '4':
            tumpukan.tampil()
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()
