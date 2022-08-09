def metade(n, mostrar= False):
    res = n/2
    return res if mostrar == False else f"{moeda()}{res:.2f}".replace(".",",")

def dobro(n, mostrar= False):
    res = n*2
    return res if mostrar == False else f"{moeda()}{res:.2f}".replace(".",",")

def aumentar(n,pc, mostrar= False):
    calc = n*(pc*0.01)
    res = n+calc
    return res if mostrar == False else f"{moeda()}{res:.2f}".replace(".",",")

def diminuir(n,pc, mostrar= False):
    calc = n*(pc*0.01)
    res = n-calc
    return res if mostrar == False else f"{moeda()}{res:.2f}".replace(".",",")

def moeda (rs="R$"):
    return rs

def resumo (num, aum, red):
    rs=moeda()
    print("="*50)
    print(f"Valor analisado: \t{rs}{num:.2f}")
    print(f"O dobro de {rs}{num}: \t{dobro(num, True)}")
    print(f"A metade de {rs}{num}: \t{metade(num, True)}")
    print(f"{aum}% de aumento: \t{aumentar(num, aum, True)}")
    print(f"{red}% de aumento: \t{diminuir(num, red, True)}")