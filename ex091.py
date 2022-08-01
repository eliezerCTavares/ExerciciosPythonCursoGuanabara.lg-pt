import random
from operator import itemgetter
jogadores = {}

for num in range(4):
    num = num+1
    jogadores[f'Player{num}'] = random.randint(1,6)
    print(f"Player{num}: {jogadores[f'Player{num}']}")

ordem = sorted(jogadores.items(), key=itemgetter(1) , reverse=True)
print(ordem)

for pos, val in enumerate(ordem):
    print(f"{pos+1}º lugar = {val[0]}: {val[1]}")