
lines = open('input.txt').read().splitlines()
list1, list2 = zip(*[list(map(int, line.split('   '))) for line in lines])

print('Part 1:', sum([abs(lId1 - lId2) for lId1, lId2 in zip(sorted(list1), sorted(list2))]))   # 2000468
print('Part 2:', sum([lId * list2.count(lId) for lId in list1]))                                # 18567089
