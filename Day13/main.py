import re

clawMachines = open('input.txt').read().split('\n\n')
clawMachines = [clawMachine.splitlines() for clawMachine in clawMachines]
clawMachines = [tuple([tuple(map(int, re.findall('\d+', line))) for line in lines]) for lines in clawMachines]

def calcTokensCount(clawMachine, prizeOffset = 0):
    buttonA, buttonB, prize = clawMachine

    prize = (prize[0] + prizeOffset, prize[1] + prizeOffset)

    countB = int((prize[1] - buttonA[1] * prize[0] / buttonA[0]) / (buttonB[1] - buttonA[1] * buttonB[0] / buttonA[0]) + 0.5)
    countA = int((prize[0] - countB * buttonB[0]) / buttonA[0] + 0.5)

    if countA * buttonA[0] + countB * buttonB[0] == prize[0] and countA * buttonA[1] + countB * buttonB[1] == prize[1]:
        return countA * 3 + countB
    
    return 0

print('Part 1:', sum(calcTokensCount(clawMachine) for clawMachine in clawMachines))                 # 27105
print('Part 2:', sum(calcTokensCount(clawMachine, 10000000000000) for clawMachine in clawMachines)) # 101726882250942
