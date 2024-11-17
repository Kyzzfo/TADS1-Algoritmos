print("====== Exercício 26 ======\nMesclagem de dicionários\n")

dici1 = {
    "n1" : 1,
    "n2" : 2,
    "n3" : 3,
    "n4" : 4
}
dici2 = {
    "n2" : 5,
    "n6" : 6,
    "n4" : 7,
    "n5" : 8
}

dici3 = {}

def mescla(dicini, dicifim):
    for i in dicini.keys():
        if i in dicifim.keys():
            dicifim[i]+=dicini[i]
        else:
            dicifim[i]=dicini[i]

print(f"Dados os dicionarios\n{dici1}\n{dici2}")

mescla(dici1, dici3)
mescla(dici2, dici3)

print(f"Mesclando ambos, e somando as chaves de mesmo nome, o resutado é\n{dici3}")

print("Final do programa")