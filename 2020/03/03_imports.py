from functools import reduce
from operator import mul
from itertools import count

def count_path_trees(tree_map, y, x):
    return sum(1 for i, r in zip(count(y, y), tree_map[x::x]) if r[i%len(r)] == '#')


def traverse_map(tree_map, dirs):
    return reduce(mul, (count_path_trees(tree_map, *c) for c in dirs))


dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
real_input = [x.rstrip() for x in open('input-03.txt').readlines()]
assert traverse_map(real_input, dirs) == 5813773056
