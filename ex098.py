def contador(ini,fim,pas):
    if pas == 0:
        pas=1
    if ini > fim:
        pas = -abs(pas)
        fim = fim-1
    else:
        fim = fim+1

    for x in range (ini,fim,pas):
        print(x,end=" ")

inicio = int(input("INICIO: "))
final = int(input("FIM: "))
passo = int(input("PASSO: "))

contador(inicio,final,passo)