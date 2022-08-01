brasileirao = ("Flamengo", "Palmeiras", "Atlético Mineiro","Grêmio","Athletico Paranaense", "Santos", "São Paulo","Internacional", "Fluminense", "Corinthians", "Fortaleza","Bahia", "Ceará", "Cruzeiro", "América Mineiro",
"Atlético Goianiense", "Chapecoense", "Botafogo", "Vasco da Gama", "Red Bull Bragantino")

print(f"""
\nOs 5 primeiros colocados são:{brasileirao[:5]}

Os 4 últimos colocados da tabela: {brasileirao[-4:]}

Todos os times em ordem alfabética: {sorted(brasileirao)}

Chapecoense está na posição: {brasileirao.index("Chapecoense")+1}
""")