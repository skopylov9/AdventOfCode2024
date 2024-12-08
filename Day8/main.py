import math

map = [list(line) for line in open('input.txt').read().splitlines()]

antennas = {}
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != '.':
            antennas[map[i][j]] = antennas.get(map[i][j], []) + [(i, j)]

antinodes = set()
for freq, locations in antennas.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            l1, l2 = locations[i], locations[j]
            dl = (l2[0] - l1[0], l2[1] - l1[1])
            if (l1[0] - dl[0]) in range(len(map)) and (l1[1] - dl[1]) in range(len(map[l1[0] - dl[0]])):
                antinodes.add((l1[0] - dl[0], l1[1] - dl[1]))
            if (l2[0] + dl[0]) in range(len(map)) and (l2[1] + dl[1]) in range(len(map[l2[0] + dl[0]])):
                antinodes.add((l2[0] + dl[0], l2[1] + dl[1]))

print('Part 1:', len(antinodes))    # 256

antinodes = set()
for freq, locations in antennas.items():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            l1, l2 = locations[i], locations[j]
            dl = (l2[0] - l1[0], l2[1] - l1[1])
            while l1[0] in range(len(map)) and l1[1] in range(len(map[l1[0]])):
                antinodes.add(l1)
                l1 = (l1[0] - dl[0], l1[1] - dl[1])
            l1, l2 = locations[i], locations[j]
            while l2[0] in range(len(map)) and l2[1] in range(len(map[l2[0]])):
                antinodes.add(l2)
                l2 = (l2[0] + dl[0], l2[1] + dl[1])

print('Part 2:', len(antinodes))    # 1005
