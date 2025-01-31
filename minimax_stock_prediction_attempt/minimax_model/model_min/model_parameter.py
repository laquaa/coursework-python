from minimax_approximation import minimax_approximation
from features import feature
import matplotlib.pyplot as plt
def model_training(iterations,k):
    num = 10
    learning_rate = 1
    error_list = []
    num_list = []
    for i in range(iterations):
        features = feature(num)[k]
        actual_value = features[-1]
        predicted_value = minimax_approximation(features,1)
        error = actual_value - predicted_value
        error_list.append(abs(error))
        num_list.append(num)
        num += learning_rate
    print(error_list)
    min_error = min(error_list)
    fit_number = 10 + error_list.index(min_error)

    return [num_list,error_list]

import matplotlib.pyplot as plt
a = model_training(40,10)
print(a)
plt.figure(figsize=(15, 10))
plt.plot(a[0],a[1])
plt.show()
