from random import *
print("====== Exercício 15 ======\nJogo da adivinhação\n")

print("O jogo consiste em tentar acertar um número aleatório de 1 até 100")
print("Enquanto não acertar o número, o computador lhe dará instruções se o número que você chutou é maior ou menor do que o número aleatório")

aleatorio=randint(1,100)

def tentativas(numt):
    try:
        if 100>=int(numt)>=1:
            if int(numt)>aleatorio:
                print(f"O número secreto é menor do que {numt}")
            elif int(numt)<aleatorio:
                print(f"O número secreto é maior do que {numt}")
            elif int(numt)==aleatorio:
                print(f"Você acertou! O número sorteado era {numt}")
                return True
        else:
            print("Insira um número de 1 a 100")
    except ValueError:
        print(" Esse valor não é valido.")

while True:
    num = input("Dê seu chute: ").strip()
    if tentativas(num) == True:
        break

print("Final do programa")