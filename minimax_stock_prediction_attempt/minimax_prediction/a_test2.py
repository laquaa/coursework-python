import pandas as pd
import numpy as np
import find_critical_points as fcp
import find_polynomials as ap2
import find_variables as ap3
import sympy as sp
import efinance as ef


day_data = pd.read_excel("day.xlsx")
day = day_data['day'][0]
stock_code = 'AAPL'
freq = 1
df = ef.stock.get_quote_history(stock_code, klt=freq)
df.to_csv(f'{stock_code + str(day)}.csv', encoding='utf-8-sig', index=None)

print(f'stock: {stock_code+str(day)} saved in: {stock_code+str(day)}.csv ')

average_price_today = []
data_today = 'AAPL' + str(day) + '.csv'
df = pd.read_csv(data_today)
df = np.array(df)

for i in range(390):
    a = (df[i, 3] + df[i, 4]) / 2
    average_price_today.append(a)

critical_points = fcp.find_critical_points(average_price_today)
polynomials = ap2.approximation_function(critical_points)
variables = ap3.approximation_variables(polynomials)

solutions = None
final_functions = []
for j in range(len(critical_points)):
    error_value = average_price_today[critical_points[j]] - polynomials[j]
    final_function = error_value + (-1)**j *variables[0]
    final_functions.append(final_function)

solutions = sp.solve(final_functions,variables)

i = day + 2

insertData1 = [day,solutions[variables[0]]]

for j in range(len(critical_points)-1):
    insertData1.append(solutions[variables[j+1]])

insertData = pd.DataFrame([insertData1])

original_data = pd.read_excel("AAPL_ap_coefficients.xlsx")
save_data = pd.concat([original_data, insertData], axis=0)
save_data.to_excel("AAPL_ap_coefficients.xlsx", index=False)

print(solutions)

day += 1
day_insertData = pd.DataFrame([{'day': day}])
day_save_data = pd.concat([day_insertData], axis=0)
day_save_data.to_excel("day.xlsx", index=False)