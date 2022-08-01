lst = []
while True:
    add = int(input("Inserir número: "))
    lst.append(add)
    if input("Quer continuar inserindo? [S/N] ").strip().upper()[0] == "N":
        break

print(f"Foram digitados {len(lst)} números.")

print(f"A lista em ordem decrescente: {sorted(lst)[::-1]}")

if 5 in lst:
    print(f"O número 5 foi digitado e está na {lst.index(5)+1}ª posição da lista: {lst}.")
else:
    print("O número 5 NÃO foi digitado e NÃO está na lista.")