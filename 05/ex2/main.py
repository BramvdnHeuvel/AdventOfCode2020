def determine_range(low_num, high_num, low_char, high_char, current_string):
    size = (high_num - low_num)//2

    if low_num == high_num:
        return low_num
    
    if abs(high_num - low_num) == 1:
        return high_num if current_string[0] == high_char else low_num
    
    if current_string[0] == low_char:
        return determine_range(low_num, low_num+size, low_char, high_char, current_string[1:])
    else:
        return determine_range(high_num-size, high_num, low_char, high_char, current_string[1:])

def get_number(line):
    row = determine_range(0, 127, 'F', 'B', line)
    col = determine_range(0, 7, 'L', 'R', line[-3:])

    return 8*row + col
    

available_ids = [get_number(line.strip()) for line in open('input.txt')]
available_ids.sort()

for i in range(len(available_ids)):
    if available_ids[i] != i + 71:
        print(available_ids[i]-1)
        break
