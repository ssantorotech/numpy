import numpy as np

matrice = np.array(
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10], 
        [11, 12, 13, 14, 15], 
        [16, 17, 18, 19, 20], 
        [21, 22, 23, 24, 25]
    ]
)

# prima della matrice
prima_riga = matrice[0]
print(prima_riga)

# ultima colonna della matrice
ultima_colonna = matrice[:, -1]
print(ultima_colonna)

# prima diagonale della matrice
diagonale = np.diag(matrice)
print(diagonale)

# ultima diagonale della matrice
ultima_diagonale = np.diag(np.fliplr(matrice))
print(ultima_diagonale)