# Membuat program Linked List Ganda dengan menggunakan bahasa Python

# Membuat simpul atau daun untuk Linked List yang menyimpan data serta pointer ke simpul berikutnya dan sebelumnya
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Membuat class Linked List Ganda untuk menyimpan data
class DoubleLinkedList:
    # Inisialisasi linked list dengan head(simpul pertama) dan tail(simpul terakhir) yang kosong
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Fungsi untuk menambahkan data ke dalam linked list ganda di bagian depan     
    def insertFirst(self, data):
        simpulBaru = Node(data) 
        # Jika linked list kosong, maka simpul baru menjadi head dan tail
        if self.head == None:
            self.head = simpulBaru
            self.tail = simpulBaru
        # Menambahkan simpul baru ke dalam linked list yang sudah ada
        else:
            simpulBaru.next = self.head
            self.head.prev = simpulBaru
            self.head = simpulBaru
    
    # Fungsi untuk menambahkan data ke dalam linked list ganda di bagian belakang
    def insertLast(self, data):
        simpulBaru = Node(data) 
        # Jika linked list kosong, maka simpul baru menjadi head dan tail
        if self.head == None: 
            self.head = simpulBaru
            self.tail = simpulBaru
        # Menambahkan simpul baru ke dalam linked list yang sudah ada
        else:
            self.tail.next = simpulBaru
            simpulBaru.prev = self.tail
            self.tail = simpulBaru
    
    # Fungsi untuk menambahkan data ke dalam linked list ganda setelah node/simpul tertentu
    def insertAfter(self, prevNode, data):
        # Jika linked list kosong
        if self.head == None:
            print("Linked list kosong")
            return
        current = self.head
        
        # Mencari node sebelumnya
        while current != None:
            if current.data == prevNode:
                break
            current = current.next
        if current == None:
            print("Node sebelumnya tidak ditemukan")
        
        # Menyisipkan node baru setelah posisi node sebelumnya ditemukan
        simpulBaru = Node(data)
        simpulBaru.next = current.next
        simpulBaru.prev = current
        if current.next != None:
            current.next.prev = simpulBaru
        current.next = simpulBaru
        if simpulBaru.next == None:
            self.tail = simpulBaru
        else:
            simpulBaru.next.prev = simpulBaru
    
    # Fungsi untuk menghapus data dari linked list ganda di bagian depan
    def removeFirst(self):
        if self.head == None:
            print("Linked list kosong")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    # Fungsi untuk menghapus data dari linked list ganda di bagian belakang
    def removeLast(self):
        if self.head == None:
            print("Linked list kosong")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    # Fungsi untuk menghapus data dari linked list ganda berdasarkan yang diberikan (key)
    def removeKey(self, key):
        if self.head == None:
            print("Linked list kosong")
            return
        current = self.head
        while current != None:
            if current.data == key:
                if current == self.head:
                    self.removeFirst()
                elif current == self.tail:
                    self.removeLast()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        print("Data yang ingin dihapus tidak ditemukan")
    
    # Fungsi untuk menampilkan data dalam linked list ganda dari kiri ke kanan
    def displayForward(self):
        print("Menampilkan data dari kiri ke kanan:")
        if self.head == None:
            print("Linked list kosong")
            return
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()
    
    # Fungsi untuk menampilkan data dalam linked list ganda dari kanan ke kiri
    def displayBackward(self):
        print("Menampilkan data dari kanan ke kiri:")
        if self.tail == None:
            print("Linked list kosong")
            return
        current = self.tail
        while current != None:
            print(current.data, end=" ")
            current = current.prev
        print()
        
# Program Utama
dll = DoubleLinkedList()

ulang = True

while ulang == True:
    print("Menu:")
    print("1. Tambah Data Depan")
    print("2. Tambah Data Belakang")
    print("3. Tambah Data Setelah Node Tertentu")
    print("4. Hapus Data Depan")
    print("5. Hapus Data Belakang")
    print("6. Hapus Data Tertentu")
    print("7. Tampilkan Data dari Kiri ke Kanan")
    print("8. Tampilkan Data dari Kanan ke Kiri")
    print("9. Selesai")

    # Menggunakan input untuk pengguna memilih menu
    pilihan = (input("Masukkan pilihan Anda: "))

    # Pilihan pengguna untuk menambahkan, menghapus, atau menampilkan data
    if pilihan == '1':
        data = input("Masukkan data yang ingin ditambahkan di depan: ")
        dll.insertFirst(data)
        
    elif pilihan == '2':
        data = input("Masukkan data yang ingin ditambahkan di belakang: ")
        dll.insertLast(data)
        
    elif pilihan == '3':
        prevNode = input("Masukkan data node sebelumnya: ")
        data = input("Masukkan data yang ingin ditambahkan setelah node tersebut: ")
        dll.insertAfter(prevNode, data)
        
    elif pilihan == '4':
        dll.removeFirst()
        
    elif pilihan == '5':
        dll.removeLast()
        
    elif pilihan == '6':
        key = input("Masukkan data yang ingin dihapus: ")
        dll.removeKey(key)
        
    elif pilihan == '7':
        dll.displayForward()
        
    elif pilihan == '8':
        dll.displayBackward()
        
    elif pilihan == '9':
        print("Terima kasih telah menggunakan program ini.")
        # Menanyakan pengguna apakah ingin mencoba lagi menggunakan ternary operator
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        ulang = True if ulang == 'y' else False
        if ulang == True:
            dll = DoubleLinkedList()
            print("Data diulang.")
            print()
        else:
            print("Program selesai.")
            print()
            
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.")
    print()