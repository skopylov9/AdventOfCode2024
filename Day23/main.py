connections = [tuple(connection.split('-')) for connection in open('input.txt').read().splitlines()]
uniqComputers = set([computer for connection in connections for computer in connection])

byComputerConnections = { uniqComputer : set() for uniqComputer in uniqComputers}
for computer1, computer2 in connections:
    byComputerConnections[computer1].add(computer2)
    byComputerConnections[computer2].add(computer1)

def checkGroup(comp1, comp2, comp3):
    return 't' in (comp1[0], comp2[0], comp3[0]) and comp2 in byComputerConnections[comp3]

threeGroupCount = 0
for computer1 in uniqComputers:
    conns = list(byComputerConnections[computer1])
    for i in range(len(conns)):
        for j in range(i + 1, len(conns)):
            if checkGroup(computer1, conns[i], conns[j]):
                threeGroupCount += 1

maxGroup = set()
def getMaxConnectedGroup(computers):
    connectionPower = { computer : len(computers.intersection(byComputerConnections[computer])) for computer in computers }
    if all(power == len(computers) for power in connectionPower.values()):
        return computers
    return getMaxConnectedGroup(computers - set([min(connectionPower, key = connectionPower.get)]))

for computer in byComputerConnections.keys():
    byComputerConnections[computer].add(computer)

for computer, connectedComputers in byComputerConnections.items():
    group = getMaxConnectedGroup(connectedComputers)
    if len(group) > len(maxGroup):
        maxGroup = group


print('Part 1:', threeGroupCount // 3)          # 1284
print('Part 2:', ','.join(sorted(maxGroup)))    # bv,cm,dk,em,gs,jv,ml,oy,qj,ri,uo,xk,yw
