print("====== Exercício 28 ======\nVerificador de Sudoku\n")

def validasudoku(tabuleiro):    
    for line in tabuleiro:
        if len(set(line)) != len(line):
            return False
    for coluna in range(9):
        for lin in range(9):
            colunas = [tabuleiro[lin][coluna]]
            if len(set(colunas)) != len(colunas):
                return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrade = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    subgrade.append(tabuleiro[k][l])
            if len(set(subgrade)) != len(subgrade):
                return False
    return True

sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


if validasudoku(sudoku) == True:
    print("O tabuleiro de sudoku:")
    for linha in sudoku:
        print(linha)
    print("É válido")
else:
    print("O tabuleiro de sudoku:")
    for linha in sudoku:
        print(linha)
    print("É inválido")

print("Final do programa")