from itertools import combinations

def three_sum(data, target):
    for a, b, c in combinations(data, 3):
        if a + b + c == target:
            return a * b * c
