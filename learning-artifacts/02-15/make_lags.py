def make_lags(series, n_lags):
    rows = []
    for t in range(n_lags, len(series)):
        features = series[t - n_lags : t]
        target = series[t]
        rows.append((features, target))
    return rows


if __name__ == "__main__":
    print(make_lags([10, 12, 14, 13, 15], 2))
    print(make_lags([1, 2, 3, 4, 5, 6], 3))
