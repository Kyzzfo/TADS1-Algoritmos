print("====== Exercício 5 ======\nTabuada do 1 ao 10 de um número\n")

def tabuada(tabua):
    print(f"A tabuada do número {tabua} será apresentada abaixo\n")
    for i in range(1, 11):
        print(f"{i} x {tabua} = {i*tabua}")
        
def verifi(num):
    try:        
        return int(num)
    except ValueError:
        print(" Esse número não é válido.")
        return None

while True:
    numstr = (input("Digite um número inteiro para realizarmos sua tabuada: ")).strip()
    if verifi(numstr) is not None:
        numint = verifi(numstr)
        break
    
tabuada(numint)

        
print("Final do programa")