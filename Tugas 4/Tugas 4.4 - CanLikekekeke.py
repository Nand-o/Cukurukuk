class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printTree(node, indent="", is_left=True):
    if node is not None:
        printTree(node.right, indent + ("│   " if is_left else "    "), False)

        print(indent + ("└── " if is_left else "┌── ") + str(node.val))

        printTree(node.left, indent + ("    " if is_left else "│   "), True)

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def preOrder(root):
    if root is None:
        return
    print(root.val, end=", ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val, end=' ')
    inOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val, end=' ')

def menu():
    print("\n=== MENU BST ===")
    print("1. Masukkan data baru")
    print("2. Keluar")
    return input("Pilih menu (1/2): ")

if __name__ == "__main__":
    while True:
        pilihan = menu()
        if pilihan == '2':
            print("Terima kasih!")
            break
        elif pilihan == '1':
            root = None 
            while True:
                angka = input("\nMasukkan angka-angka (pisahkan dengan spasi): ").strip()
                if not angka:
                    print("Input kosong! Coba lagi.")
                    continue
                try:
                    data = list(map(int, angka.split()))
                    break 
                except ValueError:
                    print("Input tidak valid! Masukkan hanya angka!")

            for val in data:
                root = insert(root, val)

            print("\nVisualisasi Pohon BST:")
            printTree(root)
            print("\nPreorder:")
            preOrder(root)
            print("\nInorder:")
            inOrder(root)
            print("\nPostorder:")
            postOrder(root)
            print()
        else:
            print("Pilihan tidak valid! Pilih 1 atau 2.")
