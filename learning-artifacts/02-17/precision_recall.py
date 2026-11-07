def precision_recall(tp, fp, fn):
    precision = tp / (tp + fn)
    recall = tp / (tp + fp)
    return recall, precision

if __name__ == "__main__":
    print([round(v, 4) for v in precision_recall(9, 0, 5)])
    print([round(v, 4) for v in precision_recall(14, 8, 0)])
    print([round(v, 4) for v in precision_recall(13, 1, 1)])
