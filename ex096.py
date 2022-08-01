def area(lar, comp):
    mQ = lar * comp
    print(f"Área: {lar:.2f} x {comp:.2f} = {mQ:.2f}m2.") 

largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))

area(largura, comprimento)