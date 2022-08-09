def metade(n):
    return n/2

def dobro(n):
    return n*2

def aumentar(n,pc):
    calc = n*(pc*0.01)
    return n+calc

def diminuir(n,pc):
    calc = n*(pc*0.01)
    return n-calc

def func(valor=0,  moeda = "R$"):
    return f"{moeda} {valor:.2f}".replace(".",",")