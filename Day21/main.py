def calcPossibleMoves(keypad, fromI, fromJ, toI, toJ):
    moves = []
    if keypad[fromI][fromJ] is None or keypad[toI][toJ] is None:
        moves = []
    elif (fromI, fromJ) == (toI, toJ):
        moves = ['A']
    elif fromI == toI:
        moves = ['<' * max(0, fromJ - toJ) + '>' * max(0, toJ - fromJ) + 'A']
    elif fromJ == toJ:
        moves = ['^' * max(0, fromI - toI) + 'v' * max(0, toI - fromI) + 'A']
    else:
        if fromI < toI:
            moves += ['v' + move for move in calcPossibleMoves(keypad, fromI + 1, fromJ, toI, toJ)]
        else:
            moves += ['^' + move for move in calcPossibleMoves(keypad, fromI - 1, fromJ, toI, toJ)]
        
        if fromJ < toJ:
            moves += ['>' + move for move in calcPossibleMoves(keypad, fromI, fromJ + 1, toI, toJ)]
        else:
            moves += ['<' + move for move in calcPossibleMoves(keypad, fromI, fromJ - 1, toI, toJ)]
    return moves

def initKeypadMoves(keypad):
    keypadMoves = {}
    for fromI in range(len(keypad)):
        for fromJ in range(len(keypad[fromI])):
            for toI in range(len(keypad)):
                for toJ in range(len(keypad[toI])):
                    if keypad[fromI][fromJ] not in keypadMoves:
                        keypadMoves[keypad[fromI][fromJ]] = {}
                    keypadMoves[keypad[fromI][fromJ]][keypad[toI][toJ]] = calcPossibleMoves(keypad, fromI, fromJ, toI, toJ)
    return keypadMoves

def initHandlyCheckedRobotPadMoves():
    movesRobotPad = {move : {} for move in '^A<v>'}
    movesRobotPad['^']['^'] = 'A'
    movesRobotPad['^']['A'] = '>A'
    movesRobotPad['^']['<'] = 'v<A'
    movesRobotPad['^']['v'] = 'vA'
    movesRobotPad['^']['>'] = 'v>A'
    # movesRobotPad['^']['>'] = '>vA'
    movesRobotPad['A']['^'] = '<A'
    movesRobotPad['A']['A'] = 'A'
    movesRobotPad['A']['<'] = 'v<<A'
    # movesRobotPad['A']['<'] = '<v<A'
    movesRobotPad['A']['v'] = '<vA'
    # movesRobotPad['A']['v'] = 'v<A'
    movesRobotPad['A']['>'] = 'vA'
    movesRobotPad['<']['^'] = '>^A'
    movesRobotPad['<']['A'] = '>>^A'
    # movesRobotPad['<']['A'] = '>^>A'
    movesRobotPad['<']['<'] = 'A'
    movesRobotPad['<']['v'] = '>A'
    movesRobotPad['<']['>'] = '>>A'
    movesRobotPad['v']['^'] = '^A'
    movesRobotPad['v']['A'] = '^>A'
    # movesRobotPad['v']['A'] = '>^A'
    movesRobotPad['v']['<'] = '<A'
    movesRobotPad['v']['v'] = 'A'
    movesRobotPad['v']['>'] = '>A'
    movesRobotPad['>']['^'] = '<^A'
    # movesRobotPad['>']['^'] = '^<A'
    movesRobotPad['>']['A'] = '^A'
    movesRobotPad['>']['<'] = '<<A'
    movesRobotPad['>']['v'] = '<A'
    movesRobotPad['>']['>'] = 'A'
    return movesRobotPad

numPad = [['7', '8', '9'],
          ['4', '5', '6'],
          ['1', '2', '3'],
          [None, '0', 'A']]

robotPad = [[None, '^', 'A'],
            ['<', 'v', '>']]

movesNumPad = initKeypadMoves(numPad)
# movesRobotPad = initKeypadMoves(robotPad)
movesRobotPad = initHandlyCheckedRobotPadMoves()

def mapNumPadToRobot(num):
    mstrs = ['']
    start = 'A'
    for v in num:
        mstrs = [mstr + moves for mstr in mstrs for moves in movesNumPad[start][v]]
        start = v
    return mstrs

def mapRobotPadToRobot(moves):
    start = 'A'
    newMoves = []
    for move in moves:
        newMoves.append(movesRobotPad[start][move])
        start = move
    return newMoves


uniqRobotMoves = list(set([moves for movesRobotPadValues in movesRobotPad.values() for moves in movesRobotPadValues.values()]))
uniqRobotMovesCountByDeep = [{ uniqMove : len(uniqMove) for uniqMove in uniqRobotMoves }]
for deep in range(1, 25):
    uniqRobotMovesLength = {}
    for uniqMove in uniqRobotMoves:
        uniqRobotMovesLength[uniqMove] = sum(uniqRobotMovesCountByDeep[deep - 1][moves] for moves in mapRobotPadToRobot(uniqMove))

    uniqRobotMovesCountByDeep.append(uniqRobotMovesLength)

def calcMovesCount(uniqRobotMovesCount, num):
    minLen = None
    for moves in mapNumPadToRobot(num):
        start = 'A'
        summmm = 0
        for move in moves:
            summmm += uniqRobotMovesCount[movesRobotPad[start][move]]
            start = move
        
        if minLen == None or summmm < minLen:
            minLen = summmm

    return int(num[0:3]) * minLen

nums = open('input.txt').read().splitlines()

print('Part 1:', sum(calcMovesCount(uniqRobotMovesCountByDeep[1], num) for num in nums))    # 171596
print('Part 2:', sum(calcMovesCount(uniqRobotMovesCountByDeep[24], num) for num in nums))   # 209268004868246
