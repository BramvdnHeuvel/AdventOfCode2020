policy = lambda mn, mx, c, pwd : (pwd[mn-1] == c) != (pwd[mx-1] == c)

def unparse(text):
    mn  = text.split('-')[0]
    mx  = text.split('-')[1].split(' ')[0]
    c   = text.split(':')[0][-1]
    pwd = text.split(' ')[-1]
    return int(mn), int(mx), c, pwd

print(
    len([line.strip() for line in open('input.txt', 'r') if policy(*unparse(line.strip()))])
)