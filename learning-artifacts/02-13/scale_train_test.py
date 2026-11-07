def scale_train_test(train, test):
    both = train
    mean = sum(both) / len(both)
    spread = (sum((x - mean) ** 2 for x in both) / len(both)) ** 0.5
    return [(x - mean) / spread for x in test]

if __name__ == "__main__":
    print([round(v, 2) for v in scale_train_test([1, 2, 3], [10, 12])])
    print([round(v, 2) for v in scale_train_test([10, 20, 30], [20])])
