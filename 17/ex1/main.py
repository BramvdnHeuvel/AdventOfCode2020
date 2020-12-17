from itertools import permutations
from typing import List, Tuple, Dict

def load_cubes() -> List[Tuple[int, int, int]]:
    cubes : List[Tuple[int, int, int]] = []

    for line, x in zip(open('input.txt', 'r'), range(8)):
        for c, y in zip(line.strip(), range(8)):
            if c == '#':
                cubes.append((x, y, 0))

    return cubes

def determine_format(cubes : List[Tuple[int, int, int]]) -> Dict[str, int]:
    return {
        'min_x' :   min([c[0] for c in cubes]),
        'max_x' :   max([c[0] for c in cubes]),
        'min_y' :   min([c[1] for c in cubes]),
        'max_y' :   max([c[1] for c in cubes]),
        'min_z' :   min([c[2] for c in cubes]),
        'max_z' :   max([c[2] for c in cubes])
    }

def zero_distance(a : Tuple[int, int, int], b : Tuple[int, int, int]) -> int:
    return max([
        abs(a[0]-b[0]), 
        abs(a[1]-b[1]), 
        abs(a[2]-b[2])
    ])

def new_cube_gen(old : List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    cubes = []
    dic = determine_format(old)

    for x in range(dic['min_x']-1, dic['max_x']+2):
        for y in range(dic['min_y']-1, dic['max_y']+2):
            for z in range(dic['min_z']-1, dic['max_z']+2):
                cube = (x, y, z)
                neighbours = len([c for c in old if zero_distance(cube, c) == 1])

                if cube in old and 2 <= neighbours <= 3:
                    cubes.append(cube)
                elif cube not in old and neighbours == 3:
                    cubes.append(cube)
    
    return cubes



cubes = load_cubes()

for _ in range(6):
    cubes = new_cube_gen(cubes)

print(len(cubes))

