from sympy.combinatorics import Permutation, PermutationGroup
s_5 = PermutationGroup(Permutation(1,2),Permutation(1,3),Permutation(1,4),Permutation(1,5),Permutation(2,3),Permutation(2,4),Permutation(2,5),Permutation(3,4),Permutation(3,5),Permutation(4,5))
print(s_5.order())
group_elements = list(s_5.generate())
print(group_elements)
result = []
while True:
    for element1 in group_elements:
        for element2 in group_elements:
            if element1*element2 != element2*element1:
                g = (~element1)*(~element2)*element1*element2
                if g not in result:
                    result.append(g)
    if result != []:
        print(result)
        group_elements = result
        result = []
    elif result == []:
        print('solvable')
        break