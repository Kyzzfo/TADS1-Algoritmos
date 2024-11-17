print("====== Exercício 29 ======\nRemover elementos duplicados de listas aninhadas\n")

lista = [
    [2,2,3,4],
    [3,3,6,7],
    [9,4,4,0]
]

def remove(listas):    
    listaok = []
    for sublista in listas:
        sublistaok = []
        for item in sublista:
            if item not in sublistaok:
                sublistaok.append(item)
        listaok.append(sublistaok)
    return listaok

print(remove(lista))

print("Final do programa")