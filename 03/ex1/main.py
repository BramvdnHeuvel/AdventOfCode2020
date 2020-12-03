def generate_coordinates(mod_len, max_depth):
    x = 0
    y = 0
    while x < max_depth:
        yield x, y
        x, y = x+1, (y+3)%mod_len

field = [line.strip() for line in open('input.txt', 'r')]
has_tree = lambda x, y : field[x][y] == '#'

trees = 0

for x, y in generate_coordinates(len(field[0]), len(field)):
    if has_tree(x, y):
        trees += 1

print(trees)