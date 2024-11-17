from unicodedata import *

print("====== Exercício 24 ======\nVerificar anagrama\n")

def tiraacento(pal):
    return ''.join(c for c in pal if category(c) != 'Mn')

def valida(letras):
        if letras.isalpha():
            return True
        else:
            print("Digite apenas uma palavra sem espaços, números ou símbolos")
            return False
    

while True:
    pal1 = input("Digite uma palavra sem números e sem espaços: ").lower().strip()
    if valida(pal1):
        break
pal1n = tiraacento(normalize("NFD",pal1))

while True:
    pal2 = input("Digite outra palavra sem números: ").lower().strip()
    if valida(pal2):
        break

pal2n =  tiraacento(normalize("NFD",pal2))

if sorted(pal1n) == sorted(pal2n):
    print(f"As palavras {pal1} e {pal2} são anagramas uma da outra")
else:
    print(f"As palavras {pal1} e {pal2} não são anagramas uma da outra")

print("Final do programa")