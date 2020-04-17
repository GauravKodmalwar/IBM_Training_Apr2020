import numpy as np
print(np.zeros((3,4)).reshape(2,6))
print(np.eye(6))

print(np.arange( 1, 100, 7 ))

A = np.array([5,6,7,3,5,7,1,4,7,9,2,8]).reshape((3,4))
B = np.array([5,6,7,3,5,7,1,4,7,9,2,8]).reshape((4,3))

print(A.dot(B))

print(A)
print(np.sum(A, axis=1))
print(np.sum(A, axis=0))

print(A.T)
print(A.ravel())



