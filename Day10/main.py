tgMap = open('input.txt').read().splitlines()
tgMap = [list(map(int, line)) for line in tgMap]

trailScore = [[set([(i, j)] if tgMap[i][j] == 9 else []) for j in range(len(tgMap[i]))] for i in range(len(tgMap))]
trailRating = [[1 if tgMap[i][j] == 9 else 0 for j in range(len(tgMap[i]))] for i in range(len(tgMap))]

for height in range(8, -1, -1):
    for i in range(len(tgMap)):
        for j in range(len(tgMap[i])):
            if height != tgMap[i][j]:
                continue
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (i + di) not in range(len(tgMap)) or (j + dj) not in range(len(tgMap[i])):
                    continue
                if tgMap[i + di][j + dj] == (tgMap[i][j] + 1):
                    trailScore[i][j].update(trailScore[i + di][j + dj])
                    trailRating[i][j] += trailRating[i + di][j + dj]

print('Part 1:', sum(len(trailScore[i][j]) for i in range(len(tgMap)) for j in range(len(tgMap[i])) if tgMap[i][j] == 0)) # 778
print('Part 2:', sum(trailRating[i][j] for i in range(len(tgMap)) for j in range(len(tgMap[i])) if tgMap[i][j] == 0))     # 1925
