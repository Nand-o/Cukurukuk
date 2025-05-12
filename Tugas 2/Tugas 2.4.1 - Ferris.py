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

    def display(self):
        print("Isi Senarai Berantai : ")
        current = self.head
        while current:
            current.display()
            current = current.next

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
        print("Data yang akan dihapus tidak ditemukan!")
        return False

sb = SenaraiBerantai()
sb.insert("CDR", "Candra")
sb.insert("HMM", "Hamim")
sb.insert("NDN", "Nando")
sb.insert("FRS", "Faris")

print("Keadaan awal:")
sb.display()

print("\nSetelah NDN dihapus:")
sb.remove("NDN")
sb.display()

kode_dicari = "NDN"
print(f"\nPencarian {kode_dicari}:")
hasil = sb.find(kode_dicari)
if hasil:
    hasil.display()
else:
    print(f"{kode_dicari} tidak ditemukan.")

kode_dicari = "HMM"
print(f"\nPencarian {kode_dicari}:")
hasil = sb.find(kode_dicari)
if hasil:
    hasil.display()
else:
    print(f"{kode_dicari} tidak ditemukan.")