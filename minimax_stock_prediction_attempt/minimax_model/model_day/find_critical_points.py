def find_critical_points(set):

    critical_points = []
    for i in range(len(set)-2):
        if set[i + 1] - set[i] > 0 and set[i + 2] - set[i+1] < 0:
            critical_points.append(i + 1)
        elif set[i + 1] - set[i] < 0 and set[i + 2] - set[i+1] > 0:
            critical_points.append(i + 1)

    return critical_points
