from itertools import repeat


def iter_visible(seats, j, i):
    ranges = [
        zip(repeat(j), range(i + 1, len(seats[0]))),
        zip(repeat(j), range(i - 1, -1, -1)),
        zip(range(j + 1, len(seats)), repeat(i)),
        zip(range(j - 1, -1, -1), repeat(i)),
        zip(range(j + 1, len(seats)), range(i + 1, len(seats[0]))),
        zip(range(j + 1, len(seats)), range(i - 1, -1, -1)),
        zip(range(j - 1, -1, -1), range(i + 1, len(seats[0]))),
        zip(range(j - 1, -1, -1), range(i - 1, -1, -1)),
    ]

    for range_ in ranges:
        for n, m in range_:
            if seats[n][m] != '.':
                yield seats[n][m]
                break


def seat(seats, s, j, i):
    if s == '.':
        return '.'

    num_occupied = sum(s == '#' for s in iter_visible(seats, j, i))
    if s == 'L' and num_occupied == 0:
        return '#'
    if s == '#' and num_occupied >= 5:
        return 'L'

    return s


def simulate(raw_data):
    seats = [l.replace('L', '#') for l in raw_data]
    new_seats = []

    while seats != new_seats:
        seats = new_seats or seats
        new_seats = [''.join(seat(seats, s, j, i) for i, s in enumerate(r)) for j, r in enumerate(seats)]

    return sum(r.count('#') for r in new_seats)


assert simulate(open('input-11.txt')) == 2149
