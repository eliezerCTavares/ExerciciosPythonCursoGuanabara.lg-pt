pessoas = []
pessoa = {}
while True:
    pessoa ["nome"] = input("Nome: ").title()
    while True:    
        pessoa ['sexo'] = input("Sexo [M/F]: ").strip().upper()[0]
        if pessoa ['sexo'] in "MF":
            break
        print("Sexo inválido. Digite corretamente. ")
    pessoa ["idade"] = int(input("Idade: "))
    pessoas.append(pessoa.copy())

    cont = ""
    while True:
        cont = input("Quer cadastrar outra pessoa? [S/N]").strip().upper()[0]
        if cont in "SN" :
            break
        print("ERRO. Digitte corretamente")
    if cont == "N":
        break


print("=" * 50)
soma_idade = 0
mulheres = []
for dic in pessoas:
    for k, v in dic.items():
        if k == "idade":
            soma_idade += v
        if k == "sexo" and v == "F":
            mulheres.append(dic["nome"])
        print(f"{k}: {v}",end=" ... ")
    print()
acima_da_media = []
for pess in pessoas:
    for k, v in pess.items():
        if k == "idade":
            if v > (soma_idade/len(pessoas)):
                acima_da_media.append(pess["nome"])


print("=" * 50)
print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"A idade média das pessoas cadastradas é: {soma_idade} / {len(pessoas)} = {soma_idade / len(pessoas):.2f}")
print("As mulheres cadastradas são: ",end="")
for x in mulheres:
    print(f'{x}; ',end="")
print()

print("="*50)
print("Pessoas acima da idade média: ")
for idoso in acima_da_media:
    for x in pessoas:
        for k,v in x.items():
            if v == idoso:
                for chave , valor in x.items():
                    print(f"{chave}: {valor}", end=" | ")
                print()

print("="*50)