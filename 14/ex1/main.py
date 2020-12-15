# Converters
abin = lambda n : bin(n)[2:].zfill(36)
aint = lambda n : int(n, base=2)

def apply_mask(n : int, mask : str) -> int:
    values = [(nv if m == 'X' else m) for nv, m in zip(abin(n), mask)]
    return aint(''.join(values))

mask = ''
memory = {}

for line in open('input.txt', 'r'):
    line = line.strip()

    if line.startswith('mask = '):
        mask = line[-36:]
    
    else:
        memory_key = int(line.split(']')[0].split('[')[1])
        value      = int(line.split('=')[-1][1:])

        memory[memory_key] = apply_mask(value, mask)

print(sum(memory.values()))
