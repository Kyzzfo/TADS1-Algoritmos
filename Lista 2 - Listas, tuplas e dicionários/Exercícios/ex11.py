print("====== Exercício 11 ======\nContar palavras únicas em uma frase\n")

def contador(frase):
    uni = set(frase.split())    
    return uni

fra = input("Digite uma frase:").lower().strip()

unic = contador(fra)

if 0<len(unic)<2:
    print(f"A frase que você digitou tem {len(unic)} única palavra")
elif len(unic)<1:
    print("A frase que você digitou não tem nenhuma palavra")
elif 2<=len(unic):
    print(f"A frase que você digitou tem {len(unic)} palavras únicas")
    
print("Final do programa")