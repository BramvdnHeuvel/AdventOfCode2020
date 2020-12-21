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

still_improvement_needed = True
occupied_ingredients = set()

while still_improvement_needed:
    still_improvement_needed = False

    for a in dic:
        if len(dic[a]) == 1:
            occupied_ingredients = occupied_ingredients.union(dic[a])
            continue

        still_improvement_needed = True

        for o in occupied_ingredients:
            if o in dic[a]:
                dic[a].remove(o)

answer = ""

keys = [a for a in dic]
keys.sort()

for a in keys:
    for o in dic[a]:
        answer += o + ","

print(answer[:-1])
