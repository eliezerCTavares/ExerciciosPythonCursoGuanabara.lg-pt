v1 = int(input("Digite um valor A: "))
v2 = int(input("Digite um valor B: "))

if v1 > v2:
    print(f"O valor A ({v1}) é maior do que B ({v2}).")
elif v2 > v1:
    print(f"O valor B({v2}) é maior do que A ({v1}). ")
elif v1 == v2:
    print(f"Não existe valor maior, os dois valores são iguais: A: {v1} = B: {v2}")