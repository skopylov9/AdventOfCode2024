import math
from functools import lru_cache

stones = list(map(int, open('input.txt').read().split(' ')))

@lru_cache(maxsize=2**24)
def blinkStone(stone, times):
    if times == 0:
        return 1
    if stone == 0:
        return blinkStone(1, times - 1)

    digits = int(math.log10(stone)) + 1
    if digits % 2:
        return blinkStone(stone * 2024, times - 1)

    return blinkStone(stone // (10 ** (digits // 2)), times - 1) + blinkStone(stone % (10 ** (digits // 2)), times - 1)

print('Part 1:', sum(blinkStone(stone, 25) for stone in stones))    # 218956
print('Part 2:', sum(blinkStone(stone, 75) for stone in stones))    # 259593838049805
