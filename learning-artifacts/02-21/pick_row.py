# Lesson 21: pick the newest snapshot on or before the label day, typed by the learner
def pick_row(rows, label_day):
    best = None
    for day, value in rows:
        if day <= label_day:
            best = (day, value)
    return best


if __name__ == '__main__':
    rows = [(7, 4), (14, 3), (21, 1), (28, 0)]
    print(pick_row(rows, 16))
    print(pick_row(rows, 5))
    print(pick_row(rows, 28))
    print(pick_row(rows, 14))
