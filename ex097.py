def escreva (tex):
    len_tex = len(tex)+2
    print("="*len_tex)
    print(f"{tex:^{len_tex}}")
    print("="*(len_tex))

for x in range (0, 3):
    texto = input("Escreva: ").upper()
    escreva (texto)
        