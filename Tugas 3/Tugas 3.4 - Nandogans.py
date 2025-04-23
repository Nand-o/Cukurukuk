# Membuat program mengurutkan data menggunakan Linked List Class

# Membuat simpul atau daun untuk Linked List yang menyimpan data serta pointer ke simpul berikutnya
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Membuat class Linked List untuk menyimpan data dan mengatur urutan data
class LinkedList:
    # Inisialisasi linked list dengan head yang kosong
    def __init__(self):
        self.head = None

    # Fungsi untuk menambahkan data ke dalam linked list
    def insert(self, data):
        simpulBaru = Node(data) # Membuat simpul baru dengan data yang diberikan
        
        # Menambahkan simpul baru ke dalam linked list dengan urutan yang benar
        if self.head == None or self.head.data >= simpulBaru.data:
            simpulBaru.next = self.head 
            self.head = simpulBaru 
        else:
            current = self.head
            while current.next and current.next.data < simpulBaru.data: # Looping untuk mencari posisi yang tepat
                current = current.next
            simpulBaru.next = current.next
            current.next = simpulBaru

    # Fungsi untuk menghapus data dari linked list
    def remove(self, data):
        if self.head is None:
            return
        # Jika data yang ingin dihapus adalah data pertama
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        # Looping untuk mencari data yang ingin dihapus
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # Fungsi untuk menampilkan data dalam linked list
    def display(self):
        current = self.head
        if current == None:
            print("Antrian kosong.") # Jika linked list kosong
            return
        # Looping untuk menampilkan data dalam linked list
        while current:
            if current.next != None:
                print(f"{current.data} - ", end="")
            else:
                print(f"{current.data}.")
                print()
            current = current.next


# Program Utama

ulang = True
linkedList = LinkedList()

while ulang == True:
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")

    # Menggunakan input untuk pengguna memilih menu
    pilihan = (input("Pilihan menu (1, 2, 3, atau 4) lalu Enter: "))    

    # Menambahkan data ke dalam antrian
    if pilihan == '1':
        dataBaru = input("Masukkan data yang ingin ditambahkan: ")
        # Memisahkan data jika ada koma
        dataBaru = dataBaru.split(",")
        for item in dataBaru:
            linkedList.insert(f'{item.strip()}')
        print("Data berhasil ditambahkan.")
        print()

    # Menghapus data dari antrian
    elif pilihan == '2':
        dataHapus = input("Masukkan data yang ingin dihapus: ")
        linkedList.remove(dataHapus)
        print(f"Data '{dataHapus}' berhasil dihapus.")
        print()

    # Menampilkan data dalam antrian
    elif pilihan == '3':
        linkedList.display()

    # Keluar dari program
    elif pilihan == '4':
        print("Data akhir dalam antrian:")
        linkedList.display()
        linkedList.head = None
        print("Terima kasih telah menggunakan program ini.")
        
        # Menanyakan kepada pengguna apakah ingin mencoba lagi
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        ulang = True if ulang == 'y' else False
        print()

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")
        print()