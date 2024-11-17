print("====== Exercício 16 ======\nFunção recursiva para cálculo fatorial\n")

def verifica(num):
    try:
        if int(num)>0:
            return int(num)
        else:
            print("Insira um número maior que 0")
            return None
    except ValueError:
        print(" Esse número não é válido.")
        return None
def fatorial(fato):
    if fato>=1:
        return fato * fatorial(fato-1)
    else:
        return 1

while True:
    num1 = (input("Digite um número inteiro para ser realizado o seu cálculo fatorial: ")).strip()
    if verifica(num1) is not None:
        num11 = verifica(num1)
        print(f"O fatorial do número {num11} é {fatorial(num11)}")
        break
    
print("Final do programa")