import sympy as sp
def approximation_function(set):
    polynomials = []
    ap_f = 0
    c_x = locals()
    for j in range(len(set)):
       for i in range(len(set)-1):
           c_x['c'+str(i)] = sp.Symbol('c'+str(i))
           ap_f = (set[j]**i) * (c_x['c'+str(i)]) + ap_f
       polynomials.append(ap_f)
       ap_f = 0
    return polynomials
