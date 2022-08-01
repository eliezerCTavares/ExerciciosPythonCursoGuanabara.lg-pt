media = {}

media['Jogador'] = input("Nome do jogador: ").title()
partidas = int(input("Quantidade de partidas: "))
media['Gols'] = []
media['Total'] = 0
for x in range (0, partidas):
    gol = int(input(f"Quantos gols o jogador {media['Jogador']} fez no {x+1}° jogo? "))
    media['Gols'].append(gol)
    media['Total'] += gol

print("="*50)
print(media)
print("="*50)
for k,v in media.items():
    print(f"{k}: {v}")

print("="*50)
print(f"O jogador {media['Jogador']} jogou {partidas} partidas:")
for n , g in enumerate(media['Gols']):
    print(f"    => Na partida {n+1} fez {g} gols.")
print(f"Com um total de {media['Total']} gols.")
print("="*50)