seq = int (input("Quantos números da Sequência Fibonacci você quer exibir? \n"))
n1 = [0]
n2 = 1
while seq > 0:
    print(n1[-1], end="  ")
    n1.append(n2)
    n2 = n1[-1] + n1[-2]
    seq-=1
