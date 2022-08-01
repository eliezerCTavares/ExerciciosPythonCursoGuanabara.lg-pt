lst = list(input("Digite uma expressão matemática para saber se ela está correta: "))
openn = []
closee = []
for brackets in lst:
    if brackets in "(":
        openn.append(brackets)
    elif brackets in ")":
        closee.append(brackets)    
print(lst,"\n",openn,"\n",closee,"\n")
if len(openn) == len(closee):
    print(f"{''.join(lst)}: Expressão correta.")
else:
    print(f"{''.join(lst)}: Expressão incorreta.")