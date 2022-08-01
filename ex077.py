tup = "aprender", "gratis", "mercado", "vogal", "carro", "programa", "nada"
for word in tup:
    print(f"Na palavra {word.upper()} temos as vogais: ",end="")
    for letter in word:
        if letter.upper() in "AEIOU":
            print(letter.upper(), end="")
    print("\n")