from sympy.combinatorics import Permutation, PermutationGroup
x = Permutation(1,3,4)(2,5)(6,9)
y = Permutation(5,1,9)(8,6,7,2)
z = Permutation(1,6)(7,9)(2,4,5)
group = PermutationGroup(x,y,z)
print(group.order())