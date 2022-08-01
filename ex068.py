from random import randint
import time
soma = 0
while True:
    pc_num = randint(0, 10)
    time.sleep(1)
    user_hd = str(input("Usuário: Par ou impar [P / I]: ")).strip().upper()[0]
    user_num = int(input("\nQual número? "))
    if (pc_num+user_num) % 2 == 0:
        if "P" in user_hd:

            print(f'''
            Usuário jogou: {user_num}
            Pc jogou {pc_num}
            Total: {user_num+pc_num}
            Usuário escolheu par - Usuário Ganha.
            ''')
            soma += 1         
        else:
            
            print(f'''
            Usuário jogou: {user_num}
            Pc jogou {pc_num}
            Total: {user_num+pc_num}
            Usuário escolheu par: PC Ganha.
            ''')
            break     
    else:
        if "I" in user_hd:

            print(f'''
            Usuário jogou: {user_num}
            Pc jogou: {pc_num}
            Total: {user_num+pc_num}
            Usuário escolheu Ímpar: Usuário Ganha.
            ''')
            soma += 1 
        else:
            print(f'''
            Usuário jogou: {user_num}
            Pc jogou: {pc_num}
            Total: {user_num+pc_num}
            Usuário escolheu Ímpar: PC Ganha.
            ''')
            break
print(f"Usuário ganhou {soma} vez(es).")