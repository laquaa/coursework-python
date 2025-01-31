from sympy.combinatorics import Permutation, PermutationGroup
s_4 = PermutationGroup(Permutation(1,2),Permutation(1,3),Permutation(1,4),Permutation(2,3),Permutation(2,4),Permutation(3,4))
group_elements = list(s_4.generate())
print(group_elements)
result = []
for element1 in group_elements:
    for element2 in group_elements:
        if element1*element2 != element2*element1:
            g = (~element1)*(~element2)*element1*element2
            if g not in result:
                result.append(g)
print(result)
print(len(result))
B = PermutationGroup(Permutation(1,2,3,4),Permutation(1,3))
print(B.order())
C = PermutationGroup(Permutation(1,2),Permutation(3,4))
print(C.order())
D = PermutationGroup(Permutation(1,2,3),Permutation(1,2)(3,4))
print(D.order())
