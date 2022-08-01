lst = []
for x in range(6):
    num = int(input("digite: "))
    if lst == [] or num >= lst[-1]:
        print("Número adicionado ao final da lista.")
        lst.append(num)
    else:
        for pos, zz in enumerate(lst):
            if num < zz:
                print(f"Número inserido à posição {pos}")
                lst.insert(pos,num)
                break
    print(lst)