import pandas as pd
import matplotlib.pyplot as plt

data_path = 'error_order_40_start_from_num=2.csv'
df = pd.read_csv(data_path)

plt.figure(figsize=(15, 20))
for i in range(df.shape[0]):
    plt.plot(df.iloc[i])
plt.xlabel('Data Points')
plt.ylabel('error')

plt.show()