class Simpul:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def display(self):
        print(f"{self.kode} : {self.nama}")

def hapus(senarai, kode):
    posisi = -1
    for i in range(len(senarai)):
        if senarai[i].kode == kode:
            posisi = i
            break
    if posisi != -1:
        del senarai[posisi]
    else:
        print(f"{kode} tidak dapat dihapus.")

def cari(senarai, kode):
    for simpul in senarai:
        if simpul.kode == kode:
            return simpul
    return None

# Main
senarai = []
senarai.insert(0, Simpul("CDR", "Candra"))
senarai.insert(0, Simpul("HMM", "Hamim"))
senarai.insert(0, Simpul("NDN", "Nando"))
senarai.insert(0, Simpul("FRS", "Faris"))

print("Keadaan awal:")
for simpul in senarai:
    simpul.display()

hapus(senarai, "NDN")

print("\nSetelah NDN dihapus:")
for simpul in senarai:
    simpul.display()

kode_dicari = "NDN"
print(f"\nPencarian {kode_dicari}:")
hasil = cari(senarai, kode_dicari)
if hasil:
    print("Hasil pencarian:")
    hasil.display()
else:
    print(f"{kode_dicari} tidak ditemukan.")

kode_dicari = "HMM"
print(f"\nPencarian {kode_dicari}:")
hasil = cari(senarai, kode_dicari)
if hasil:
    print("Hasil pencarian:")
    hasil.display()
else:
    print(f"{kode_dicari} tidak ditemukan.")