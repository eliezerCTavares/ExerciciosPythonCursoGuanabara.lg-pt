def metade(n):
    res = n/2
    return res

def dobro(n):
    res = n*2
    return res

def aumentar(n, pc):
    calc = n*(pc*0.01)
    res = n+calc
    return res

def diminuir(n, pc):
    calc = n*(pc*0.01)
    res = n-calc
    return res

def titulo (text):
    print("_" * 40)
    print(f"{text}")

def func(valor):
    result = "R$" + str(valor)
    return result