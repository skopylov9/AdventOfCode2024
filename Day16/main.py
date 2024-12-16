import heapq

def markStepsMap(raceMap, startPoint):
    stepsMap = [[[1000000 for _ in range(4)] for cell in line] for line in raceMap]
    stepsMap[startPoint[0]][startPoint[1]][1] = 0

    toProcessCells = []
    heapq.heappush(toProcessCells, (0, (startPoint, 1)))
    while toProcessCells:
        _, (point, orientation) = heapq.heappop(toProcessCells)
        di, dj = ((-1, 0), (0, 1), (1, 0), (0, -1))[orientation]
        if raceMap[point[0] + di][point[1] + dj] != '#' and stepsMap[point[0] + di][point[1] + dj][orientation] > stepsMap[point[0]][point[1]][orientation] + 1:
            stepsMap[point[0] + di][point[1] + dj][orientation] = stepsMap[point[0]][point[1]][orientation] + 1
            heapq.heappush(toProcessCells, (stepsMap[point[0] + di][point[1] + dj][orientation], ((point[0] + di, point[1] + dj), orientation)))
        if stepsMap[point[0]][point[1]][(orientation + 1) % 4] > stepsMap[point[0]][point[1]][orientation] + 1000:
            stepsMap[point[0]][point[1]][(orientation + 1) % 4] = stepsMap[point[0]][point[1]][orientation] + 1000
            heapq.heappush(toProcessCells, (stepsMap[point[0]][point[1]][(orientation + 1) % 4], ((point[0], point[1]), (orientation + 1) % 4)))
        if stepsMap[point[0]][point[1]][(orientation + 3) % 4] > stepsMap[point[0]][point[1]][orientation] + 1000:
            stepsMap[point[0]][point[1]][(orientation + 3) % 4] = stepsMap[point[0]][point[1]][orientation] + 1000
            heapq.heappush(toProcessCells, (stepsMap[point[0]][point[1]][(orientation + 3) % 4], ((point[0], point[1]), (orientation + 3) % 4)))
    
    return stepsMap

def getTilesUsedInBestPath(stepsMap, endPoint, minScore):
    tiles = set()
    toProcessCells = [(endPoint, orientation) for orientation, steps in enumerate(stepsMap[endPoint[0]][endPoint[1]]) if steps == minScore]
    while toProcessCells:
        point, orientation = toProcessCells.pop(0)
        tiles.add(point)
        di, dj = ((-1, 0), (0, 1), (1, 0), (0, -1))[(orientation + 2) % 4]
        if stepsMap[point[0] + di][point[1] + dj][orientation] == stepsMap[point[0]][point[1]][orientation] - 1:
            toProcessCells.append(((point[0] + di, point[1] + dj), orientation))
        if stepsMap[point[0]][point[1]][(orientation + 1) % 4] == stepsMap[point[0]][point[1]][orientation] - 1000:
            toProcessCells.append(((point[0], point[1]), (orientation + 1) % 4))
        if stepsMap[point[0]][point[1]][(orientation + 3) % 4] == stepsMap[point[0]][point[1]][orientation] - 1000:
            toProcessCells.append(((point[0], point[1]), (orientation + 3) % 4))
    return tiles

raceMap = open('input.txt').read().splitlines()

startPoint = (len(raceMap) - 2, 1)
endPoint = (1, len(raceMap[0]) - 2)

stepsMap = markStepsMap(raceMap, startPoint)

minScore = min(stepsMap[endPoint[0]][endPoint[1]])

print('Part 1:', minScore) # 89460
print('Part 2:', len(getTilesUsedInBestPath(stepsMap, endPoint, minScore))) # 504
