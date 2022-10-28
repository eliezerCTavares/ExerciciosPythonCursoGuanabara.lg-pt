from ex107mod.func import titulo, metade, dobro, aumentar, diminuir

num = int(input("Digite um número: "))

titulo(f"A metade de {num} é: {metade(num)}")
titulo(f"O dobro de {num} é: {dobro(num)}")

per = 20

titulo(f"Aumentar {per}% ao número {num}: {aumentar(num, per)}")
titulo(f"Diminui {per}% ao número {num}: {diminuir(num, per)}")
