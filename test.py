import alg3
import numpy as np
m = np.array([[1, 0, 2], [1, 4, 1], [2, 0, 1]], dtype = float)
m1 = np.array([[0, 0, 2], [1, 4, 1], [2, 0, 1]], dtype = float)
a = alg3.decompositions(m)
b,d,c=a.form_diagonal()
print("diagonal form:")
print(b)
print(d)
print(c)
b=alg3.Decompositions2(m)
print("")
b.LU()
print("")
b.LDU()
print("\n")
c=alg3.Decompositions2(m1)
c.LU()
d=alg3.decompositions(m)
print()
print("coefcients of characteristic polynom:",d.coefficients())
print()
print("eigenvctors:\n",d.eigenvectors)