from minimax_approximation import minimax_approximation
from feature_no_overlap import feature
from find_critical_points import find_critical_points
def model_training(iterations,k,num):
    learning_rate = 1
    error_list = []
    num_list = []
    data = feature(iterations+num)[k]
    for i in range(iterations):
        sub_critical_points = find_critical_points(data)
        sub_sub_feature = data[0:(sub_critical_points[num]+1)]
        print(sub_sub_feature)
        prediction = minimax_approximation(sub_sub_feature,1)
        actual_value = sub_sub_feature[-1]
        error = actual_value - prediction
        error_list.append(error)
        num_list.append(num)
        num += learning_rate
    print(error_list)

    return [num_list,error_list]
print(model_training(40,2,10))
