intervals = []

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
    
for line in d['ticket fields']:
    inters = line.split(':')[1][1:].split(' or ')
    
    for interval in inters:
        nums = interval.split('-')
        interval = (int(nums[0]), int(nums[1]))
        
        to_remove = []

        # Merge with existing interval
        for existing in intervals:
            if existing not in to_remove and (
                (existing[0]-1 <= interval[0] <= existing[1]+1) or
                (existing[0]-1 <= interval[1] <= existing[1]+1) or
                (interval[0]-1 <= existing[0] <= interval[1]+1) or
                (interval[1]-1 <= existing[1] <= interval[1]+1)
            ):
                interval = (min(interval[0], existing[0]), max(interval[1], existing[1]))
                to_remove.append(existing)
        else:
            intervals.append(interval)

        for tup in to_remove:
            intervals.remove(tup)

print(intervals)

def in_interval(intervals, num):
    for low, high in intervals:
        if low <= num <= high:
            return True
    else:
        return False

tot = 0

for ticket in d['nearby tickets']:
    for t in ticket.split(','):
        if not in_interval(intervals, int(t)):
            tot += int(t)
            break

print(tot)
