import math

equations = [eq.split(': ') for eq in open('input.txt').read().splitlines()]
equations = [(int(eq[0]), list(map(int, eq[1].split(' ')))) for eq in equations]

def isValid(result, arguments, withConcatenation = False):
    *arguments, arg = arguments
    power = 10 ** (int(math.log10(arg)) + 1)
    if not arguments:
        return arg == result
    elif False if arg > result else isValid(result - arg, arguments, withConcatenation):
        return True
    elif False if result % arg else isValid(result // arg, arguments, withConcatenation):
        return True
    elif False if result % power != arg else isValid(result // power, arguments, withConcatenation):
        return withConcatenation
    else:
        return False

print('Part 1:', sum(eq[0] for eq in equations if isValid(eq[0], eq[1])))       # 465126289353
print('Part 2:', sum(eq[0] for eq in equations if isValid(eq[0], eq[1], True))) # 70597497486371
