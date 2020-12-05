def test_passwords_new(policies):
    def count_chars(text, char, a, b):
        return (a < len(text) and text[a] == char) + (b < len(text) and text[b] == char)

    return sum(1 for p in policies if count_chars(p.p, p.c, p.a, p.b) == 1)
