numeros = [[],[]]
for number in range(7):
    num = int(input("Número: "))
    if num % 2 == 0:
        if numeros[0] == [] or num >= numeros[0][-1]:
            numeros[0].append(num)
        else:
            for p, n in enumerate(numeros[0]):
                if num < n:
                    numeros[0].insert(p,num)
                    break
    else:
        if numeros[1] == [] or num >= numeros[1][-1]:
            numeros[1].append(num)
        else:
            for p, n in enumerate(numeros[1]):
                if num < n:
                    numeros[1].insert(p,num)
                    break
print(numeros)