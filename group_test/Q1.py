from sympy.combinatorics import Permutation
x = Permutation(1,3,4)(2,5)(6,9)
y = Permutation(5,1,9)(8,6,7,2)
print(x*y)