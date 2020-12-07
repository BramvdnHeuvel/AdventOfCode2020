# Build the dic
dic = {}

for line in open('input.txt', 'r'):
    line = line.strip()

    bag = line.split('contain')[0].strip()

    if line.split('contain')[1] == ' no other bags.':
        sub_bags = []
    else:
        sub_bags = line.split('contain')[1].strip()
        sub_bags = [(int(sub_bag.strip().split(' ')[0]), ' '.join(sub_bag.strip().split(' ')[1:])) for sub_bag in sub_bags[:-1].split(',')]
    
    dic[bag] = sub_bags

# Calculate the value
print(dic)

def calculate_bags(dic, value):
    tot = 0

    for bag in dic[value]:
        amount = bag[0]
        name = bag[1] + ('s' if bag[1][-1] == 'g' else '')

        tot += amount + amount * calculate_bags(dic, name)
    
    return tot

print(calculate_bags(dic, 'shiny gold bags'))