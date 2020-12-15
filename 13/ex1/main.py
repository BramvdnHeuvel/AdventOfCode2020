with open('input.txt', 'r') as open_file:
    timestamp = int(open_file.readline().strip())
    bus_lines = open_file.readline().strip().split(',')
    bus_lines = [b for b in bus_lines if b != 'x']

def find_first_number(num : int, limit : int) -> int:
    """
        Find the smallest multiple of `num` that
        is larger than `limit`.
    """
    i = 0
    while num*i < limit:
        i += 1
    
    return num*i

bus_lines_departures = [find_first_number(int(b), timestamp) for b in bus_lines]

print(bus_lines)
print(bus_lines_departures)

print(min(bus_lines_departures))
print(min(bus_lines_departures) - timestamp)

# Note: 2 days after completing this assignment
#
# I used this two days ago to calculate the answer as quickly as possible.
# The answer does not immediately get printed, I calculated the rest by hand.
