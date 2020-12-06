def count_answers(group, target):
    return sum(group.count(c) == target for c in set(group.replace('\n', '')))


def sum_answers(input_file):
    return sum(count_answers(g, len(g.split())) for g in open(input_file).read().split('\n\n'))


assert sum_answers('input-06.txt') == 3445
