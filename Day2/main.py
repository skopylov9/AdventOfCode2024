reports = open('input.txt').read().splitlines()
reports = [list(map(int, report.split(' '))) for report in reports]

def isSafe(levels):
    if levels[0] > levels[-1]:
        return isSafe(list(reversed(levels)))
    return all([levels[i] - levels[i - 1] in range(1, 4) for i in range(1, len(levels))])

def isSafeWithTolerance(levels):
    return any([isSafe(levels[:i] + levels[i + 1:]) for i in range(len(levels))])

print('Part 1:', sum([1 if isSafe(levels) else 0 for levels in reports]))
print('Part 2:', sum([1 if isSafeWithTolerance(levels) else 0 for levels in reports]))
