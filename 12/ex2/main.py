commands = [line.strip() for line in open('input.txt', 'r')]
commands = [(line[0], int(line[1:])) for line in commands]

directions = ['N', 'E', 'S', 'W']

execs = {
    'N' :   (lambda x, y, c :   (x, y + c)),
    'E' :   (lambda x, y, c :   (x + c, y)),
    'S' :   (lambda x, y, c :   (x, y - c)),
    'W' :   (lambda x, y, c :   (x - c, y)),
}

waypoint_x, waypoint_y = 10, 1
boat_x, boat_y = 0, 0

for c in commands:
    if c[0] in execs:
        waypoint_x, waypoint_y = execs[c[0]](waypoint_x, waypoint_y, c[1])

    elif c[0] == 'F':
        boat_x += c[1]*waypoint_x
        boat_y += c[1]*waypoint_y
    
    elif c[0] == 'L':
        for _ in range(c[1]//90):
            waypoint_x, waypoint_y = -1*waypoint_y, waypoint_x
    
    elif c[0] == 'R':
        for _ in range(c[1]//90):
            waypoint_x, waypoint_y = waypoint_y, -1*waypoint_x

print(boat_x, boat_y)
print(abs(boat_x) + abs(boat_y))