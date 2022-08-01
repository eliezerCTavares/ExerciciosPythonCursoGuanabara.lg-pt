print("\nConversão Decimal, Binaria e Hexadecimal\n\nEscolha uma conversão:")

escolha = int(input("0 = Bin -> Dec\n1 = Dec -> Bin\n2 = Oct -> Dec\n3 = Dec -> Oct\n4 = Hex -> Dec\n5 = Dec -> Hex"))

if escolha == 0:
    nbr = str(input("Digite um número binário para converter em Decimal: "))
    length = len(nbr) - 1
    bin2 = []
    for x in nbr:
        bin2.append(int(x) * 2 ** length)
        length -= 1
    print(f"Binário: {nbr}\nDecimal: {sum(bin2)}")

elif escolha == 1:
    numero = int(input("Digite um número Decimal inteiro para converter em Binário: "))
    nb = numero
    endgame = False
    bi_list = []
    while endgame == False:
        div_ = nb // 2
        mod_ = nb % 2
        print(div_)
        bi_list.append(mod_)
        nb = div_
        if div_ == 1:
            mod_ = 1
            print(div_)
            bi_list.append(mod_)
            endgame = True
    print(bi_list)
    bi_list.reverse()
    bi_ = map(str, bi_list)
    print("".join(bi_))

elif escolha == 2:
    nbr = str(input("Digite um número Octal para converter em Decimal: "))
    length = len(nbr) - 1
    bin2 = []
    if "8" in nbr or "9" in nbr:
        print("'8' e '9' não são Octais.")
    else:
        for x in nbr:
            bin2.append(int(x) * 8 ** length)
            length -= 1
        print(f"Octal: {nbr}\nDecimal: {sum(bin2)}")

elif escolha == 3:
    numero = int(input("Digite um número Decimal inteiro para converter em Octal: "))
    nb = numero
    endgame = False
    bi_list = []
    while endgame == False:
        div_ = nb // 8
        mod_ = nb % 8
        print(div_)
        bi_list.append(mod_)
        nb = div_
        if div_ < 8:
            mod_ = div_
            print(div_)
            bi_list.append(mod_)
            endgame = True
    print(bi_list)
    bi_list.reverse()
    bi_ = map(str, bi_list)
    print("".join(bi_))





elif escolha == 4:
    nbr = str(input("Digite um número Hexadecimal para converter em Decimal: "))
    length = len(nbr) - 1
    bin2 = []
    if "8" in nbr or "9" in nbr:
        print("'8' e '9' não são Octais.")
    else:
        for x in nbr:
            if x == "a":
                x = 10
            elif x == "b":
                x = 11
            elif x == "c":
                x = 12
            elif x == "d":
                x = 13
            elif x == "e":
                x = 14
            elif x == "f":
                x = 15
            bin2.append(int(x) * 16 ** length)
            length -= 1
        print(f"Octal: {nbr}\nDecimal: {sum(bin2)}")
elif escolha == 5:
    numero = str(input("Digite um número Decimal inteiro para converter em Hexadecimal: "))
    nb = int(numero)
    endgame = False
    bi_list = []
    while endgame == False:
        div_ = nb // 16
        mod_ = nb % 16

        if mod_ == 10:
            mod_ = "A"
        elif mod_ == 11:
            mod_ = "B"
        elif mod_ == 12:
            mod_ = "C"
        elif mod_ == 13:
            mod_ = "D"
        elif mod_ == 14:
            mod_ = "E"
        elif mod_ == 15:
            mod_ = "F"

        bi_list.append(str(mod_))
        nb = div_
        if div_ < 16:
            mod_ = div_
            print(div_)
            if mod_ == 10:
                mod_ = "A"
            elif mod_ == 11:
                mod_ = "B"
            elif mod_ == 12:
                mod_ = "C"
            elif mod_ == 13:
                mod_ = "D"
            elif mod_ == 14:
                mod_ = "E"
            elif mod_ == 15:
                mod_ = "F"

            bi_list.append(mod_)
            endgame = True

    bi_list.reverse()

    print(bi_list)
    bi_ = map(str, bi_list)
    hexa = " ".join(bi_)
    print(hexa)
    print(" ".join(bi_))