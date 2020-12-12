commands = [line.strip() for line in open('input.txt', 'r')]
commands = [(line[0], int(line[1:])) for line in commands]

directions = ['N', 'E', 'S', 'W']

execs = {
    'N' :   (lambda x, y, c :   (x, y + c)),
    'E' :   (lambda x, y, c :   (x + c, y)),
    'S' :   (lambda x, y, c :   (x, y - c)),
    'W' :   (lambda x, y, c :   (x - c, y)),
}

x, y = 0, 0
direction = 1

for c in commands:
    if c[0] in execs:
        x, y = execs[c[0]](x, y, c[1])

    elif c[0] == 'F':
        d = directions[direction]
        x, y = execs[d](x, y, c[1])
    
    elif c[0] == 'L':
        direction = (direction - c[1]//90) % 4
    
    elif c[0] == 'R':
        direction = (direction + c[1]//90) % 4

print(x, y)
print(abs(x) + abs(y))