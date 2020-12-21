def get_products():
    for line in open('input.txt', 'r'):
        line = line.strip().split(' (contains ')

        ingredients = line[0].split(' ')
        allergens = line[1][:-1].split(', ')

        yield ingredients, allergens

ingr = set()
dic = {}

for ingredients, allergens in get_products():
    i = set(ingredients)

    for ing in ingredients:
        ingr.add(ing)

    for a in allergens:
        if a not in dic:
            dic[a] = i
        else:
            # Intersection
            dic[a] = i & dic[a]

print(dic)
print(ingr)

tot = 0
for ingredients, _ in get_products():
    for i in ingredients:
        for a in dic:
            if i in dic[a]:
                break
        else:
            tot += 1


print(tot)