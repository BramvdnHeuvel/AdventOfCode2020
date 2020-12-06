from functools import reduce

answers = [line if line == '\n' else line.strip() for line in open('input.txt')]
answers = '\t'.join(answers).split('\n')
answers = [sentence.strip().split('\t') for sentence in answers]

print(
    sum([len(reduce((lambda a, b: set(a) & set(b)), sentence)) for sentence in answers])
)