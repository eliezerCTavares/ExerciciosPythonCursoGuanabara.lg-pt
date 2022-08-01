num = int(input("Fatorial de: \n!"))

def fatorial(n, show=False):
    """ Calcula a faorial de um número.
    n é o valor inserido pelo uruário a ser calculado.
    "show=True" mostra o cálculo até chegar no resultado.
    "show=False" mostra somente o resultado, sem o cálculo
    """
    n1 = n
    fat = n
    while n > 1:
        fat = fat * (n-1)
        if n > 1 and show==True:
            print(n, end=" x ")
        n = n-1
        if n == 1 and show==True:
            print(1, end=" = ")
    print (f"\nA fatorial de {n1}! é: ", fat)

fatorial(num,show=True)
help(fatorial)