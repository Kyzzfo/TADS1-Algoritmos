print("====== Exercício 2 ======\nVerificador de número par ou ímpar\n")

def parouimpar(num1):
    try:
        num11 = int(num1)
        if num11%2:
            print(f"O número {num11} é ímpar")
        else:
            print(f"O número {num11} é par")
        return True
    except ValueError:
        print(" Esse número não é válido.")
    return None

while True:
    num = (input("Digite o número que irei adivinhar se ele é par ou impar: ")).strip()
    if parouimpar(num) is not None:
        break
        
print("Final do programa")