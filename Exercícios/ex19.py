print("====== Exercício 19 ======\nContar caracteres em uma frase\n")

def contar(frase):
    contagem = {}
    for letra in frase:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

frase = input("Digite uma frase para realizarmos a contagem de cada letra e espaços na frase: ").strip().lower()

dici = contar(frase)

print("Caracteres:")
for caractere, quantidade in dici.items():
    print(f"'{caractere}': {quantidade}")

print("Final do programa")