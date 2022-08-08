from ex110mod import func as fn

num = int(input("Valor: R$ "))
per = int(input("Porcentagem: % "))

print("="*50)

print(f" {'METADE':<10} | {'DOBRO':<10} | {'AUMENTAR':<10} | {'DIMINUIR':<10}")

print(f" {fn.func(fn.metade(num)):<9} ", end= " | ")

print(f"{fn.func(fn.dobro(num)):<9} ", end= " | ")

print(f"{fn.func(fn.aumentar(num,per)):<9} ", end= " | ")

print(f"{fn.func(fn.diminuir(num,per)):<9}")

print("="*50)