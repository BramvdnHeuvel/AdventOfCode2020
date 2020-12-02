policy = lambda mn, mx, c, pwd : (mn <= len([ch for ch in pwd if ch == c]) <= mx)

def unparse(text):
    mn  = text.split('-')[0]
    mx  = text.split('-')[1].split(' ')[0]
    c   = text.split(':')[0][-1]
    pwd = text.split(' ')[-1]
    return int(mn), int(mx), c, pwd

print(
    len([line.strip() for line in open('input.txt', 'r') if policy(*unparse(line.strip()))])
)