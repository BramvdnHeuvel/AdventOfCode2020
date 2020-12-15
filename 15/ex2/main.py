from typing import Dict, Tuple, Union
import time

now = time.time()

numbers       : int = 0
last_position : Dict[int, Tuple[int, Union[int, None]]] = {}
previous_num  : int = None

# Start with the file
for line in open('input.txt', 'r'):
    current_number = int(line.strip())
    numbers        += 1

    if current_number not in last_position:
        last_position[current_number] = (numbers, None)
    else:
        t = last_position[current_number]
        last_position[current_number] = (numbers, t[0])

# Now make the new numbers
while numbers < 30000000:
    previous_num = current_number
    numbers      += 1

    # Find out the next number
    if last_position[previous_num][1] == None:
        current_number = 0
    else:
        t = last_position[previous_num]
        current_number = t[0] - t[1]
    
    # Register the next number
    if current_number in last_position:
        last_position[current_number] = (numbers, last_position[current_number][0])
    else:
        last_position[current_number] = (numbers, None)
    
    if numbers % 1000000 == 0:
        print(numbers)

print(current_number)
print("\nTIME:")
print(time.time() - now)
