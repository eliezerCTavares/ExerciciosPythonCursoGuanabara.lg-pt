from datetime import datetime
maiores = []
menores = []
x = 1
for _ in range (1, 8):
    ano = int(input(f"Qual o ano de nascimento da pessoa {x}? "))
    idade = (datetime.today().year)-ano
    
    if idade >= 21:
        print(f"Pessoa {x} - {(datetime.today().year)-ano} anos  -  atingiu a maioridade.")
        maiores.append(idade)
    else:
        print(f"Pessoa {x} - {(datetime.today().year)-ano} anos  -  NÃO atingiu a maioridade.")
        menores.append(idade)
    x+=1
print(f"Maioridade: {len(maiores)}")
print(f"Menoridade: {len(menores)}")