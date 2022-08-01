from random import randint
import time

def bloco():
    aleatorio = randint(0,10)
    valores = []
    for x in range(0,aleatorio):
        ale = randint(0,100)
        valores.append(ale)
    print("="*80)
    print("ANALISANDO...",end=" ")
    time.sleep(0.5)

    for x in valores:
        print(x,end=" - ")
        time.sleep(0.5)
    print("FIM")
    time.sleep(0.5)
    print(f"Foram passados {len(valores)} valores.",end=" | ")
    time.sleep(0.5)
    if valores == []:
        print("Nenhum valor encontrado.")
    else:
        print(f"O maior valor passado foi: {max(valores)}.")
    time.sleep(0.5)
    print("="*80)

for z in range(0,4):
    bloco()