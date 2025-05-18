# Membalikkan String menggunakan bahasa Python

ulang = True

tumpukanParagraf = []

# Membuat kondisi untuk mengulangi program
while ulang == True:
    print()
    print("Membalikkan String")
    print("===================================")
    print("1. Menambahkan paragraf")
    print("2. Jalankan pembalikan string")
    print("3. Keluar dari program")
    
    pilihan = input("Silahkan pilih (1 atau 2) lalu Enter: ")
    
    if pilihan == '1':
        inputStr = input("Masukkan string yang ingin dibalik: ")
        
        tumpukanParagraf.append(inputStr) # Menyimpan string ke dalam tumpukanParagraf
        print("String berhasil ditambahkan ke dalam tumpukan.")
        
        
    elif pilihan == '2':
        if len(tumpukanParagraf) == 0:
            print("Tidak ada string yang ditambahkan. Silakan tambahkan string terlebih dahulu.")
            continue
        else:
            
            for i in range(len(tumpukanParagraf)):
                print()
                print(f"String ke-{i+1}: {tumpukanParagraf[i]}")
                print()
                # Menggunakan loop untuk membalikkan string
                tumpukanHasil = []
                
                paragraf = tumpukanParagraf[i] # Mengambil string dari tumpukanParagraf
                
                # Memisahkan string menjadi per kata
                for kata in paragraf.split(): # Memisahkan string berdasarkan spasi
                    # Membalikkan setiap kata
                    kataBalik = ""
                    for huruf in kata: # Menggunakan loop untuk membalikkan huruf
                        kataBalik = huruf + kataBalik
                    tumpukanHasil.append(kataBalik) # Menyimpan kata yang sudah dibalik ke dalam tumpukanHasil
                
                print()
                print("Hasil pembalikan string: ", end="")
                
                # Menggunakan loop untuk menampilkan hasil
                for kata in tumpukanHasil:
                    print(kata, end=" ")
                print()    
            print()      

            
    elif pilihan == '3':
        print("Terima kasih telah menggunakan program ini.")

        # Menanyakan kepada pengguna apakah ingin mencoba lagi
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ").lower()
        
        # Menggunakan ternary operator 
        ulang = True if ulang == 'y' else False 
        if ulang == True:
            tumpukanParagraf.clear() # Menghapus semua string yang ada di dalam tumpukanParagraf
        
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        print()