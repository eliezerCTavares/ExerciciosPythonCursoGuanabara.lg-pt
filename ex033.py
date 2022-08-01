numeros = input("Digite 3 números separados por espaço: ").split()
print (numeros)
n1 = int(numeros[0])
n2 = int(numeros[1])
n3 = int(numeros[2])

def maior(n1,n2,n3):

    if n1 > n2 and n1 > n3:
        print(f"{n1} é maior do que {n2} e {n3}")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} é maior do que {n1} e {n3}")
    elif n3 > n2 and n3 > n1:
        print(f"{n3} é maior do que {n2} e {n1}")

def menor(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        print(f"{n1} é Menor do que {n2} e {n3}")
    elif n2 < n1 and n2 < n3:
        print(f"{n2} é menor do que {n1} e {n3}")
    elif n3 < n2 and n3 < n1:
        print(f"{n3} é menor do que {n2} e {n1}")
maior(n1,n2,n3)
menor(n1,n2,n3)