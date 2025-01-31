import coefficient_changing_by_day as ccbd
import pandas as pd

prediction_day = int(input('prediction_day_number:'))
prediction_time = int(input('prediction_time:'))

day = ccbd.day
all_coefficients = []
data = pd.read_excel("AAPL_ap_coefficients_by_day.xlsx")

columns_number = []
for i in range(32):
    i += 1
    row_index = i
    selected_row = data.iloc[row_index]
    number_of_non_nan_columns = selected_row.notna().sum()
    print(number_of_non_nan_columns)
    variables = []
    for j in range(number_of_non_nan_columns-1):
        c_x = 'c' + str(j)
        variables.append(c_x)
    print(variables)
    c_n = 0
    coefficients = []
    for k in range(number_of_non_nan_columns-1):
        print(variables[k])
        n = data[variables[k]][i]
        coefficients.append(n)

        print(coefficients)

    for k in range(len(coefficients)):
        c_n += coefficients[k]*(prediction_day**k)
        all_coefficients.append(c_n)

print(all_coefficients)
result = 0
for i in range(32):
    result += all_coefficients[i] * (prediction_time**i)

print(result)