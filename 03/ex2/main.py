def calculate_for_direction(x_dir, y_dir):
    def generate_coordinates(mod_len, max_depth):
        x = 0
        y = 0
        while x < max_depth:
            yield x, y
            x, y = x+y_dir, (y+x_dir)%mod_len

    field = [line.strip() for line in open('input.txt', 'r')]
    has_tree = lambda x, y : field[x][y] == '#'

    trees = 0

    for x, y in generate_coordinates(len(field[0]), len(field)):
        if has_tree(x, y):
            trees += 1

    return trees

tot = 1

for directions in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    tot = tot * calculate_for_direction(*directions)

print(tot)