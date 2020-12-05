def count_path_trees(tree_map, y, x):
    n, m = len(tree_map), len(tree_map[0])
    return sum(1 for i, r in zip(range(y, n*y, y), tree_map[x::x]) if r[i%m] == '#')

def traverse_map(tree_map):
    dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    counts = [count_path_trees(tree_map, *c) for c in dirs]
    return counts[0] * counts[1] * counts[2] * counts[3] * counts[4] 
