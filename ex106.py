from colorama import Fore, Style

def titlePrint(desenho, título):
    tamanho = 50
    print(Fore.BLUE + f"{desenho}"*tamanho)
    print(f"{título:^{tamanho}}" + Style.RESET_ALL)
    print(Fore.BLUE + f"{desenho}" *tamanho +Style.RESET_ALL)


while True:
    titlePrint("=", "PyHelp")
    escolha = input("Escolha um módulo ou uma biblioteca: ")
    titlePrint("-",f"Help de {escolha}.")
    print(help(escolha))
    if escolha == "fim":
        break


titlePrint("=", "Fim")