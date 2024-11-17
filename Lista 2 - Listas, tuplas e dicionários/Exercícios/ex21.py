print("====== Exercício 21 ======\nExcluir números duplicados de uma lista\n")

lista = []
listasem = []

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
print("A lista que você definiu é:")
print(lista)

for i in range(len(lista)):
    if lista[i] not in listasem:
        listasem.append(lista[i])
        
print("Tirando os números que estão duplicados, fica:")
print(listasem)

print("Final do programa")