import numpy as np


numeri = np.array([
    12, 5, 34, 21, 8,
    45, 17, 29, 3, 50,
    14, 38, 7, 26, 41,
    19, 2, 33, 11, 47
])

somma = np.sum(numeri)
media = np.mean(numeri)
minimo = np.min(numeri)
massimo = np.max(numeri)

print("Somma:", somma)
print("Media:", media)
print("Minimo:", minimo)
print("Massimo:", massimo)