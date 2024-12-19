patterns, designs = open('input.txt').read().split('\n\n')
patterns = set(patterns.split(', '))
designs = designs.splitlines()

def calcPossibleWays(design):
    posMap = [0 for _ in range(len(design) + 1)]
    posMap[0] = 1

    for end in range(len(design) + 1):
        for border in range(end):
            posMap[end] += posMap[border] if design[border:end] in patterns else 0
    
    return posMap[len(design)]

print('Part 1:', sum(1 for design in designs if calcPossibleWays(design)))  # 238
print('Part 2:', sum(calcPossibleWays(design) for design in designs))       # 635018909726691
