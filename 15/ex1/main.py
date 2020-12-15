

memory = [int(line.strip()) for line in open('input.txt', 'r')]

while len(memory) < 2020:
    old = memory[:-1]
    old.reverse()

    last_number = memory[-1]

    if last_number in old:
        memory.append(old.index(last_number)+1)
    else:
        memory.append(0)

print(memory[-1])

