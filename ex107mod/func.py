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

def titulo (text):
    print("="*40)
    print(f"{text}")

def func():
    return "R$"