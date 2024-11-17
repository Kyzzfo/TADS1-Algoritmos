print("====== Exercício 1 ======\nCalculadora de soma simples\n")

def validar(num):
    try:
        numf = float(num)
        return numf
    except ValueError:
        print(" Esse número não é válido.")
        return None

def somar(num1f, num2f):
    soma = num1f + num2f
    return soma


while True:
    num1 = (input("Digite o primeiro número para ser realizada a soma: ")).strip()
    if validar(num1) is not None:
        num11 = validar(num1)
        print(f"Primeiro número: {num11}")
        break
    
while True:
    num2 = (input("Digite o segundo número para ser realizada a soma: ")).strip()
    if validar(num2) is not None:
        num22 = validar(num2)
        print(f"Segundo número: {num22}")
        break

print(f"\nA soma dos números selecionados é {somar(num11, num22)}")

print("Final do programa")