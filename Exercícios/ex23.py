print("====== Exercício 23 ======\nCalculadora básica\n")

def validanum(num):
    try:
        return float(num)
    except ValueError:
        print("Esse valor é inválido")
        return None

def validanum2(num2):
    try:
        if ope =="4" and int(num2) == 0:
            print("É impossível dividir um número por 0")
            return None
        else:
            return float(num2)
    except ValueError:
        print("Esse valor é inválido")
        return None
    
def validaope(oper):
    try:
        if 4>=int(oper)>=1:
            return int(oper)
        else:
            print("Insira um valor de 1 a 4")
            return None
    except ValueError:
        print("Esse valor é inválido")
        return None
def op(num1, op, num2):
        if op == "1":
            resul = num1+num2    
            return resul
        elif op == "2":
            resul = num1-num2    
            return resul
        elif op == "3":
            resul = num1*num2    
            return resul
        elif op == "4":
            resul = num1/num2    
            return resul

while True:
    val1 = input("Digite um número para ser feito o cálculo: ").strip()
    if validanum(val1) is not None:
        break

while True:
    ope = input("Digite '1' para realizar uma adição\nDigite '2' para realizar uma subtração\nDigite '3' para realizar uma multiplicação\nDigite '4' para realizar uma divisão\nSelecione: ").strip()
    if validaope(ope) is not None:
        break

while True:
    val2 = input("Digite o segundo número para ser feito o cálculo: ").strip()
    if validanum2(val2) is not None:
        break

print(f"O resultado do cálculo pedido é {op(validanum(val1), ope, validanum(val2))}")

print("Final do programa")