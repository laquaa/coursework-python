def choose_critical_points(critical_points):

    output = []
    for n in range(33):
        num = int((len(critical_points)-1)*(n/32))
        output.append(critical_points[num])

    return output
