guardMap = [list(line) for line in open('input.txt').read().splitlines()]

for i in range(len(guardMap)):
    if '^' in guardMap[i]:
        startPos = (i, guardMap[i].index('^'), 0)

def findAWayOut(pos):
    orients = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = set()
    while pos not in visited:
        visited.add(pos)
        ni, nj = pos[0] + orients[pos[2]][0], pos[1] + orients[pos[2]][1]
        if ni not in range(len(guardMap)) or nj not in range(len(guardMap[ni])):
            return visited
        elif guardMap[ni][nj] == '#':
            pos = (pos[0], pos[1], (pos[2] + 1) % len(orients))
        else:
            pos = (ni, nj, pos[2])
    return None

def isTheWayOut(obstr):
    guardMap[obstr[0]][obstr[1]] = '#'
    path = findAWayOut(startPos)
    guardMap[obstr[0]][obstr[1]] = '.'
    return bool(path)

uniqCellsInPath = set((pos[0], pos[1]) for pos in findAWayOut(startPos))
uniqCellsInPath.remove((startPos[0], startPos[1]))
    
print('Part 1:', len(uniqCellsInPath) + 1)                                      # 5329
print('Part 2:', sum(1 for i, j in uniqCellsInPath if not isTheWayOut((i, j)))) # 2162
