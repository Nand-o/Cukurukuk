# Membalikkan String menggunakan bahasa Python
with open('data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

ulang = True

tumpukanParagraf = []

# Membuat kondisi untuk mengulangi program
while ulang == True:
    print()
    print("Membalikkan String")
    print("===================================")
    print("Menu:")
    print("0. Memasukkan data melalui file dan membalikkan string")
    print("1. Menambahkan paragraf melalui terminal ke dalam tumpukan")
    print("2. Jalankan pembalikan string")
    print("3. Keluar dari program")
    
    pilihan = input("Silahkan pilih (1 atau 2) lalu Enter: ")
    
    if pilihan  == '0':
        print()
        print("Data hasil pembalikan string:")
        for line in lines:
            dataTxt = line.strip()[::-1] # Membaca file dan membalikkan string
            print(dataTxt)
    
    elif pilihan == '1':  
        current_paragraph = []
            
        print("Silakan masukkan paragraf satu per satu.")
        print("Jika paragraf sudah selesai, tulis SELESAI lalu tekan Enter.")    
            
        while True:
            line = input()
            if line == "SELESAI":
                # Simpan paragraf terakhir jika ada
                if current_paragraph:
                    tumpukanParagraf.append('\n'.join(current_paragraph))
                break
                
                # Jika baris kosong, ini menandakan paragraf baru
            if line.strip() == "":
                if current_paragraph:  # Hanya tambahkan jika paragraf tidak kosong
                    tumpukanParagraf.append('\n'.join(current_paragraph))
                    current_paragraph = []
            else:
                current_paragraph.append(line)
        
        
    elif pilihan == '2':
        if len(tumpukanParagraf) == 0:
            print("Tidak ada string yang ditambahkan. Silakan tambahkan string terlebih dahulu.")
            continue
        else:
            
            for i in range(len(tumpukanParagraf)):
                print()
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
                
                print(f"Hasil pembalikan paragraf ke-{i+1}: ")
                
                # Menggunakan loop untuk menampilkan hasil
                for kata in tumpukanHasil:
                    print(kata, end=" ")
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
            print("Program selesai. Sampai jumpa lagi!")
            break
        
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        print()