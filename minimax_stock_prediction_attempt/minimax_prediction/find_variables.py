import sympy as sp
import find_polynomials as ap2

def approximation_variables(set):
    ap_set = ap2.approximation_function(set)
    A = sp.Symbol('A')
    variables = [A]
    c_x = locals()
    for i in range(len(set)-1):
        c_x['c' + str(i)] = sp.Symbol('c' + str(i))
        variables.append(c_x['c' + str(i)])

    return variables
