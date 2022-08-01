lst = []

while True:
    add = int(input("Inserir: "))
    lst.append(add)
    if input("Continuar inserindo? ").strip().upper()[0] == "N":
        break

lst_even = []
lst_odd = []
for num in lst:
    if num % 2 == 0:
        lst_even.append(num)
    else:
        lst_odd.append(num)

print(f"Lista completa: {lst} / Pares: {lst_even} / Ímpares: {lst_odd}")
