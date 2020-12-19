from typing import Tuple, List, Dict, Union, Optional, Generator

def load_file(file_name : str) -> Tuple[Dict[int, Union[str, List[str]]], List[str]]:
    d = {}
    words = []

    loading_rules = True

    for line in open(file_name, 'r'):
        line = line.strip()

        if line == '':
            loading_rules = False
            continue

        # Load rule
        elif loading_rules:
            num = int(line.split(':')[0])
            if '"' in line:
                values = line.split('"')[1]
            else:
                values = line.split(':')[1].strip().split('|')
            d[num] = values

        # Load abababbababaa sentence
        else:
            words.append(line)

    d[8] = ['42', '42 8']
    d[11] = ['42 31', '42 11 31']

    return d, words

def check_rule(line : str, 
            rules : Dict[int, Union[str, List[str]]], 
            checked_so_far : Optional[int] = 0,
            current_rule : Optional[int] = 0
    ) -> Generator[int, None, None]:
    """Find strings that match the sentence"""
    options = rules[current_rule]

    if len(line) > checked_so_far:
        # Rule is a single character
        if len(options[0]) == 1:
            if line[checked_so_far] == options:
                yield checked_so_far + 1

        # Rule is a combination of rules
        else:
            for option in options:
                subrules = [int(o) for o in option.strip().split(' ')]
                progress = set()
                progress.add(checked_so_far)

                for subr in subrules:
                    # Keep a set to prevent the generator from generating the same number over and over again.
                    previous_progress = progress
                    progress = set()

                    for p in previous_progress:
                        for new_p in check_rule(line, rules, checked_so_far=p, current_rule=subr):
                            progress.add(new_p)
                    
                yield from progress

def is_valid(line : str, rules : Dict[int, Union[str, List[str]]]) -> bool:
    """Check if the line is valid."""
    for value in check_rule(line, rules):
        if value == len(line):
            return True
    else:
        return False

rules, words = load_file('input.txt')

print(len([word for word in words if is_valid(word, rules)]))


