
map = [list(line) for line in open('input.txt').read().splitlines()]

def markRegion(markedMap, i, j, regionId):
    markedMap[i][j] = (regionId, markedMap[i][j][1])
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if (i + di) in range(len(markedMap)) and (j + dj) in range(len(markedMap[i + di])):
            if markedMap[i][j][1] == markedMap[i + di][j + dj][1] and markedMap[i + di][j + dj][0] == None:
                markRegion(markedMap, i + di, j + dj, regionId)

def createMarkedMap(map):
    markedMap = [[(None, cell) for cell in line] for line in map]
    uniqRegion = 0
    for i in range(len(markedMap)):
        for j in range(len(markedMap[i])):
            if markedMap[i][j][0] == None:
                markRegion(markedMap, i, j, uniqRegion)
                uniqRegion += 1    
    return markedMap

def getRegions(markedMap):
    regions = { markedMap[i][j] : [0, []] for i in range(len(markedMap)) for j in range(len(markedMap[i])) }
    for i in range(len(markedMap)):
        for j in range(len(markedMap[i])):
            regions[markedMap[i][j]][0] += 1
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (i + di) not in range(len(markedMap)) or (j + dj) not in range(len(markedMap[i + di])) or markedMap[i][j] != markedMap[i + di][j + dj]:
                    regions[markedMap[i][j]][1].append((i, j, di, dj))
    return regions

def calcLines(perimeter):
    hLines = sorted([(i, di, j) for i, j, di, _ in perimeter if di])
    vLines = sorted([(j, dj, i) for i, j, _, dj in perimeter if dj])
    linesCount = len(hLines) + len(vLines)
    for i in range(1, len(hLines)):
        if (hLines[i][0], hLines[i][1], hLines[i][2] - 1) == hLines[i - 1]:
            linesCount -= 1
    for i in range(1, len(vLines)):
        if (vLines[i][0], vLines[i][1], vLines[i][2] - 1) == vLines[i - 1]:
            linesCount -= 1
    return linesCount

markedMap = createMarkedMap(map)
regions = getRegions(markedMap)

print('Part 1:', sum(area * len(perimeter) for area, perimeter in regions.values()))        # 1533024
print('Part 2:', sum(area * calcLines(perimeter) for area, perimeter in regions.values()))  # 910066
# for region, (area, perimeter) in regions.items():
    # print(region, area, len(perimeter), calcLines(perimeter))
