schematics = open('input.txt').read().split('\n\n')
schematics = [schematic.splitlines() for schematic in schematics]
locks = [[column.count('#') for column in zip(*schematic)] for schematic in schematics if '.' not in schematic[0]]
keys = [[column.count('#') for column in zip(*schematic)] for schematic in schematics if '.' not in schematic[-1]]

print('Part 2:', sum(1 for lock in locks for key in keys if max(sum(pair) for pair in zip(lock, key)) < 8)) # 3242
