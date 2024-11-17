print("====== Exercício 4 ======\nContador de caracteres de uma palavra\n")

def verifica(letras):
    if " " in letras:
        print("Você digitou mais de uma palavra ou um espaço. Tente novamente")
        return False
    elif not letras:
        print("Você não digitou nada. Tente novamente.")
        return False
    else:
        return True

def contar(palavrac):
    return len(palavrac)

while True:
    palavra = input("Digite apenas uma palavra (sem espaços): ").strip()
    if verifica(palavra):
        break

print(f"A palavra '{palavra}' tem {contar(palavra)} caracteres.")
print("Final do programa")