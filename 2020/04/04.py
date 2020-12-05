def count_valid_passports(input_file):
    data = (p.split() for p in open(input_file).read().split('\n\n'))
    data = (dict(f.split(':') for f in p) for p in data)

    return sum(validate_passport(p) for p in data)


def validate_passport(passport):
    return (
        set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']).issubset(passport.keys())
        and 1920 <= int(passport['byr']) <= 2002
        and 2010 <= int(passport['iyr']) <= 2020
        and 2020 <= int(passport['eyr']) <= 2030
        and (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193
             or passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76)
        and (len(passport['hcl']) == 7
             and passport['hcl'].startswith('#') 
             and all(c in "0123456789abcdef" for c in passport['hcl'][1:]))
        and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        and (len(passport['pid']) == 9 and passport['pid'].isnumeric())
    )


assert count_valid_passports('input-04.txt') == 158
