class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"({self.key}: {self.value})"

class TabelHash:
    # Inisialisasi tabel hash
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    # Fungsi hash sederhana yang menggunakan modulus untuk menghitung indeks
    def fungsiHash(self, key):
        # Jika key adalah string, gunakan sum dari ASCII
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        # Jika key adalah angka, gunakan key itu sendiri
        elif not isinstance(key, int):
            print("Key harus berupa string atau integer")
            return None
        
        return key % self.size
    
    # Fungsi untuk menyisipkan data dengan menggunakan key ke dalam tabel hash
    def insert(self, key, value):
        # Hitung indeks menggunakan fungsi hash
        index = self.fungsiHash(key)
        print(f"Index untuk key '{key}' adalah {index}")
        
        # Cek apakah slot kosong
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Slot tidak kosong, terjadi tabrakan hash (collision), mengatasi dengan pembentukan rantai (chaining)
            print(f"Tabrakan Hash terjadi pada index {index}, menggunakan metode Pembentukan Rantai (Chaining)")
            # Periksa apakah key sudah ada pada rantai
            current = self.table[index]
            while current:
                # Jika key sudah ada, update value
                if current.key == key:
                    current.value = value
                    return
                # Jika mencapai akhir rantai dan key tidak ditemukan
                if current.next is None:
                    break
                current = current.next
            
            # Tambahkan node baru di akhir rantai
            current.next = Node(key, value)
        
        self.count += 1
    
    # Fungsi untuk mengecek apakah ada data yang dicari pada tabel hash
    def get(self, key):
        index = self.fungsiHash(key)
        
        # Jika slot kosong, key tidak ada
        if self.table[index] is None:
            return None
        
        # Telusuri rantai untuk mencari key
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        # Data tidak ditemukan
        return None
    
    # Fungsi untuk menghapus data dari tabel hash
    def remove(self, key):
        index = self.fungsiHash(key)
        
        # Jika slot kosong, key tidak ada
        if self.table[index] is None:
            return False
        
        # Jika node pertama memiliki key yang dicari
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            self.count -= 1
            return True
        
        # Telusuri rantai untuk mencari key
        current = self.table[index]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                self.count -= 1
                return True
            current = current.next
        
        return False
    
    # Fungsi untuk menampilkan isi tabel hash
    def display(self):
        print("Tabel Hash:")
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            if self.table[i] is None:
                print("None")
            else:
                current = self.table[i]
                while current:
                    print(current, end=" -> " if current.next else "\n")
                    current = current.next
    
    # Fungsi untuk mencari key berdasarkan value
    def searchKey(self, value):
        for i in range(self.size):
            current = self.table[i]
            while current:
                if current.value == value:
                    return current.key
                current = current.next
        return None