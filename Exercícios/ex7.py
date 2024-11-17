print("====== Exercício 7 ======\nInvertendo algo que o usuário digitou\n")

def invert(text):
    invertido = text[::-1]
    return invertido

def verifica(text):
    if text.strip() == "":
        print("Você não digitou nada ou apenas espaços. Tente novamente.")
        return None
    else:
        return True
    
print("Digite um texto e irei lhe mostrar o resultado da inversão do que você digitou")

while True:
    texto = input("Digite um texto: ").strip()
    if verifica(texto) is not None:
        break

print(f"Invertendo o que você digitou, o resultado é:\n{invert(texto)}")

print("Final do programa")