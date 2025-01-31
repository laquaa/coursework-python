import day as da
def feature(n):
    features = []
    h = 0
    v = 0
    l = len(da.critical_points_position) - n
    while v != l + 1:
        features_element = []
        k = 0
        while k != n:
            features_element.append(da.dataframe['close_interpolated'][h])
            if da.dataframe['critical_points'][h] == 1:
                k += 1
            if k != n:
                h += 1
            if k == n:
                features_element.append(da.dataframe['close_interpolated'][h + 1])
        features.append(features_element)
        h = da.critical_points_position[v]+1
        v += 1
    return features
