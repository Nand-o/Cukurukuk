def converter(string,base):
    stackInt = []
    stackFloat = []
    # integer
    a = int(desimal)
    hex_map = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    print("\nProses Bilangan Bulat")
    while a>0:
        digit = a%base
        print(f"{a} : {base} = {a//base} sisa {digit}")
        if base==16 and digit>=10:
            stackInt.append(hex_map[digit])
        else:
            stackInt.append(digit)
        a = a//base
    digits = ''
    while stackInt:
        digits += str(stackInt.pop())
    # float
    floated = desimal - int(desimal)
    if floated == 0.00:
        print(f"{string} = {digits}")
    else:
        print("\nProses Float/Koma")
        while floated>0:
            floated *= base
            digit = int(floated)
            print(f"{floated} x {base} =  sisa {digit}")
            if base==16 and digit>=10:
                stackFloat.append(hex_map[digit])
            else: 
                stackFloat.append(digit)
            floated -= int(floated)
        floats = ''
        while stackFloat:
            floats += str(stackFloat.pop())
        print(f"{string} = {digits}.{floats[::-1]}")

while True:
    try: 
        desimal = float(input("Masukkan bilangan desimal = "))
    except ValueError:
        print('Input tidak valid, harus bilangan desimal')
        continue    
    
    print(f"\nDesimal = {desimal}\n")
    print("Hasilnya : ")
    kumpulanConvert = [('Biner', 2),('Oktal', 8),('Heksadesimal', 16)]
    for string, base in kumpulanConvert:
        converter(string, base)
    
    loop = input("\nulangi kode? yes/no\n")
    if loop.lower() != 'yes':
        break