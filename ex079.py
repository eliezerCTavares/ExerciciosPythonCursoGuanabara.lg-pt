lst = []
while True:
    num = int(input("Insira um número: "))
    if num in lst:
        print("\nJá está na lista.")
    else:
        lst.append(num)
        print("Adicionado com sucesso.\n")
    if input("Quer continuar? [S/N] ").strip().upper()[0] == "N":
        break

print(f"""
Os valores em ordem crescente são: {sorted(lst)}
Os valores em ordem decrescente são: {list(reversed(sorted(lst)))}
""")
