def converter(string,base):
    stackInt = []
    stackFloat = []
    # integer
    a = int(desimal)
    hex_map = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while a>0:
        digit = a%base
        if base==16 and digit>=10:
            stackInt.append(hex_map[digit])
        else:
            stackInt.append(digit)
        a = a//base
    digits = ''
    while stackInt:
        digits += str(list.pop(stackInt))
    # float
    floated = desimal - int(desimal)
    if floated == 0.00:
        print(f"{string} = {digits}")
    else:
        while floated>0:
            floated *= base
            digit = int(floated)
            if base==16 and digit>=10:
                stackFloat.append(hex_map[digit])
            else: 
                stackFloat.append(digit)
            floated -= int(floated)
        floats = ''
        while stackFloat:
            floats += str(list.pop(stackFloat))
        print(f"{string} = {digits}.{floats[::-1]}")

while True:
    try: 
        desimal = float(input("Masukkan bilangan desimal = "))
    except:
        print('Input tidak valid, harus bilangan desimal')
        continue    
    
    print(f"Desimal = {desimal}")
    print()

    print("Hasilnya : ")
    converter('Biner', 2)
    converter('Oktal', 8)
    converter('Heksadesimal', 16)
    
    loop = input("ulangi kode? yes/no\n")
    if loop.lower() != 'yes':
        break