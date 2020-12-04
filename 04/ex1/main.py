from typing import List, Dict

def lines_to_dic(lines : List[str]) -> Dict[str, str]:
    dic = {}

    for line in lines:
        for obj in line.split(' '):
            key, value = obj.split(':')[0], obj.split(':')[1]
            dic[key] = value
    return dic

def dic_is_complete(dic : Dict[str, str]) -> bool:
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if key not in dic:
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