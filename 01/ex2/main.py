
numbers = [int(num.strip()) for num in open('input.txt', 'r')]

product = lambda a, b, c : a*b*c if (a+b+c == 2020) else 0

for a in numbers:
    for b in numbers:
        for c in numbers:
            if (tot := product(a, b, c)) > 0:
                print(tot)
