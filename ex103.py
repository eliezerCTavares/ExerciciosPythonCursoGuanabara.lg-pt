def ficha(jogador,gols=0):
    if jogador=="":
        jogador = "<desconhecido>"
    if gols.isnumeric() == False:
        gols=0
    else:
        gols= int(gols)
    print(f"Jogador {jogador} fez {gols} gols.")


jog = input("Jogador: ").strip().title()
gol = input("Gols: ").strip()


ficha(jog,gol)