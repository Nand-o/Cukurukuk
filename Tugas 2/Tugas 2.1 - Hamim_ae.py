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

    def dequeue(self):
        if self.is_kosong():
            print("Antrian kosong")
            return None
        else:
            self.depan = (self.depan + 1) % self.kapasitas
            return self.data[self.depan]

# Program utamanya
def main():
    while True:
        print("\nPilih jenis antrian:")
        print("1. Antrian Kapasitas Terbatas")
        print("2. Antrian Tak Terbatas (deque)")
        print("3. Exit")
        pilihan = input("Masukkan pilihan (1, 2 atau 3): ")

        if pilihan == "1":
            kapasitas = int(input("Masukkan maksimal antriannya: "))
            nama_nama = []
            print(f"Masukkan {kapasitas} nama peserta antrian:")
            for i in range(kapasitas):
                data = input(f"Nama ke-{i+1}: ")
                nama_nama.append(data)

            antrian = AntrianTerbatas(kapasitas + 1)  # Tambah 1 slot untuk circular queue
            for nama in nama_nama:
                antrian.enqueue(nama)

            print("\nIsi Antrian (Kapasitas Terbatas):")
            while not antrian.is_kosong():
                print(antrian.dequeue())

        elif pilihan == "2":
            print("Masukkan nama peserta antrian (ketik 'selesai' untuk berhenti):")
            antrian = deque()
            i = 1
            while True:
                data = input(f"Nama ke-{i}: ")
                if data.lower() == 'selesai':
                    break
                antrian.append(data)
                i += 1

            print("\nIsi Antrian (Tak Terbatas):")
            while antrian:
                print(antrian.popleft())


        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
