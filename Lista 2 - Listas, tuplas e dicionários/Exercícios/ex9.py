print("====== Exercício 9 ======\nVerificador de maioridade\n")

def maioridade(idade):
    try:
        age = int(idade)
        if age>=18:
            print(f"Você tem {age} anos, o que significa que é maior de idade")
            return True
        elif 0<=age<=17:
            print(f"Você tem {age} anos, o que significa que é menor de idade")
            return False
        elif age<0:
            print("Essa não é uma idade válida.")
            return None
    except ValueError:
        print("Isso não é uma idade válida.")
        return None

while True:
    idad= input("Digite sua idade em números:").strip()
    if maioridade(idad) is not None:
        break
        
print("Final do programa")