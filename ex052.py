escolha  = int(input("""\nPara calcular todos os números primos de 1 à 100, digite '1':
Para saber se um número específico é primo, digite 2:\n"""))

def primo(numbr):
    divisivel = []
    for n in range (1, numbr + 1):
        if numbr % n == 0:
            if numbr % numbr == 0:
                divisivel.append(int(numbr / n))
    if len(divisivel) == 2:
        print(f"{numbr} É PRIMO")
    else:
        print(f"{numbr}")
    

if escolha == 1:
    for number in range (1,101):
        primo(numbr=number)
elif escolha == 2:
    number = int(input("Qual número quer saber se é primo? "))
    primo(numbr=number)