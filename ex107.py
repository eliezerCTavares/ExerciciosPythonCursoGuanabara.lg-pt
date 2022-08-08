from ex107mod import func

num = 20

func.titulo(f"A metade de {num} é:")
print(func.metade(num))

func.titulo(f"O dobro de {num} é:")
print(func.dobro(num))

per = 20

func.titulo(f"Aumentar {per}% ao número {num}:")
print(func.aumentar(num,per))

func.titulo(f"Diminui {per}% ao número {num}:")
print(func.diminuir(num,per))