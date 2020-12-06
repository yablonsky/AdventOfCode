def count_answers(row, target):
    return sum(row.count(c) == target for c in set(row.replace('\n', '')))


def sum_answers(input_file):
    return sum(count_answers(r, len(r.split())) for r in open(input_file).read().split('\n\n'))


assert sum_answers('input-06.txt') == 3445
