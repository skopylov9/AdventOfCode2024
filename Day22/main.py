nums = list(map(int, open('input.txt').read().splitlines()))

def getNextNum(num):
    num = (num ^ (num << 6)) & ((1 << 24) - 1)
    num = (num ^ (num >> 5)) & ((1 << 24) - 1)
    num = (num ^ (num << 11)) & ((1 << 24) - 1)
    return num

times = 2000
globalPatterns = {}

for i in range(len(nums)):
    prevBanans = None
    pattern = tuple()
    patterns = dict()
    for j in range(times):
        nums[i] = getNextNum(nums[i])
        banans = nums[i] % 10
        if prevBanans is not None:
            pattern = pattern[-3:] + ((banans - prevBanans),)
        prevBanans = banans

        if j > 4 and pattern not in patterns:
            patterns[pattern] = banans
    
    for pattern, banans in patterns.items():
        globalPatterns[pattern] = globalPatterns.get(pattern, 0) + banans

print('Part 1:', sum(nums))                     # 13185239446
print('Part 2:', max(globalPatterns.values()))  # 1501
