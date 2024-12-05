from functools import cmp_to_key

rules, updates = open('input.txt').read().split('\n\n')
rules = [tuple(map(int, rule.split('|'))) for rule in rules.splitlines()]
updates = [list(map(int, update.split(','))) for update in updates.splitlines()]

rulesMap = {}
for rule in rules:
    rulesMap[rule[0]] = rulesMap.get(rule[0], []) + [rule[1]]

sortedUpdates = [sorted(update, key=cmp_to_key(lambda x, y: -1 if y in rulesMap.get(x, []) else 0)) for update in updates]

print('Part 1:', sum(sortedUpdate[len(sortedUpdate) // 2] for update, sortedUpdate in zip(updates, sortedUpdates) if update == sortedUpdate))  # 6612
print('Part 2:', sum(sortedUpdate[len(sortedUpdate) // 2] for update, sortedUpdate in zip(updates, sortedUpdates) if update != sortedUpdate))  # 4944
