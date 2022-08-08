from ex107mod import func as fn

num = int(input("Valor: R$ "))
per = int(input("Porcentagem: % "))

print("="*50)

print(f" {'METADE':<10} | {'DOBRO':<10} | {'AUMENTAR':<10} | {'DIMINUIR':<10}")

valores = [fn.metade(num), fn.dobro(num), fn.aumentar(num,per), fn.diminuir(num,per)]

for v in valores:
    if v == valores[-1]:
        print(f" {fn.func()} {v:<8}")
        break
    print(f" {fn.func()} {v:<8}", end="|")

print("="*50)