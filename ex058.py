from random import randint
from time import sleep
y_n = "S"
while not y_n == "N":
    comp_rand = randint(1, 5)
    print("Vou pensar um número. Tente adivinhar!\n")
    sleep(1)
    print("PROCESSANDO...\n")
    sleep(1)
    user_choice = int(input("De 1 à 5, que número eu pensei?: \n"))
    print("PROCESSANDO... \n")
    sleep(1)
    if user_choice==comp_rand:
        print(f"Parabéns! Você acertou. - PC pensou {comp_rand} / Usuário pensou {user_choice}.\n")
    else:
        print(f"Que pena, Você errou. PC: {comp_rand} / Usuário: {user_choice}\n")

    y_n= input("Voçê quer continuar jogando? (S/N)\n").strip().upper()[0]

print("\nFIM DE JOGO")