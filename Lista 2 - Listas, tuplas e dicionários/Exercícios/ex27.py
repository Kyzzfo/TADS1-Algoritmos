print("====== Exercício 27 ======\nContador de palavras\n")

def contar(termo):
    contagem = {}
    for palavras in termo:
        if palavras in contagem:
            contagem[palavras] += 1
        else:
            contagem[palavras] = 1
    return contagem

frase = input("Digite uma frase para realizarmos a contagem de cada palavra na frase: ").strip().lower()
palavra = frase.split()
dici = dict(sorted(contar(palavra).items(), key=lambda item: item[1], reverse=True))

print("Palavras:")
for item, quantidade in dici.items():
    print(f"'{item}': {quantidade}")

print("Final do programa")