from ex109mod.func import metade, dobro, aumentar, diminuir

num = int(input("Valor: R$ "))
per = int(input("Porcentagem: % "))

print("="*50)

print(f" {'METADE':<10} | {'DOBRO':<10} | {'AUMENTAR':<10} | {'DIMINUIR':<10}")

print(f" {metade(num, True):<9} ", end= " | ")

print(f"{dobro(num, True):<9} ", end= " | ")

print(f"{aumentar(num,per, True):<9} ", end= " | ")

print(f"{diminuir(num,per, True):<9}")

print("="*50)