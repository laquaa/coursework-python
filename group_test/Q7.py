from sympy.combinatorics import Permutation, PermutationGroup
E = PermutationGroup(Permutation(1,3,5,7)(2,4,6,8),Permutation(1,6)(2,5)(7,8)(3,4),Permutation(2,5)(3,4),Permutation(1,2)(3,8),Permutation(4,7)(5,6),Permutation(1,6)(7,8))
group_elements = list(E.generate())
result = []
derived_length = 0
while True:
    derived_length += 1
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
        print('derived length = '+str(derived_length))
        break