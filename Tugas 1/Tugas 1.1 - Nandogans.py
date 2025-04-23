# Membalikkan String menggunakan bahasa Python

ulang = True

# Membuat kondisi untuk mengulangi program
while ulang == True:
    inputStr = input("Masukkan string yang ingin dibalik: ")
    reversedStr = ""

    # Menggunakan loop untuk membalikkan string
    for i in range(len(inputStr) - 1, -1, -1):
        reversedStr += inputStr[i]

    print("Hasil String yang dibalik adalah:", reversedStr)
    print()
    
    # Menanyakan kepada pengguna apakah ingin mencoba lagi
    ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
    
    # Menggunakan ternary operator 
    ulang = True if ulang == 'y' else False 
    
    # Menggunakan if-else 
    # if ulang.lower() == 'y':
    #     ulang = True
    # else:
    #     ulang = False
    print()