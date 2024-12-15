warehousMap, moves = open('input.txt').read().split('\n\n')

scalePolicy = {'#' : '##', 'O' : '[]', '.' : '..', '@' : '@.'}
warehousMap = [list(line) for line in warehousMap.splitlines()]
scaledWarehousMap = [list(''.join([scalePolicy[cell] for cell in line])) for line in warehousMap]
moves = ''.join(moves.splitlines())

orientations = {'^' : (-1, 0), '>' : (0, 1), 'v' : (1, 0), '<' : (0, -1)}

def makeMovePart1(warehous, robotPos, move):
    di, dj = orientations[move]

    toCheckPosition = (robotPos[0] + di, robotPos[1] + dj)
    while warehous[toCheckPosition[0]][toCheckPosition[1]] == 'O':
        toCheckPosition = (toCheckPosition[0] + di, toCheckPosition[1] + dj)

    if warehous[toCheckPosition[0]][toCheckPosition[1]] == '.':
        warehous[toCheckPosition[0]][toCheckPosition[1]] = warehous[toCheckPosition[0] - di][toCheckPosition[1] - dj]
        warehous[robotPos[0] + di][robotPos[1] + dj] = warehous[robotPos[0]][robotPos[1]]
        warehous[robotPos[0]][robotPos[1]] = '.'
        return (robotPos[0] + di, robotPos[1] + dj)
    
    return robotPos

def makeMovePart2(warehous, robotPos, move):
    di, dj = orientations[move]

    toCheckPositions = [(robotPos[0] + di, robotPos[1] + dj)]
    toMove = toCheckPositions[:]
    while True:
        if any(warehous[i][j] == '#' for i, j in toCheckPositions):
            return robotPos
        elif all(warehous[i][j] == '.' for i, j in toCheckPositions):
            for pos in reversed(toMove):
                warehous[pos[0]][pos[1]] = warehous[pos[0] - di][pos[1] - dj]
                warehous[pos[0] - di][pos[1] - dj] = '.'
            return (robotPos[0] + di, robotPos[1] + dj)
        elif move in ('<', '>'):
            toCheckPositions = [(toCheckPositions[0][0] + di, toCheckPositions[0][1] + dj)]
            toMove.extend(toCheckPositions)
        else:
            toCheckPositions = [[(i + di, j), (i + di, j + (1 if warehous[i][j] == '[' else -1))] for i, j in toCheckPositions if warehous[i][j] in ('[', ']')]
            toCheckPositions = list(set(pos for positions in toCheckPositions for pos in positions))
            toMove.extend(toCheckPositions)

for i, line in enumerate(warehousMap):
    if '@' in line:
        robotPos = (i, line.index('@'))
scaledRobotPos = (robotPos[0], robotPos[1] * 2)

for move in moves:
    robotPos = makeMovePart1(warehousMap, robotPos, move)
    scaledRobotPos = makeMovePart2(scaledWarehousMap, scaledRobotPos, move)

print('Part 1:', sum(100 * i + j for i, line in enumerate(warehousMap) for j, cell in enumerate(line) if cell == 'O')) # 1475249
print('Part 2:', sum(100 * i + j for i, line in enumerate(scaledWarehousMap) for j, cell in enumerate(line) if cell == '[')) # 1509724
