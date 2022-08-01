idades = []
homens_idade = 0
homens_nome = []
mulheres_menor = 0

for pessoa in range (0, 4):
    print(f"\n{pessoa+1}ª Pessoa")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    idades.append(idade)
    sexo = input("Sexo: M ou F: ").upper()
    if sexo == "M":
        if idade > homens_idade:
            homens_idade = idade
            homens_nome = nome
    elif sexo == "F":
        if idade < 21:
            mulheres_menor+=1

print (f"\nMédia das idades: {(sum(idades))/4}")
print(f"Mulheres na menoridade: {mulheres_menor}.")
print(f"Homem mais velho: {homens_nome} / Idade {homens_idade}.")