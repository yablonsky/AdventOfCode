def transform_data(raw_data):
    for line in raw_data.split('.\n'):
        k, v = line.split('s contain ')
        v = [x.split(' ', 1) for x in v.split(', ')]
        v = {b.rstrip('s'): 1 if n == 'no' else int(n) for n, b in v}
        yield k, v


def count_bags(raw_data, start_bag, target_bag='other bag'):
    bags = dict(transform_data(raw_data))
    
    return bfs_sum(bags, start_bag, 1) - 1


def bfs_sum(bags, bag, count):
    if bag == 'other bag':
        return 0

    return count + (count * sum(bfs_sum(bags, b, c) for b, c in bags.get(bag, {}).items()))


assert count_bags(open('input-07.txt').read().rstrip('s.\n'), 'shiny gold bag') == 3805
