# [(25, 974)] is the interval - determined in the last exercise
INTERVAL_MIN = 25
INTERVAL_MAX = 974
TICKET_VALUES = 20

def valid_tickets():
    for line in get_file_data()['nearby tickets']:
        ticket = [int(t) for t in line.split(',')]

        for t in ticket:
            if not (INTERVAL_MIN <= t <= INTERVAL_MAX):
                break
        else:
            yield ticket

def get_file_data():
    d = {
        'ticket fields' : [],
        'your ticket'   : [],
        'nearby tickets': []
    }

    state = 'ticket fields'
    for line in open('input.txt', 'r'):
        line = line.strip()
        if line == '':
            continue
        elif line.endswith(':'):
            state = line[:-1]
        else:
            d[state].append(line)
    return d

values = [[] for _ in range(TICKET_VALUES)]

for ticket in valid_tickets():
    for i, t in zip(range(TICKET_VALUES), ticket):
        values[i].append(t)

options = get_file_data()['ticket fields']
options = {o.split(':')[0] : [(int(i.split('-')[0]), int(i.split('-')[1])) for i in o.split(': ')[1].split(' or ')] for o in options}

def option_interval(option, existing_values):
    for value in existing_values:
        for low, high in option:
            if low <= value <= high:
                break
        else:
            return False
    else:
        return True

with open('options.txt', 'w') as write_file:
    for v in values:
        possible_options = []
        for option in options:
            if option_interval(options[option], v):
                possible_options.append(option)
        
        write_file.write(','.join(possible_options))
        write_file.write('\n')