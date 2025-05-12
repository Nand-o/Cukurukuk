class Simpul:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def display(self):
        print(f"{self.kode} : {self.nama}")

def cari(senarai, kode):
    for simpul in senarai:
        if simpul.kode == kode:
            return simpul
    return None

def hapus(senarai, kode):
    for i in range(len(senarai)):
        if senarai[i].kode == kode:
            del senarai[i]
            return True
    return False

def main():
    senarai = []
    while True:
        print("\n=== Menu Senarai Berantai (List Python) ===")
        print("1. Insert data")
        print("2. Cari data")
        print("3. Hapus data")
        print("4. Tampilkan semua")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            kode = input("Masukkan kode: ").upper()
            nama = input("Masukkan nama: ")
            senarai.insert(0, Simpul(kode, nama))  # seperti linked list (dari depan)
        elif pilihan == "2":
            if not senarai:
                print("Senarai kosong, Tidak ada yang bisa dicari!")
            else:
                kode = input("Masukkan kode yang dicari: ").upper()
                hasil = cari(senarai, kode)
                if hasil:
                    print("Data ditemukan:")
                    hasil.display()
                else:
                    print("Data tidak ditemukan.")
        elif pilihan == "3":
            if not senarai:
                print("Senarai kosong, Tidak ada yang bisa dihapus!")
            else:
                kode = input("Masukkan kode yang ingin dihapus: ").upper()
                if hapus(senarai, kode):
                    print("Data berhasil dihapus.")
                else:
                    print("Data tidak ditemukan.")
        elif pilihan == "4":
            print("\nIsi senarai:")
            if not senarai:
                print("Senarai kosong.")
            for simpul in senarai:
                simpul.display()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
