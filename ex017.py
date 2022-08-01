numero = str(input("Digite um número Decimal inteiro para converter em Hexadecimal: "))
nb = int(numero)
endgame = False
bi_list = ""
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
    if div_ == 1:
        mod_ = 1
        bi_list.append(str(mod_))
        endgame = True

bi_list.reverse()

print(bi_list)
bi_ = map(str, bi_list)
hex = " ".join(bi_)
print(hex)
print(" ".join(bi_))
