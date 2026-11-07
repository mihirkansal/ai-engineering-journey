from statistics import pvariance

def low_variance(columns, threshold):
    names = []
    for name, values in columns.items():
        if pvariance(values) < threshold:
            names.append(name)
    return names

if __name__ == "__main__":
    cols = {"a": [1, 1, 1, 1], "b": [1, 2, 3, 4], "c": [5, 5, 5, 6]}
    print(low_variance(cols, 0.5))
    print(low_variance(cols, 0.1))
    print(low_variance(cols, 2))
