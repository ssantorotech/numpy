import numpy as np

new_array = np.arange(1, 25)
print('New_array: \n', new_array)
reshaped_array = np.reshape(new_array, (4, 6))
print('Reshaped array: \n', reshaped_array)
re_reshaped_array = np.reshape(reshaped_array, (3, 8))
print('Re-reshaped array: \n', re_reshaped_array)