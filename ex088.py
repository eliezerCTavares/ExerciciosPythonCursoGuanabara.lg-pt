from random import randint
jogos = int(input("Quantos jogos você quer gerar? "))
for game in range(jogos):
    jogada = []
    for num in range(6):
        while True:
            gerar = randint(1,60)
            if gerar not in jogada:
                jogada.append(gerar)
                break
    print(f"Jogo {game+1} = {jogada}")