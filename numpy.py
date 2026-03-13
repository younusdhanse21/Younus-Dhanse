
import numpy as np
# Creating arrays
a = np.array([1, 2, 3, 4, 5,6]).reshape(3,2)
print(a)
matrix = np.arange(12).reshape(3, 4)
print(matrix)
b = np.zeros((3, 3))        # 3x3 of zeros
print(b)
c = np.ones((2, 4))    
print(c)
d = np.arange(0, 10, 2)
d = np.arange(0, 10, 4)  
print(d)
e = np.linspace(0, 1, 5)  
print(e)
e = np.linspace(0, 1, 20)  
print(e)
print(a.ndim)
print(d.ndim)


import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Basic indexing
print(arr[0]) # 10
print(arr[-1]) # 50
print(arr[1:4]) # [20, 30, 40]

# 2D indexing
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m[1, 2]) # 6
print(m[:, 1]) # [2, 5, 8] (column)
print(m[0:2, :]) # first 2 rows

# Boolean masking
scores = np.array([85, 42, 91, 67, 73])
passed = scores[scores >= 70]
print(passed) # [85, 91, 73]

# Fancy indexing
idx = [0, 3, 4]
print(arr[idx]) # [10, 40, 50]

import numpy as np

# Scalar broadcasting
a = np.array([1, 2, 3])
print(a * 10) # [10, 20, 30]

# Array + scalar
matrix = np.ones((3, 3))
print(matrix + 5)
# [[6. 6. 6.]
# [6. 6. 6.]
# [6. 6. 6.]]

# Broadcasting rule:
# Arrays with different shapes are compatible when
# dimensions are equal OR one of them is 1

row = np.array([[1, 2, 3]]) # shape (1, 3)
col = np.array([[10],[20],[30]]) # shape (3, 1)
result = row + col
print(result)
# [[11 12 13]
# [21 22 23]
# [31 32 33]]

# Vectorized math (no loops!)
x = np.linspace(0, 2*np.pi, 5)
print(np.sin(x).round(2))
# [ 0. 0.95 0.59 -0.59 -0.95]
