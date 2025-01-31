from sympy.combinatorics import Permutation, PermutationGroup
G = PermutationGroup(Permutation(1,2,3,4,5),Permutation(2,3,5,4))
group_elements = list(G.generate())
result = []
for element1 in group_elements:
    for element2 in group_elements:
        if element1*element2 != element2*element1:
            g = (~element1)*(~element2)*element1*element2
            if g not in result:
                result.append(g)
print(result)
print(len(result))
print(G.order())
B = PermutationGroup(Permutation(1,2,3,4,5))
print(B.order())
D = PermutationGroup(Permutation(2,3,5,4))
print(D.order())
