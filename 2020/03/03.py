def count_path_trees(tree_map, y, x):
    n, m = len(tree_map), len(tree_map[0])
    return sum(1 for i, r in zip(range(y, n*y, y), tree_map[x::x]) if r[i%m] == '#')


def traverse_map(input_file):
    data = [x.rstrip() for x in open(input_file)]
    return (count_path_trees(data, 1, 1)
            * count_path_trees(data, 3, 1)
            * count_path_trees(data, 5, 1)
            * count_path_trees(data, 7, 1)
            * count_path_trees(data, 1, 2))


assert traverse_map('input-03.txt') == 5813773056
