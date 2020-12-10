nums = [0] + [int(line.strip()) for line in open('input.txt', 'r')]
nums.append(max(nums) + 3)
nums.sort()

product_table = {0:1, 1:1, 2:2, 3:4, 4:7}

i = 0
number_of_ones_in_a_row = 0
possible_ways = 1

for i in range(len(nums)-1):
    last, this = nums[i], nums[i+1]

    if this-last == 3:        
        # Since looking at the data shows
        # this variable never gets higher
        # than 4, we can just hardcode
        # the solution
        possible_ways = possible_ways * product_table[number_of_ones_in_a_row]
        number_of_ones_in_a_row = 0
    else:
        number_of_ones_in_a_row += 1

print(possible_ways)
