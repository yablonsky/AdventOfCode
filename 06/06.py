def sum_answers(input_file):
    data = open(input_file).read().split('\n\n')
    return sum(sum(r.count(c) == len(r.split()) for c in set(r.replace('\n', ''))) for r in data)


assert sum_answers('input-06.txt') == 3445
