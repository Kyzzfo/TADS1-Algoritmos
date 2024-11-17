print("====== Exercício 10 ======\nCalcular área de um retângulo\n")

def valida(comp):
    try:
        if float(comp)>0:
            return float(comp)
        else:
            print("O valor do comprimento deve ser maior do que 0")
            return None
    except ValueError:
        print(" Esse valor não é valido.")
        return None

def area(bas, alt):
    are = bas*alt
    return are

while True:
    base = (input("Digite o valor do comprimento da base do retângulo: ")).strip()
    if valida(base) is not None:
        basi = valida(base)
        print(f"O comprimento da base do retângulo é de {basi}")
        break

while True:
    altu = (input("Digite o valor do comprimento da altura do retângulo: ")).strip()
    if valida(altu) is not None:
        heig = valida(altu)
        print(f"O comprimento da altura do retângulo é de {heig}")
        break

print(f"O valor da área do retângulo de base {basi} e altura {heig} é de {area(basi,heig)} ")

print("Final do programa")