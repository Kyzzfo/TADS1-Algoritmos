print("====== Exercício 6 ======\nCálculo de média aritmética de 3 notas\n")

def valida(nota):
    try:
        notar = float(nota)
        if 10>=notar>=0:
            return notar
        else:
            print("Essa nota é inválida, deve ser de 0 a 10")       
    except ValueError:
        print(" Essa nota não é válida.")
    return None

def notafinal(n1,n2,n3):
    final = (n3 + n2 + n1)/3
    return final

while True:
    nota1 = (input("Digite a primeira nota de 0 a 10 para ser realizado o cálculo da média aritmética das 3 notas: ")).strip()
    if valida(nota1) is not None:
        nota11 = valida(nota1)
        print(f"Primeira nota: {nota11}")
        break
while True:
    nota2 = (input("Digite a segunda nota de 0 a 10 para ser realizado o cálculo da média aritmética das 3 notas: ")).strip()
    if valida(nota2) is not None:
        nota22 = valida(nota2)
        print(f"Segunda nota: {nota22}")
        break
while True:
    nota3 = (input("Digite a terceira nota de 0 a 10 para ser realizado o cálculo da média aritmética das 3 notas: ")).strip()
    if valida(nota3) is not None:
        nota33 = valida(nota3)
        print(f"Terceira nota: {nota33}")
        break

print(f"\nA média aritmética das notas é {notafinal(nota11, nota22, nota33)}")

print("Final do programa")