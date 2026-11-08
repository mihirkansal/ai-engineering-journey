# Lesson 20: PSI, typed by the learner
import math

def psi(expected, actual):
    total = 0
    for e, a in zip(expected, actual):
        total += (a - e) * math.log(a / e)
    return total


if __name__ == '__main__':
    print(round(psi([0.5, 0.4, 0.1], [0.3, 0.4, 0.3]), 4))
    print(psi([0.5, 0.4, 0.1], [0.5, 0.4, 0.1]))
    print(round(psi([0.3, 0.4, 0.3], [0.5, 0.4, 0.1]), 4))
