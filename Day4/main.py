matrix = [list(line) for line in open('input.txt').read().splitlines()]

def countPart1(i, j):
    def getFromMatrix(i, j):
        return matrix[i][j] if i in range(len(matrix)) and j in range(len(matrix[i])) else ''

    ws = zip(*[(getFromMatrix(i, j + d), getFromMatrix(i + d, j), getFromMatrix(i + d, j + d), getFromMatrix(i - d, j + d)) for d in range(4)])
    ws = list(map(''.join, ws))
    return sum(1 for w in ws if w in ('XMAS', 'SAMX'))

def countPart2(i, j):
    if i < 1 or i > len(matrix) - 2 or j < 1 or j > len(matrix[i]) - 2:
        return 0
    matrixSlice = ''.join(matrix[i + di][j + dj] for di, dj in ((-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)))
    return 1 if matrixSlice in ('MSAMS', 'MMASS', 'SMASM', 'SSAMM') else 0

print('Part 1:', sum(countPart1(i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))))  # 2642
print('Part 2:', sum(countPart2(i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))))  # 1974
