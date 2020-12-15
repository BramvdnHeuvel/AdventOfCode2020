from itertools import combinations

with open('input.txt', 'r') as open_file:
    nums = [int(n) for n in open_file]

    for a, b in combinations(nums, 2):
        if a + b == 2020:
            print(a*b)
            break
