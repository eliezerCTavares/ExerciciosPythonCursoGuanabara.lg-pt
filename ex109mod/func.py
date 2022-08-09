def metade(n, mostrar= False):
    res = n/2
    return res if mostrar == False else f"{moeda()}{res}"

def dobro(n, mostrar= False):
    res = n*2
    return res if mostrar == False else f"{moeda()}{res}"

def aumentar(n,pc, mostrar= False):
    calc = n*(pc*0.01)
    res = n+calc
    return res if mostrar == False else f"{moeda()}{res}"

def diminuir(n,pc, mostrar= False):
    calc = n*(pc*0.01)
    res = n-calc
    return res if mostrar == False else f"{moeda()}{res}"

def moeda (rs="R$"):
    return rs