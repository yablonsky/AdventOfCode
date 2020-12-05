def calculate_seat_id(in_row):
    row = sum(2**i for i, c in enumerate(reversed(in_row[:7])) if c == 'B')
    col = sum(2**i for i, c in enumerate(reversed(in_row[-3:])) if c == 'R')

    return row * 8 + col


def find_my_seat(input_file):
    seats = sorted(calculate_seat_id(r.rstrip()) for r in open(input_file))
    mid = len(seats) // 2
    for i, (a, b) in enumerate(zip(seats[mid::-1], seats[mid:])):
        if a + i < seats[mid]:
            return a + 1
        if b - i > seats[mid]:
            return b - 1
