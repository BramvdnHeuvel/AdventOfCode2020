def sum_can_be_made(number, previous_numbers):
    for a in previous_numbers:
        for b in previous_numbers:
            if a+b == number:
                return True
    
    return False

def invalid_number(numbers):
    for i in range(25, len(numbers)):
        if not sum_can_be_made(numbers[i], numbers[i-25:i]):
            return numbers[i]

def test_slices(numbers, amount_of_numbers_to_pick):
    for i in range(len(numbers)-amount_of_numbers_to_pick):
        yield numbers[i:i+amount_of_numbers_to_pick]

nums = [int(line.strip()) for line in open('input.txt', 'r')]
invalid_number = invalid_number(nums)

nums = [nums[i] for i in range(nums.index(invalid_number))]

list_found, i = False, 0
while not list_found:
    i += 1

    for slice in test_slices(nums, i):
        if sum(slice) == invalid_number:
            list_found = True

            print(slice)
            print(min(slice)+max(slice))
    
    if list_found:
        break
    
