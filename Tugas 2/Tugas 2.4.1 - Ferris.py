class Node:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama
        self.next = None

    def display(self):
        print(f"{self.kode} : {self.nama}")

class SenaraiBerantai:
    def __init__(self):
        self.head = None

    def insert(self, kode, nama):
        new_node = Node(kode, nama)
        new_node.next = self.head
        self.head = new_node

    def find(self, kode):
        current = self.head
        while current:
            if current.kode == kode:
                return current
            current = current.next
        return None

    def remove(self, kode):
        current = self.head
        prev = None
        while current:
            if current.kode == kode:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def display_all(self):
        print("\nIsi senarai berantai:")
        current = self.head
        if not current:
            print("Senarai kosong.")
        while current:
            current.display()
            current = current.next

    def is_empty(self):
        return self.head is None

def main():
    sb = SenaraiBerantai()
    while True:
        print("\n=== Menu Senarai Berantai (Pilih Angka Secara Manual lalu Enter) ===")
        print("1. Insert data")
        print("2. Cari data")
        print("3. Hapus data")
        print("4. Tampilkan semua")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kode = input("Masukkan kode: ").upper()
            nama = input("Masukkan nama: ")
            sb.insert(kode, nama)
        elif pilihan == "2":
            if sb.is_empty():
                print("Senarai kosong, Tidak ada yang bisa dicari!")
            else:
                kode = input("Masukkan kode yang dicari: ").upper()
                hasil = sb.find(kode)
                if hasil:
                    print("Data ditemukan:")
                    hasil.display()
                else:
                    print("Data tidak ditemukan.")
        elif pilihan == "3":
            if sb.is_empty():
                print("Senarai kosong, Tidak ada yang bisa dihapus!")
            else:
                kode = input("Masukkan kode yang ingin dihapus: ").upper()
                if sb.remove(kode):
                    print("Data berhasil dihapus.")
                else:
                    print("Data tidak ditemukan.")
        elif pilihan == "4":
            sb.display_all()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak ada!")

if __name__ == "__main__":
    main()
