from itertools import combinations

with open('input.txt', 'r') as open_file:
    nums = [int(n) for n in open_file]

    for a, b, c in combinations(nums, 3):
        if a + b + c == 2020:
            print(a*b*c)
            break
