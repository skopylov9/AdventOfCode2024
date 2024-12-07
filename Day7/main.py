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


import unittest
class TestEquations(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(isValid(190, [10, 19]), True)
        self.assertEqual(isValid(3267, [81, 40, 27]), True)
        self.assertEqual(isValid(83, [17, 5]), False)
        self.assertEqual(isValid(156, [15, 6]), False)
        self.assertEqual(isValid(7290, [6, 8, 6, 15]), False)
        self.assertEqual(isValid(161011, [16, 10, 13]), False)
        self.assertEqual(isValid(192, [17, 8, 14]), False)
        self.assertEqual(isValid(21037, [9, 7, 18, 13]), False)
        self.assertEqual(isValid(292, [11, 6, 16, 20]), True)

    def test_part2(self):
        self.assertEqual(isValid(190, [10, 19], True), True)
        self.assertEqual(isValid(3267, [81, 40, 27], True), True)
        self.assertEqual(isValid(83, [17, 5], True), False)
        self.assertEqual(isValid(156, [15, 6], True), True)
        self.assertEqual(isValid(7290, [6, 8, 6, 15], True), True)
        self.assertEqual(isValid(161011, [16, 10, 13], True), False)
        self.assertEqual(isValid(192, [17, 8, 14], True), True)
        self.assertEqual(isValid(21037, [9, 7, 18, 13], True), False)
        self.assertEqual(isValid(292, [11, 6, 16, 20], True), True)
    
    def test_result(self):
        self.assertEqual(sum(eq[0] for eq in equations if isValid(eq[0], eq[1])), 465126289353)
        self.assertEqual(sum(eq[0] for eq in equations if isValid(eq[0], eq[1], True)), 70597497486371)

unittest.main()