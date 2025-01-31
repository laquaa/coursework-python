from sympy.combinatorics import Permutation, PermutationGroup
v_90 = Permutation(1,2,3,4)
v_180 = Permutation(1,3)(2,4)
v_270 = Permutation(1,4,3,2)
h_90 = Permutation(1,5,3,6)
h_180 = Permutation(1,3)(5,6)
h_270 = Permutation(1,6,3,5)
R_C = PermutationGroup(v_90,v_180,v_270,h_90,h_180,h_270)
print(R_C.order())