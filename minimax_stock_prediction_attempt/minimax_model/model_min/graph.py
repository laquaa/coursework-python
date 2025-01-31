import pandas as pd
import matplotlib.pyplot as plt

data_path = 'error_order.csv'
df = pd.read_csv(data_path)

plt.figure(figsize=(15, 10))
for i in range(46):
    plt.plot(df.iloc[i])
plt.xlabel('Data Points')
plt.ylabel('error')

plt.show()