impar = 0
for num in range(1,501,2):
    if num % 3 == 0:
        impar += num
print(impar)