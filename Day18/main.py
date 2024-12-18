import bisect

blockedBytes = open('input.txt').read().splitlines()
blockedBytes = [tuple(map(int, pos.split(','))) for pos in blockedBytes]

def findPath(startPos, endPos, blockedBytes):
    bestPath = {startPos : 0}
    posQueue = [startPos]
    while posQueue:
        pos = posQueue.pop(0)
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if pos[0] + dx not in range(endPos[0] + 1) or pos[1] + dy not in range(endPos[1] + 1):
                continue
            if (pos[0] + dx, pos[1] + dy) in blockedBytes:
                continue
            if (pos[0] + dx, pos[1] + dy) in bestPath:
                continue

            bestPath[(pos[0] + dx, pos[1] + dy)] = bestPath[pos] + 1
            posQueue.append((pos[0] + dx, pos[1] + dy))

            if (pos[0] + dx, pos[1] + dy) == endPos:
                return bestPath[endPos]
    
    return None

def findFirstByteNoPath(startPos, endPos, blockedBytes, byteIndex):
    lastIndex = bisect.bisect_right(
        [i for i in range(byteIndex, len(blockedBytes))],
        0,
        key=lambda i: 0 if findPath(startPos, endPos, set(blockedBytes[0:i])) else 1)
    return ','.join(map(str, blockedBytes[lastIndex + byteIndex - 1]))


startPos = (0, 0)
# endPos = (6, 6)
endPos = (70, 70)
# byteIndex = 12
byteIndex = 1024

print('Part 1:', findPath(startPos, endPos, set(blockedBytes[0:byteIndex]))) # 226
print('Part 2:', findFirstByteNoPath(startPos, endPos, blockedBytes, byteIndex)) # 60,46
