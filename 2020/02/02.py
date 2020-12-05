import re


def count_chars(t, c, a, b):
    return [a < len(t) and t[a], b < len(t) and t[b]].count(c)


def test_passwords_new(input_file):
    passport_re = re.compile(r'(?P<a>\d+)-(?P<b>\d+) (?P<c>\w+): (?P<p>\w+)')
    rows = (passport_re.match(row).groupdict() for row in open(input_file))
    return sum(1 for p in rows if count_chars(p['p'], p['c'], int(p['a']) - 1, int(p['b']) - 1) == 1)


assert test_passwords_new('input-02.txt') == 472
