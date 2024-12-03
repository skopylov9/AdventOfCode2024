import re

inputLine = open('input.txt').read()

filteredInput = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', inputLine)

doFlag = True
doStr = 'do()'
doNotStr = 'don\'t()'
mulListPart1 = []
mulListPart2 = []
for value in filteredInput:
    if value == doStr or value == doNotStr:
        doFlag = value == doStr
        continue

    mulListPart1.append(value)
    if doFlag:
        mulListPart2.append(value)

print('Part 1:', sum(x * y for x, y in [tuple(map(int, mul[4:-1].split(','))) for mul in mulListPart1]))    # 187833789
print('Part 2:', sum(x * y for x, y in [tuple(map(int, mul[4:-1].split(','))) for mul in mulListPart2]))    # 94455185
