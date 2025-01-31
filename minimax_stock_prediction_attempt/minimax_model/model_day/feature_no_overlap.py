import day as da
from find_critical_points import find_critical_points
def feature(n):
    features = []
    h = 0
    v = 1
    l = len(da.critical_points_position)//n
    while v != l+1:
        features_element = []
        k = 0
        while k != n:
            features_element.append(da.dataframe['close_interpolated'][h])
            k = len(find_critical_points(features_element))
            h += 1
        features.append(features_element)
        h = da.critical_points_position[v*n]-1
        v += 1
    return features

