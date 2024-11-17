print("====== Exercício 25 ======\nFiltro de números pares\n")

lista=[]
listapar=[]
listaimpar=[]

def verifica(num):
    try:
        if num.lower() == "parar":
            return True
        elif int(num):
           lista.append(int(num))
           if len(lista) >= 2:
               print(f"Números cadastrados até agora: {lista}")
           elif len(lista) == 1: 
               print(f"Número cadastrado até agora: {lista}")
    except ValueError:
        print(" Esse valor não é valido.")
        
while True:
    nums = input("Digite Números para adicionar à lista ou 'parar' quando quiser parar: ").strip()
    if verifica(nums) is True:
        break
    
print(f"A lista que você digitou é:\n{lista}")

for i in range(len(lista)):
    if lista[i]%2:
        listaimpar.append(lista[i])
    else:
        listapar.append(lista[i])

print(f"Os números pares da sua lista são {listapar}")
print(f"Os números ímpares da sua lista são {listaimpar}")

print("Final do programa")