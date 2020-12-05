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

highest = 0

for line in open('input.txt', 'r'):
    line = line.strip()

    row = determine_range(0, 127, 'F', 'B', line)
    col = determine_range(0, 7, 'L', 'R', line[-3:])

    num = 8*row + col
    print(row, col, num)

    highest = max(highest, num) 

print(highest)