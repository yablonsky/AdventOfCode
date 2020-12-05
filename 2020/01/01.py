from itertools import combinations


def three_sum(input_file, target=2020):
    data = (int(x) for x in open(input_file))
    for a, b, c in combinations(data, 3):
        if a + b + c == target:
            return a * b * c


assert three_sum('input-01.txt') == 253928438
