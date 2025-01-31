import data_analysis as da
def feature_no_overlap(n):
    min_number_of_critical_points = min(da.number_of_critical_points)
    features = []
    if min_number_of_critical_points >= n:
        min_number_of_critical_points = n
    for i in range(da.number_of_files):
        h = 0
        v = 0
        l = da.number_of_critical_points[i] - min_number_of_critical_points
        while v != l + 1:
            features_element = []
            k = 0
            while k != min_number_of_critical_points:
                features_element.append(da.dataframes[i]['average_price_interpolated'][h])
                if da.dataframes[i]['critical_points'][h] == 1:
                    k += 1
                if k != min_number_of_critical_points:
                    h += 1
                if k == min_number_of_critical_points:
                    features_element.append(da.dataframes[i]['average_price_interpolated'][h + 1])
            features.append(features_element)
            h = da.all_critical_points_positions[i][v]+1
            v += 1
    return features