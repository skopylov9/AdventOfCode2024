racetrack = open('input.txt').read().splitlines()
racetrack = [list(line) for line in racetrack]

def markRaceTrack(racetrack):
    for i, line in enumerate(racetrack):
        if 'S' in line:
            startPos = (i, line.index('S'))
        if 'E' in line:
            endPos = (i, line.index('E'))

    racetrack[startPos[0]][startPos[1]] = 0
    racetrack[endPos[0]][endPos[1]] = '.'
    while startPos != endPos:
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if racetrack[startPos[0] + di][startPos[1] + dj] == '.':
                racetrack[startPos[0] + di][startPos[1] + dj] = racetrack[startPos[0]][startPos[1]] + 1
                startPos = (startPos[0] + di, startPos[1] + dj)
                break

def calcCheatCount(racetrack, cheatLength, chectThreshold = 100):
    result = 0
    for i in range(len(racetrack)):
        for j in range(len(racetrack[i])):
            if racetrack[i][j] == '#':
                continue

            for di in range(-cheatLength, cheatLength + 1):
                for dj in range(abs(di) - cheatLength, cheatLength - abs(di) + 1):
                    if i + di in range(len(racetrack)) and j + dj in range(len(racetrack[i + di])):
                        if racetrack[i + di][j + dj] != '#':
                            cheat = racetrack[i + di][j + dj] - racetrack[i][j] - abs(di) - abs(dj)
                            if cheat >= chectThreshold:
                                result += 1
    return result

markRaceTrack(racetrack)

print('Part 1:', calcCheatCount(racetrack, 2))     # 1311
print('Part 2:', calcCheatCount(racetrack, 20))    # 961364
