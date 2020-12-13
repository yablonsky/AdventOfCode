def rotate(e, s, r, v):
    if r == 'R' and v == 90 or r == 'L' and v == 270:
        return -s, e
    if r == 'L' and v == 90 or r == 'R' and v == 270:
        return s, -e
    return (-e, -s) if v == 180 else (e, s)


def mhtn_dist(raw_data):
    actions = [(l[0], int(l[1:])) for l in raw_data]
    e, s, we, ws = 0, 0, 10, -1

    for a, v in actions:
        if a == 'F':
            e, s = e + we * v, s + ws * v
        elif a in 'RL':
            we, ws = rotate(we, ws, a, v)
        elif a in 'NS':
            ws += -v if a == 'N' else v
        else:
            we += -v if a == 'W' else v

    return abs(e) + abs(s)


assert mhtn_dist(open('input-12.txt')) == 29895
