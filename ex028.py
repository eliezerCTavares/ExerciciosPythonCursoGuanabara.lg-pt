#exercício 28 curso de python do gustavo guanabara

from random import randint
from time import sleep
cont = "Y"
while cont == "Y":
    comp_rand = randint(1, 5)
    print("\033[7;30;44m *  \033[m"*10)
    print("\033[1;30;44m Vou pensar um número. Tente adivinhar! \033[m")
    sleep(2)
    print("\033[7;30;44mPROCESSANDO...                          \033[m")
    sleep(2)
    user_choice = int(input("\033[1;30;44mDe 1 à 5, que número eu pensei?:        \033[m"))
    print("\033[7;30;44mPROCESSANDO...                          \033[m")
    sleep(2)
    if user_choice==comp_rand:
        print(f"\033[1;30;44mParabéns! Você acertou.\033[m\nPC pensou {comp_rand} / Usuário pensou {user_choice}\033[m\n")
    else:
        print(f"\033[1;30;44mQue pena, Você errou. PC: {comp_rand} / Usuário: {user_choice}\033[m\n")
    y_n= input("\033[7;30;44mVoçê quer continuar jogando?            \033[m").upper()
    if y_n == "N":
        cont = "N"
