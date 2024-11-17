print("====== Exercício 13 ======\nLista de notas maiores que a média\n")

notas = []

def verifica(notes):
    try:
        if notes.lower() == "parar":
            return True
        elif 10>=float(notes)>=0:
           notas.append(float(notes))
           if len(notas) >= 2:
               print(f"Notas cadastradas até agora: {notas}")
           elif len(notas) == 1: 
               print(f"Nota cadastrada até agora: {notas}")
        elif float(notes):
            print("Insira uma nota de 0 a 10")
    except ValueError:
        print(" Esse valor não é valido.")
        
while True:
    nota = input("Digite as notas dos alunos de 1 a 10 ou 'parar' quando acabar as notas: ").strip()
    if verifica(nota) is True:
        break

media = sum(notas)/len(notas)
maior = []
for i in notas:
    if i>media:
        maior.append(i)
        
if len(notas) >= 2:
    print(f"As notas inseridas foram: {notas}")
    print(f"A média das notas é {media}")    
    if len(maior) >= 2:
        print(f" As notas maiores que a média são: {maior}")  
    elif len(maior) == 1:
        print(f"A única nota maior que a média foi {maior}")
    else:
        print("Nenhuma nota foi maior que a média")
elif len(notas) == 1:
    print(f"A única nota é {media}")
else:
    print("Não foi inserida nenhuma nota")

print("Final do programa")