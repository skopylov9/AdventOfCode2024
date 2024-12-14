import time

robots = [line.split(' ') for line in open('input.txt').read().splitlines()]
robots = [(tuple(map(int, p[2:].split(','))), tuple(map(int, v[2:].split(',')))) for p, v in robots]

w, h = map(max, zip(*[p for p, _ in robots]))
w, h = w + 1, h + 1

def printPositions(positions):
    rMap = [['.' for _ in range(w)] for _ in range(h)]
    for p in positions:
        rMap[p[0]][p[1]] = '*'

    for line in rMap:
        print(''.join(line))

def moveRobots(secs):
    return [((p[1] + (h + v[1]) * secs) % h, (p[0] + (w + v[0]) * secs) % w) for p, v in robots]


s1 = 100
s2 = 6475   # Don't ask me why

positions = moveRobots(s1)
q1 = sum(1 for p in positions if p[0] < h // 2 and p[1] < w // 2)
q2 = sum(1 for p in positions if p[0] < h // 2 and p[1] > w // 2)
q3 = sum(1 for p in positions if p[0] > h // 2 and p[1] < w // 2)
q4 = sum(1 for p in positions if p[0] > h // 2 and p[1] > w // 2)

printPositions(moveRobots(s2))

print('Part 1:', q1 * q2 * q3 * q4) # 27105
print('Part 2:', s2)                # 6475
