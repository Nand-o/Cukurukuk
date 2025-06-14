from collections import deque

class AntrianTerbatas:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.data = [None] * kapasitas
        self.depan = 0
        self.belakang = 0

    def is_penuh(self):
        return (self.belakang + 1) % self.kapasitas == self.depan

    def is_kosong(self):
        return self.depan == self.belakang

    def enqueue(self, item):
        if self.is_penuh():
            print("Antrian penuh, tidak bisa menambahkan:", item)
        else:
            self.belakang = (self.belakang + 1) % self.kapasitas
            self.data[self.belakang] = item
            print(f"{item} masuk ke antrian.")

    def dequeue(self):
        if self.is_kosong():
            print("Antrian kosong.")
            return None
        else:
            self.depan = (self.depan + 1) % self.kapasitas
            keluar = self.data[self.depan]
            print(f"{keluar} dikeluarkan dari antrian (FIFO).")
            return keluar

    def remove(self, item):
        new_queue = AntrianTerbatas(self.kapasitas)
        found = False
        while not self.is_kosong():
            elemen = self.dequeue()
            if elemen == item and not found:
                found = True
                print(f"{item} berhasil dihapus dari antrian.")
            else:
                new_queue.enqueue(elemen)
        self.data = new_queue.data
        self.depan = new_queue.depan
        self.belakang = new_queue.belakang
        if not found:
            print(f"{item} tidak ditemukan dalam antrian.")

    def tampilkan(self):
        print("Isi antrian saat ini:")
        i = (self.depan + 1) % self.kapasitas
        while i != (self.belakang + 1) % self.kapasitas:
            print(self.data[i])
            i = (i + 1) % self.kapasitas


# ~ Program Utama
def main():
    print("Pilih jenis antrian yang ingin digunakan:")
    print("1. Antrian Terbatas (Circular Queue)")
    print("2. Antrian Tak Terbatas")
    jenis = input("Masukkan pilihan (1 atau 2): ")

    if jenis == "1":
        kapasitas = int(input("Masukkan kapasitas antrian terbatas: "))
        antrian = AntrianTerbatas(kapasitas + 1)
    elif jenis == "2":
        antrian = deque()
    else:
        print("Pilihan tidak valid.")
        return

    while True:
        print("\nMenu Antrian:")
        print("1. Tambah ke antrian (enqueue)")
        print("2. Keluarkan dari antrian (dequeue/ FIFO)")
        print("3. Hapus nama tertentu")
        print("4. Tampilkan isi antrian")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            if jenis == "1":
                antrian.enqueue(nama)
            else:
                antrian.append(nama)
                print(f"{nama} masuk ke antrian.")

        elif pilihan == "2":
            if jenis == "1":
                antrian.dequeue()
            else:
                if antrian:
                    print(f"{antrian.popleft()} dikeluarkan dari antrian (FIFO).")
                else:
                    print("Antrian kosong.")

        elif pilihan == "3":
            target = input("Masukkan nama yang ingin dihapus: ")
            if jenis == "1":
                antrian.remove(target)
            else:
                if target in antrian:
                    antrian.remove(target)
                    print(f"{target} berhasil dihapus dari antrian.")
                else:
                    print(f"{target} tidak ditemukan dalam antrian.")

        elif pilihan == "4":
            print("Isi antrian saat ini:")
            if jenis == "1":
                antrian.tampilkan()
            else:
                if not antrian:
                    print("(Kosong)")
                else:
                    for item in antrian:
                        print(item)

        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

# Udah dawg
