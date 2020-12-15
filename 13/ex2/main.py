from functools import reduce
from typing import List

PRODUCT = 1463175673841141

# -----------------------------------------
with open('input.txt', 'r') as open_file:
    _ = int(open_file.readline().strip())
    bus_lines = open_file.readline().strip().split(',')


bus_lines = [(i, int(b)) for i, b in zip(range(len(bus_lines)), bus_lines) if b != 'x']

timestamp = 0

while True:
    prod = 1
    for off_set, n in bus_lines:
        if (timestamp + off_set) % n == 0:
            prod = prod * n
        else:
            break
    else:
        print(timestamp)
        break

    timestamp += prod

