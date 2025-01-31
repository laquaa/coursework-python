import sympy as sp
from find_critical_points import find_critical_points
def minimax_approximation(data,parameter):
    critical_points = find_critical_points(data)
    symbol_names = ' '.join([f'c{i}' for i in range(len(critical_points)-1)]) + ' A'
    symbols = sp.symbols(symbol_names)
    equations = []
    for i in range(len(critical_points)):
        t = critical_points[i]
        eq = data[t]
        for j in range(len(critical_points)-1):
            eq -= symbols[j]*(t*parameter)**j
        equation = sp.Eq(symbols[-1]*(-1)**i,eq)
        equations.append(equation)
    solutions = sp.solve(equations,symbols)
    predict_next_minute = 0
    for k in range(len(critical_points)-1):
        predict_next_minute += solutions[symbols[k]]*((critical_points[-1]+1)*parameter)**k
    return predict_next_minute