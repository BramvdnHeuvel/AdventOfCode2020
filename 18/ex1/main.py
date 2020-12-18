from typing import Callable, Tuple

OPERATOR = {
    "+" :   (lambda a, b : a + b),
    "*" :   (lambda a, b : a * b)
}

def parse_into_brackets(line : str, solver : Callable) -> Tuple[int, int]:
    """
        Parse a string. Notice brackets and solve them before continuing.
        The function returns the answer, the string length
    """
    i = 0
    open_brackets = [i for i in range(len(line)) if line[i] == '(']
    closed_brackets = [i for i in range(len(line)) if line[i] == ')']

    while open_brackets != []:
        # Calculate the first deepest bracket set
        i, j = (max([b for b in open_brackets if b < closed_brackets[0]]), closed_brackets[0])

        solution = solver(line[i+1:j])

        line = line[:i] + str(solution) + line[j+1:]
    
        open_brackets = [i for i in range(len(line)) if line[i] == '(']
        closed_brackets = [i for i in range(len(line)) if line[i] == ')']
        
    return solver(line)


def solve_puzzle(line : str):
    """
        Solve a line puzzle.
    """  
    print(line)
    chars = line.split(' ')
    answer = int(chars[0])
    i = 1

    while i < len(chars):
        operator = chars[i]
        value    = chars[i+1]

        answer = OPERATOR[operator](answer, int(value))
        i += 2

    return answer

print(sum([parse_into_brackets(line.strip(), solve_puzzle) for line in open('input.txt', 'r')]))
