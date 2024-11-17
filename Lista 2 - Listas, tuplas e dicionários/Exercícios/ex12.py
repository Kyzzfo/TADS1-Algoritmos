from math import *
print("====== Exercício 12 ======\nVerificar números primos em um intervalo\n")

def primo(num):
    if num<=1:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def mostrarprimos(start,end):
    for i in range(start, end+1):
        if primo(i) == True:
            print(i)
            
def verificaini(star):
    try:
        return int(star)
    except ValueError:
        print(" Esse valor não é valido.")
    return None

def verificafim(fin, start):
    try:
        fim = int(fin)
        if fim>start:
            return fim    
        else:
            print("O número que finaliza o intervalo deve ser maior que o que inicia")
            return None
    except ValueError:
        print(" Esse valor não é valido.")
        return None

while True:
    num1 = (input("Digite um número inteiro para decidir o início do intervalo: ")).strip()
    if verificaini(num1) is not None:
        ini = verificaini(num1)
        print(f"Certo, o número que inicia o intervalo é {ini}")
        break
while True:
    num2 = (input("Digite um número inteiro para decidir o final do intervalo: ")).strip()
    if verificafim(num2, ini) is not None:
        fim = verificafim(num2, ini)
        print(f"Então o intervalo vai de {ini} até {fim}")
        break


print(f"Agora serão mostrados a seguir os números primos de {ini} a {fim}")
mostrarprimos(ini, fim)
print("Final do programa")