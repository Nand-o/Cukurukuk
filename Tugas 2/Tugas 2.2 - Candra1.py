kota = []
maksimalData = 10
jumlahKota = 0
kotaX = ''

def tambahData(kotaBaru):
    global kota, jumlahKota
    if jumlahKota == maksimalData:
        print('Data sudah penuh')
        return False
    posisi = -1
    for i in range(jumlahKota):
        if kotaBaru == kota[i]:
            print('Data sudah ada')
            return False
        elif kotaBaru < kota[i]:
            posisi = i
            break 
    if posisi == -1:
        kota.append(kotaBaru)
    else:
        kota.append("")
        for i in range(jumlahKota, posisi, -1):
            kota[i] = kota[i-1]
        kota[posisi] = kotaBaru
    jumlahKota += 1
    return True

def hapusData(kotaX):
    global kota, jumlahKota
    posisi = -1
    for i in range(0, jumlahKota):
        # Mencari posisi data
        if kotaX == kota[i] :
            posisi = i
            break
    if posisi == -1:
        print('Data tidak ditemukan')
        return False
    # Penghapusan Kota
    for i in range(posisi+1, jumlahKota):
        kota[i-1] = kota[i]
    kota.pop()
    jumlahKota-=1

def tampilkanData(kota):
    print("Kota : ")
    if not kota:
        print("Data kota masih kosong")
    else:
        for i in range(len(kota)):
            if i == len(kota) - 1:
                print(kota[i])
            else:
                print(kota[i], end=" - ")

def menu():
    while True:
        print("====== MENU ======")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data")
        print("4. Selesai")
        pilihan = int(input("Masukkan pilihan (1/2/3/4): "))   
        match pilihan:
            case 1 :
                print('Penambahan data. \nKota : ')
                kotaX = input('')
                if not tambahData(kotaX):
                    continue
            case 2 :
                print('Penghapusan Data. \nKota : ')
                kotaX = input('')
                hapusData(kotaX)
            case 3 :
                tampilkanData(kota)
            case 4 : 
                print('Program Selesai')
                break
menu()