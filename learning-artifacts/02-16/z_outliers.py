from statistics import mean, pstdev

def z_outliers(values, threshold):
    m = mean(values)
    s = pstdev(values)
    return [x for x in values if abs((x - m) / s) > threshold]

if __name__ == "__main__":
    d = [20, 21, 19, 22, 20, 21, 95]
    print(z_outliers(d, 2))
    print(z_outliers(d, 3))
    print(z_outliers([10, 11, 9, 10, 12, 10, 50, 11], 2))
