lst = []
mai=0
men=0
for n in range(5):
    lst.append(int(input(f"Insira o {n+1}º valor: ")))
    if n == 0:
        mai = men = lst[n]
    else:
        if lst[n] > mai:
            mai = lst[n]
        else:
            men = lst[n]
mai_p = []
men_p = []
for p , n in enumerate(lst):
    if n == mai:
        mai_p.append(p)
    if n == men:
        men_p.append(p)

print("Você digitou os valores:", lst)
print(f"\nO maior valor é: {mai} na posição {mai_p}")
print(f"\nO menor valor é: {men} na posição {men_p}")