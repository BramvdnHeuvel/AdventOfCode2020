from typing import Generator, List

# Converters
abin = lambda n : bin(n)[2:].zfill(36)
aint = lambda n : int(n, base=2)

def apply_mask(n : int, mask : str) -> Generator[str, None, None]:
    values = [(nv if m == '0' else m) for nv, m in zip(abin(n), mask)]

    yield from iterate_x(values)

def iterate_x(values : List[str]) -> Generator[str, None, None]:
    if 'X' not in values:
        yield ''.join(values)
    else:
        i = values.index('X')

        values[i] = '0'
        yield from iterate_x(values)
        values[i] = '1'
        yield from iterate_x(values)
        values[i] = 'X'


mask = ''
memory = {}

for line in open('input.txt', 'r'):
    line = line.strip()

    if line.startswith('mask = '):
        mask = line[-36:]
    
    else:
        memory_key = int(line.split(']')[0].split('[')[1])
        value      = int(line.split('=')[-1][1:])

        for mem in apply_mask(memory_key, mask):
            memory[mem] = value

print(sum(memory.values()))
    