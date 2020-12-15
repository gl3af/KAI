def solve(value):
    return value ** 2


def find(start, stop, accuracy):
    m = (stop + start) / 2
    if round(abs(solve(m) - 2), 2) == accuracy:
        print(m)
        exit()
    elif solve(m) > 2:
        find(start, m, accuracy)
    elif solve(m) < 2:
        find(m, stop, accuracy)


find(0, 5, 0.01)
