import numpy as np

a = [1, 2, 3]
b = [[1, np.array([4, 5, 6])], [2, np.array([1, 2, 3])], [0, np.array([1, 2, 3])]]

a = np.array(a)
a = [0, a]
print(a)
print(a in b)