from ex107mod.func import titulo, metade, dobro, aumentar, diminuir

num = 20

titulo(f"A metade de {num} é:")
print(metade(num))

titulo(f"O dobro de {num} é:")
print(dobro(num))

per = 20

titulo(f"Aumentar {per}% ao número {num}:")
print(aumentar(num,per))

titulo(f"Diminui {per}% ao número {num}:")
print(diminuir(num,per))
