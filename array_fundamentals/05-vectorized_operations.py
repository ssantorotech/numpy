import numpy as np


primo_array = np.arange(1, 13)
secondo_array = np.arange(13, 25)

def somma_array(arr1, arr2):
    new_array = arr1 + arr2
    return new_array

def sottrai_array(arr1, arr2):
    new_array = arr1 - arr2
    return new_array

def moltiplica_array(arr1, arr2):
    new_array = arr1 * arr2
    return new_array

def dividi_array(arr1, arr2):
    new_array = arr1 / arr2
    return new_array


print('Somma:', somma_array(primo_array, secondo_array))
print('Sottrazione:', sottrai_array(primo_array, secondo_array))
print('Moltiplicazione:', moltiplica_array(primo_array, secondo_array))
print('Divisione:', dividi_array(primo_array, secondo_array))
