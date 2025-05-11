class ContohStack :
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def print_stack(self):
        if not self.stack:
            print("Stack kosong")
        else:
            print("\nIsi stack :")
            for item in self.stack:
                print(item)

def main(): 
    stack = ContohStack()

    jumlah_stack = int(input("Masukkan jumlah yang ingin dimasukkan ke stack : "))

    for i in range(jumlah_stack) :
       nama = input(f"Masukkan nama ke-{i+1}: ")
       stack.push(nama)
       
    stack.print_stack()
    
if __name__ == "__main__":
    main()