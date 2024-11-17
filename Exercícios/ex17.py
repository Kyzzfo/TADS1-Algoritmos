print("====== Exercício 17 ======\nOrdenar lista de números\n")

lista = [-2, 3, -1, 2, 0, 8, 6, 2, -6, -1]
listaok = []

def ordena(listao):
    for i in range(len(listao)-1,-1,-1):
        if listao[i]<0:
            listaok.insert(0, listao[i])
        else:
            listaok.append(listao[i])

ordena(lista)

print (f"Ordenando a lista:\n{lista}\npara que o resultado seja com os números positivos na frente dos negativos, mas sem mudar a ordem original\no resultado é:\n{listaok}")

print("Final do programa")