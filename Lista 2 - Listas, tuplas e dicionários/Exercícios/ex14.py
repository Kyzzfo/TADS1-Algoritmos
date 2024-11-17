print("====== Exercício 14 ======\nVerificador de palíndromos\n")

def verifica(letras):
    if letras.isalpha():
        return True
    else:
        print("Digite apenas uma palavra sem espaços ou símbolos")
        return False

def palindromo(termo):
    if termo[::-1] == termo:
        print("Essa palavra é um palíndromo")
    else:
        print("Essa palavra não é um palíndromo")

while True:
    palavra = input("Digite uma palavra para verificar se é um palíndromo: ").lower().strip()
    if verifica(palavra) == True:
        palindromo(palavra)
        break
    
print("Final do programa")