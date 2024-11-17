print("====== Exercício 18 ======\nSomar números das diagonais de uma matriz\n")

print("Neste exercício, será calculada a soma das diagonais de uma matriz quadrada")

def verifica(verif):
    try:
        return int(verif)
    except ValueError:
        print(" Esse número não é válido.")
        return None
def adcsoma(som):
    for i in range(som):
        for j in range(som):
            if i == j or i + j == som - 1:
                somar.append(matri[i][j])
def adcmatr(n):
    for i in range(n):
        line = []
        for j in range(n):
            while True:
                num = input(f"Qual o valor ficará na posição {i} {j} na matriz?").strip()
                if verifica(num) is not None:
                    val = verifica(num)
                    break   
            line.append(val)
        matri.append(line)

somar = []
matri = []

while True:
    tams = input("Digite o número de linhas e colunas da matriz: ").strip()
    if verifica(tams) is not None:
        tamn = verifica(tams)
        break

print(f"Certo, a matriz terá {tamn} linhas e colunas")

adcmatr(tamn)

print("A matriz ficou assim:")
for i in matri:
    print(i)
    
adcsoma(tamn)

print(f"E o resultado das somas das diagonais é {sum(somar)}")

print("Final do programa")