
numbers = [int(num.strip()) for num in open('input.txt', 'r')]

product = lambda a, b : a*b if (a+b == 2020) else 0

tot = 0

for a in numbers:
    for b in numbers:
        tot += product(a, b)
    else:
        if tot > 0:
            break

print(tot)