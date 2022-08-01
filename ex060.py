n = int(input("Fatorial de: \n!"))
n1 = n
fat = n
while n > 1:
    fat = fat * (n-1)
    if n > 1:
        print(n, end=" x ")
    n = n-1
    if n == 1:
        print(1, end=" = ")
print(fat)
print (f"\nA fatorial de {n1}! é: ", fat)