class dataKota:
    def __init__(self):
        self.maksimalData = int(input("Jumlah data yang diinginkan : "))
        self.jumlahKota = 0
        self.kota = []
        self.history = []

    def tambahData(self, kotaBaru):
        if self.jumlahKota == self.maksimalData:
            print('Data sudah penuh')
            return False
        posisi = -1
        for i in range(self.jumlahKota):
            if kotaBaru == self.kota[i]:
                print('Data sudah ada')
                return False
            elif kotaBaru < self.kota[i]:
                posisi = i
                break 
        if posisi == -1:
            self.kota.append(kotaBaru)
        else:
            self.kota.append("")
            for i in range(self.jumlahKota, posisi, -1):
                self.kota[i] = self.kota[i-1]
            self.kota[posisi] = kotaBaru
        self.jumlahKota += 1
        if kotaBaru not in self.history:
            self.history.append(kotaBaru)
        return True

    def hapusData(self, kotaX):
        posisi = -1
        for i in range(0, self.jumlahKota):
            # Mencari posisi data
            if kotaX == self.kota[i] :
                posisi = i
                break
        if posisi == -1:
            if kotaX in self.history:
                print('Data sudah pernah dihapus')
            else:
                print('Data tidak ditemukan')
            return False
        # Penghapusan Kota
        for i in range(posisi+1, self.jumlahKota):
            self.kota[i-1] = self.kota[i]
        self.kota.pop()
        self.jumlahKota-=1

    def tampilkanData(self):
        print("Kota : ")
        if not self.kota:
            print("Data kota masih kosong")
        else:
            for i in range(len(self.kota)):
                if i == len(self.kota) - 1:
                    print(self.kota[i])
                else:
                    print(self.kota[i], end=" - ")

def menu():
    data = dataKota()
    while True:
        print("====== MENU ======")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data")
        print("4. Selesai")
        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
        except ValueError:
            print("\nInput harus berupa angka\n")
            continue
        match pilihan:
            case 1 :
                print('Penambahan data. \nKota : ')
                kotaX = input('').strip()
                if not data.tambahData(kotaX):
                    continue
            case 2 :
                print('Penghapusan Data. \nKota : ')
                kotaX = input('').strip()
                data.hapusData(kotaX)
            case 3 :
                data.tampilkanData()
            case 4 : 
                print('Program Selesai')
                break

menu()