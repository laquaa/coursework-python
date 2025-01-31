from model_parameter import model_training
from features import feature
import pandas as pd
results = pd.DataFrame()
all_error = []
for i in range(len(feature(40))):
    result = model_training(40, i)
    all_error.append(result[1])
for i in range(len(all_error[0])):
    column_data = []
    for j in range(len(all_error)):
        a = all_error[j][i]
        column_data.append(a)
    results[str(i)] = column_data
results.to_csv('error_order_40_start_from_num=2.csv')