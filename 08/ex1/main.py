encountered_lines = []
file_content = [line.strip() for line in open('input.txt', 'r')]

i = 0
accumulator = 0

while i not in encountered_lines:
    encountered_lines.append(i)
    code = file_content[i].split(' ')

    if code[0] == 'nop':
        i += 1
    elif code[0] == 'acc':
        accumulator += int(code[1])
        i += 1
    elif code[0] == 'jmp':
        i += int(code[1])

else:
    print(accumulator)