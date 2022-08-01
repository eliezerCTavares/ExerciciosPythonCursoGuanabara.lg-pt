velocidade = float(input("Velocidade KM/H: "))
if velocidade > 80:
    excesso = (velocidade - 80)*7
    print(f"Você está a {velocidade} km/h e ultrapassou o limite de 80 km/h e será multado em R${excesso}.")
else:
    print("Você está abaixo do limite de velocidade.")