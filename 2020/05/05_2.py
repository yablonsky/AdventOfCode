def calculate_seat_id(in_row):
    row = int(in_row[:7].replace('B', '1').replace('F', '0'), base=2)
    col = int(in_row[-3:].replace('R', '1').replace('L', '0'), base=2)

    return row * 8 + col


def find_my_seat(input_file):
    seats = sorted(calculate_seat_id(r.rstrip()) for r in open(input_file))
    mid = len(seats) // 2
    for i, (a, b) in enumerate(zip(seats[mid::-1], seats[mid:])):
        if a + i < seats[mid]:
            return a + 1
        if b - i > seats[mid]:
            return b - 1


assert find_my_seat('input-05.txt') == 559
