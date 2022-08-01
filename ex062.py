print("Calcule uma Progressão Aritmética")
primter = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
x = 10
cont = 0
while x >0:
    while x > 0 :
        print(primter, end=" - ")
        primter+=razao
        x-=1
        cont+=1
    print("PAUSA")
    x = int (input("\n\nQuantos termos a mais quer mostrar: "))
print(f'Foram mostrados {cont} termos.')