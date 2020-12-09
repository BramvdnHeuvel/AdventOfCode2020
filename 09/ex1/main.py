def sum_can_be_made(number, previous_numbers):
    for a in previous_numbers:
        for b in previous_numbers:
            if a+b == number:
                return True
    
    return False

nums = [int(line.strip()) for line in open('input.txt', 'r')]

for i in range(25, len(nums)):
    if not sum_can_be_made(nums[i], nums[i-25:i]):
        print(nums[i])
        break