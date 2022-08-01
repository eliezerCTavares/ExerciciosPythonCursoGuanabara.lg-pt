km = int(input("Quantos Km irá viajar? " ))


if km <= 200:
    preço1 = 0.50 * km
    print(f"Sua passagem para {km}Km custará R$ {preço1}")
else:
    preço2 = 0.45 * km
    print(f"Sua passagem para {km}Km custará R$ {preço2}")