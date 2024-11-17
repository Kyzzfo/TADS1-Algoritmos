from unicodedata import *
print("====== Exercício 22 ======\nContar vogais e consoantes em uma lista\n")

vogal = 0
conso = 0

def valida(frase):
    global vogal, conso
    for i in range(len(frase)):
        if frase[i].isalpha():
            if frase[i] in "aeiou":
                vogal += 1
            else:
                conso += 1        
        
termo = input("Digite uma frase, e será feita uma contagem de quantas vogais e consoantes ela tem: ").strip().lower()
termo = normalize("NFD",termo)

valida(termo)
print(f"O número de vogais é {vogal}")
print(f"O número de consoantes é {conso}")

print("Final do programa")