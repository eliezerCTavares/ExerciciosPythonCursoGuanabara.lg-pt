tup = (int(input("Insira um número: ")),
int(input("Insira o segundo número: ")),
int(input("Insira terceiro número: ")),
int(input("Insira o último número: ")),
)

print(tup)
print(f"O número 9 foi digitado {tup.count(9)} vez(es)")
###################
if 3 in tup:
    print(f"Número 3 está na {tup.index(3)+1}ª posição.")
else:
    print("O número 3 não foi digitado.")
 ################   
print("Os números pares foram ",end="")
for x in tup:
    if x % 2 == 0:
        print(f"{x}",end=" ")