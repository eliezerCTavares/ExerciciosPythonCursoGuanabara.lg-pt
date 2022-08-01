from random import randint

randic = randint(1,3)
print("1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n")

lista = ["Pedra","Papel","Tesoura"]

user = int(input("Player escolhe: "))
pc = randint(1,3)
print (f"PC escolhe: {pc}\n")
if user==pc:
    print(f"PC: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nEmpate")
elif user==1 and pc==2:
    print(f"Pc: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nPC vence. Papel ganha da pedra (embrulhando-a).")

elif user==1 and pc==3:
    print(f"Pc: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nPlayer vence. Pedra ganha da tesoura (amassando-a ou quebrando-a).")
    
elif user==2 and pc==3:
    print(f"Pc: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nPC vence. Tesoura ganha do papel (cortando-o).")

elif user==2 and pc==1:
    print(f"Pc: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nPlayer vence. Papel ganha da pedra (embrulhando-a).")

elif user==3 and pc==1:
    print(f"Pc: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nPC vence. Pedra ganha da tesoura (amassando-a ou quebrando-a).")

elif user==3 and pc==2:
    print(f"Pc: {pc} - {lista[pc-1]}\nPlayer: {user} - {lista[user-1]}\nPlayer vence. Tesoura ganha do papel (cortando-o).")
else:
    print("Whatever!")
print("\n")