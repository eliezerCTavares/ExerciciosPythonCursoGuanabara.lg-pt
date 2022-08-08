from ex107mod import func

num = int(input("Valor: "))
per = int(input("Porcentagem: "))

print(f"{'METADE'}{'DOBRO'}{'AUMENTAR'}{'DIMUNUIR'}")

print(func.metade(num))

print(func.dobro(num))

print(func.aumentar(num,per))

print(func.diminuir(num,per))