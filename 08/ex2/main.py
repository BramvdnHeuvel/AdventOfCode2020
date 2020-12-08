
def simulate_program(file_content, flipped_value):
    encountered_lines = []
    i = 0
    accumulator = 0

    while i not in encountered_lines:
        if i == len(file_content):
            # Program has reached end of file
            break

        encountered_lines.append(i)
        code = file_content[i].split(' ')

        if code[0] == 'nop' or (code[0] == 'jmp' and i == flipped_value):
            i += 1
        elif code[0] == 'acc':
            accumulator += int(code[1])
            i += 1
        elif code[0] == 'jmp' or (code[0] == 'nop' and i == flipped_value):
            i += int(code[1])

    else:
        return None
    
    return accumulator

# -----------------------------------
file_content = [line.strip() for line in open('input.txt', 'r')]

for instruction, i in zip(file_content, range(len(file_content))):
    if instruction.split(' ')[0] not in ['acc', 'jmp']:
        continue

    if (outcome := simulate_program(file_content, i)) is not None:
        print(outcome)
