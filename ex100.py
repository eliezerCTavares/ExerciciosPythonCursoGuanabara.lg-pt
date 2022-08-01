from random import randint
import time

def sorteia(nume):
    print("SORTEANDO... ", end="")
    for _ in range (0,5):
        time.sleep(0.5)
        num = randint(0,100)
        nume.append(num)
        print(num, end=" - ")
    print("END")
    print(f"A soma dos valores é: {sum(nume)}.")
    time.sleep(0.5)

numeros = []

sorteia(numeros)


def soma_par(lista):
    ''''''
    print("Os números pares são: ",end="")
    time.sleep(0.5)
    par = 0
    for z in lista:
        if z % 2 == 0:
            print(z,end=" - ")
            time.sleep(0.5)

            par+=z
    if par == 0:
        print("Nenhum valor par encontrado")
    print("END")
    print(f"A soma dos números pares é: {par}")

soma_par(numeros)
help(soma_par)
