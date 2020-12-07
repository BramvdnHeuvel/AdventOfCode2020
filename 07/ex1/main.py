# Build the dic
dic = {}

for line in open('input.txt', 'r'):
    line = line.strip()

    bag = line.split('contain')[0].strip()

    if line.split('contain')[1] == ' no other bags.':
        sub_bags = []
    else:
        sub_bags = line.split('contain')[1].strip()
        sub_bags = [sub_bag.strip() for sub_bag in sub_bags[:-1].split(',')]
    
    dic[bag] = sub_bags

# Calculate the value
tot = 0

def can_hold_shiny_gold(dic, value):
    if value == 'shiny gold bags':
        dic[value] = True
        return True

    if dic[value] in [True, False]:
        return dic[value]

    if 'shiny gold bags' in dic[value]:
        dic[value] = True
        return True
    
    for bag in dic[value]:
        bag = bag[2:] + ('s' if bag[-1] == 'g' else '')
        if can_hold_shiny_gold(dic, bag):
            dic[value] = True
            return True
    else:
        return False

for bag in dic:
    tot += int(can_hold_shiny_gold(dic, bag))

print(tot-1)
