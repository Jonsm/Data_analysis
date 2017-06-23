import numpy as np

r1 = 0.571371
r2 = 0.5530518
A = np.array([
    [r1, -1, 1-r1],
    [1-r2, -1, r2],
    [1, 1, 1]
])

b = np.array([0,0,1])
p = np.linalg.solve(A,b)
print p*100
print np.dot(A, p)