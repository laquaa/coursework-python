import pandas as pd
import find_critical_points as fcp
import find_polynomials as ap2
import find_variables as ap3
import sympy as sp

original_data = pd.read_excel("AAPL_ap_coefficients.xlsx")

day_data = pd.read_excel("day.xlsx")
day = day_data['day'][0]

all_functions_coefficients = []
for i in range(33):
    data = []
    i = i+1
    for j in range(day):
        data.append(original_data[i][j])

    print(data)

    critical_points = fcp.find_critical_points(data)
    polynomials = ap2.approximation_function(critical_points)
    print(critical_points)
    variables = ap3.approximation_variables(polynomials)
    #print(variables)
    solutions = None
    final_functions = []
    for k in range(len(critical_points)):
        error_value = data[critical_points[k]] - polynomials[k]
        #print(error_value)

        final_function = error_value + (-1) ** k * variables[0]
        final_functions.append(final_function)
    solutions = sp.solve(final_functions, variables)
    all_functions_coefficients.append(solutions)

#print(all_functions_coefficients)
#print(pd.DataFrame(all_functions_coefficients))

insertData = pd.DataFrame(all_functions_coefficients)

original_data = pd.read_excel("AAPL_ap_coefficients_by_day.xlsx")
save_data = pd.concat([insertData], axis=0)
save_data.to_excel("AAPL_ap_coefficients_by_day.xlsx", index=False)

