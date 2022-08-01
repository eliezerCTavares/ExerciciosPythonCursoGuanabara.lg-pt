nums =0
soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    nums +=1
print(f"Soma total: {soma}\nNúmeros digitados: {nums}")
