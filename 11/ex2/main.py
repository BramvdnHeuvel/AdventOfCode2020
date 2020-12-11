def iterate_occupied_neighbours(lijst, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if x+i < 0 or y+j < 0:
                continue

            try:
                mult = 1
                spot = lijst[x+(mult*i)][y+(mult*j)]
                while spot == '.' and (x+(mult*i) > 0 or i==0) and (y+(mult*j) > 0 or j==0):
                    mult += 1
                    spot = lijst[x+(mult*i)][y+(mult*j)]
            except IndexError:
                continue
            else:
                yield spot

def count_occupied_neighbours(lijst, x, y):
    return len([n for n in iterate_occupied_neighbours(lijst, x, y) if n == '#'])

waiting_area = [[c for c in line.strip()] for line in open('input.txt', 'r')]

changes_made = True

while changes_made:
    seats_to_occupy = []
    seats_to_free   = []

    for i in range(len(waiting_area)):
        for j in range(len(waiting_area[0])):
            if waiting_area[i][j] == '.':
                continue

            occupied_neighbouring_seats = count_occupied_neighbours(waiting_area, i, j)

            if occupied_neighbouring_seats == 0 and waiting_area[i][j] == 'L':
                seats_to_occupy.append((i, j))
            
            if occupied_neighbouring_seats >= 5 and waiting_area[i][j] == '#':
                seats_to_free.append((i, j))

    changes_made = (len(seats_to_free) + len(seats_to_occupy) > 0)

    for x, y in seats_to_occupy:
        waiting_area[x][y] = '#'
    for x, y in seats_to_free:
        waiting_area[x][y] = 'L'

    #for line in waiting_area:
    #    print(''.join(line))
    #print(changes_made)
    #
    #input()

print(sum([len([c for c in line if c == '#']) for line in waiting_area]))
