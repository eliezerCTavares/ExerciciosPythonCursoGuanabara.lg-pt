jogadores = []
while True:
    media = {}

    media['Jogador'] = input("Nome do jogador: ").title()
    partidas = int(input("Quantidade de partidas: "))
    media['Gols'] = []
    media['Total'] = 0
    for x in range(0,partidas):
        gol = int(input(f"Quantos gols {media['Jogador']} fez no {x+1}° jogo? "))
        media['Gols'].append(gol)
        media['Total'] += gol

    jogadores.append(media)
    if input("Quer cadastrar outro jogador? ").strip().upper()[0] == "N":
        break
print("="*80)
print(f"{'Cód':<10} {'NOME':<25} {'GOLS':<} {'TOTAL':>25} |")
for i, l in enumerate(jogadores):
    print(f"{i:<10}", end=" ")
    tam = 0
    total_length = 0
    for k,v in l.items():
        if k == 'Gols':
            tam = len(v)
            for x in v:
                print(f"{x}",end=" ")
        elif k == "Total":
            total_length = len(str(v))
            tam = 26 - (tam*2)
            print(f"{v:>{tam}}", end=" ")
        elif k == 'Jogador':
            print(f"{v:<25}", end=" ")
        else:
            print(f"{v:<10}", end=" ")
    print(" "*(4-total_length),"|")
print("="*80)
while True:
    per = int(input("Digite o código para ver os dados do jogador: "))
    for k,v in jogadores[per].items():
        if k == "Gols": 
            print(f"Jogador: {jogadores[per]['Jogador'].upper()}")
            for i , l in enumerate(jogadores[per][k]):
                print(f"Jogo {i+1}: {l} gol(s).")
    print("="*80)
    if input("Quer buscar os dados de outro jogador? [S/N] ").strip().upper()[0] =="N":
        break
print("BYE!")