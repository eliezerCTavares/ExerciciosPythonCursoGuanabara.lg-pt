while True:
    vl = int(input("Quer ver a tabuada de qual valor? "))
    if vl < 0:
        break
    for x in range (0, 11):
        print(f"{vl} x {x} = {vl * x}")
print("Encerrado")