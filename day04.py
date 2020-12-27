import re

INPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

def parse(input):
    """Splits input into list of dict objects, each 
    containing a field and value of a passport item"""

    passports = input.split('\n\n')
    outputs = []

    for passport in passports:

        output = {}
        items = re.split(' |\n', passport)
        
        for item in items:
            key_vals = item.split(':')
            output[key_vals[0]] = key_vals[1]
        
        outputs.append(output)


    return outputs

def validate(passports):
    """Checks passports for the following fields and returns number of 
    valid passports found.

        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)
    
    """

    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = len(passports)

    for passport in passports:
        for field in fields:
            if field in passport:
                pass
            else:
                valid = valid - 1
                break
            
    return valid


def isvalid(field, value):
    """Checks a passport field and returns True if it's value 
    matches the required value
    
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

    """

    if field == 'byr':
        if  1920 <= int(value) <= 2002:
            return True
    if field == 'iyr':
        if 2010 <= int(value) <= 2020:
            return True
    if field == 'eyr':
        if 2020 <= int(value) <= 2030:
            return True
    if field == 'hgt':
        if value [-2:] == 'cm':
            if 150 <= int(value[:-2]) <= 193:
                return True
        elif value [-2:] == 'in':
            if 59 <= int(value[:-2]) <= 76:
                return True
    if field == 'hcl':
        if re.match('^#[0-9a-f]{6}$', value):
            return True
    if field == 'ecl':
        if value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            return True
    if field == 'pid':
        if re.match('^[0-9]{9}$', value):
            return True

    return False

def validate2(passports):
    """Validates the following fields for each passport 
    and returns number of valid passports found.

        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)

    """

    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid = len(passports)

    for passport in passports:
        for field in fields:
            #check if all fields present
            if field in passport:
                #check if each field is valid
                if isvalid(field, passport[field]):
                    pass
                else:
                    valid = valid - 1
                    break
            else:
                valid = valid - 1
                break
            
    return valid

assert validate(parse(INPUT)) == 2

with open('./data/day04.txt') as f:
    inputs = f.read()

    parsed = parse(inputs)
    print("Part 1:", str(validate(parsed)))

    print("Part 2:", str(validate2(parsed)))
