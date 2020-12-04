from typing import List, Dict

COMPLETE_VALUES = {
    'byr'   : lambda v : 1920 <= int(v) <= 2002,
    'iyr'   : lambda v : 2010 <= int(v) <= 2020,
    'eyr'   : lambda v : 2020 <= int(v) <= 2030,
    'hgt'   : lambda v : ((150 <= int(v[:-2]) <= 193) and v[-2:] == 'cm') or ((59 <= int(v[:-2]) <= 76) and v[-2:] == 'in'),
    'hcl'   : lambda v : v[0] == '#' and len([c for c in v[1:] if c in '0123456789abcdef']) == 6,
    'ecl'   : lambda v : v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid'   : lambda v : len(v) == 9 and len([c for c in v if c in '0123456789']) == 9,
    'cid'   : lambda v : True
}

def lines_to_dic(lines : List[str]) -> Dict[str, str]:
    dic = {}

    for line in lines:
        for obj in line.split(' '):
            key, value = obj.split(':')[0], obj.split(':')[1]
            dic[key] = value
    return dic

def dic_is_complete(dic : Dict[str, str]) -> bool:
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if key not in dic or not COMPLETE_VALUES[key](dic[key]):
            return False
    else:
        return True

current_passport_lines = []
tot = 0

for line in open('input.txt'):
    line = line.strip()

    if line == '':
        tot += int(dic_is_complete(lines_to_dic(current_passport_lines)))
        current_passport_lines = []
    else:
        current_passport_lines.append(line)
else:
    tot += int(dic_is_complete(lines_to_dic(current_passport_lines)))
    current_passport_lines = []

print(tot)