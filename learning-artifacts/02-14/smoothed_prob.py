def smoothed_prob(count, total, vocab):
    return (count + 1) / (total + vocab)

if __name__ == "__main__":
    print(round(smoothed_prob(80, 150, 3), 4))
    print(round(smoothed_prob(0, 150, 3), 4))
    print(round(smoothed_prob(100, 115, 3), 4))
