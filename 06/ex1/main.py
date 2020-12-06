answers = [line if line == '\n' else line.strip() for line in open('input.txt')]
answers = ''.join(answers).split('\n')

tot = 0

for sentence in answers:
    tot += len(set([c for c in sentence]))

print(tot)