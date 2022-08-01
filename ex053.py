frase = input("Frase: ").upper().replace(" ","")
if (frase[::-1]) == frase:
    print ("Palíndromo")
else:
    print("Não é um palíndromo")
print (f"{frase} x {frase[::-1]}")
