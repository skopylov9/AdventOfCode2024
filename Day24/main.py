wires, gates = open('input.txt').read().split('\n\n')
wires = { wire[:3] : int(wire[5:]) for wire in wires.splitlines() }
gates = [(gate[0:3], gate[4:-11], gate[-10:-7], gate[-3:]) for gate in gates.splitlines()]
gates = [(arg1, op, arg2, out) if arg1 < arg2 else (arg2, op, arg1, out) for arg1, op, arg2, out in gates]

calcQueue = list(wires.keys())
while calcQueue:
    wire = calcQueue.pop(0)
    for arg1, op, arg2, out in gates:
        if out in wires:
            continue
        if (wire == arg1 and arg2 in wires) or (wire == arg2 and arg1 in wires):
            opMap = { 'AND' : lambda a, b: a & b, 'OR' : lambda a, b: a | b, 'XOR' : lambda a, b: a ^ b }
            wires[out] = opMap[op](wires[arg1], wires[arg2])
            calcQueue.append(out)

zwires = sorted([wire for wire in wires.keys() if wire[0] == 'z'])
zwires = [(i, wires[wire]) for i, wire in enumerate(zwires)]

zValue = 0
for i, v in enumerate(zwires):
    zValue += v[1] * 2 ** i

def containsGate(etArg1 = None, etOp = None, etArg2 = None, etOut = None):
    for arg1, op, arg2, out in gates:
        result = True
        if etArg1 and etArg1 not in (arg1, arg2):
            result = False
        if etArg2 and (etArg1, etArg2) != (arg1, arg2) and (etArg2, etArg1) != (arg1, arg2):
            result = False
        if etOp and etOp != op:
            result = False
        if etOut and etOut != out:
            result = False
        if result:
            return True
    return False

def getGate(etArg1 = None, etOp = None, etArg2 = None, etOut = None):
    for arg1, op, arg2, out in gates:
        result = True
        if etArg1 and etArg1 not in (arg1, arg2):
            result = False
        if etArg2 and (etArg1, etArg2) != (arg1, arg2) and (etArg2, etArg1) != (arg1, arg2):
            result = False
        if etOp and etOp != op:
            result = False
        if etOut and etOut != out:
            result = False
        if result:
            return (arg1, op, arg2, out)

def updateGate(etArg1 = None, etOp = None, etArg2 = None, etOut = None, nOut = None):
    for i, (arg1, op, arg2, out) in enumerate(gates):
        result = True
        if etArg1 and etArg1 not in (arg1, arg2):
            result = False
        if etArg2 and (etArg1, etArg2) != (arg1, arg2) and (etArg2, etArg1) != (arg1, arg2):
            result = False
        if etOp and etOp != op:
            result = False
        if etOut and etOut != out:
            result = False
        if result and nOut:
            gates[i] = (arg1, op, arg2, nOut)

def isXYPattern(arg1, op, arg2, out):
    return arg1[0] == 'x' and arg2[0] == 'y'

def isValidXYPattern(arg1, op, arg2, out):
    return isXYZeroPattern(arg1, op, arg2, out) or isXYAndPattern(arg1, op, arg2, out) or isXYXorPattern(arg1, op, arg2, out)

def isZPattern(arg1, op, arg2, out):
    return out[0] == 'z'

def isValidZPattern(arg1, op, arg2, out):
    return isZPattern(arg1, op, arg2, out) and (op == 'XOR' or out == 'z45')

def isXorPatter(arg1, op, arg2, out):
    return op == 'XOR'

def isValidXorPattern(arg1, op, arg2, out):
    return isXorPatter(arg1, op, arg2, out) and (isXYPattern(arg1, op, arg2, out) or isZPattern(arg1, op, arg2, out))

def isOrPatter(arg1, op, arg2, out):
    return op == 'OR'

def isValidOrPattern(arg1, op, arg2, out):
    return isOrPatter(arg1, op, arg2, out) and (containsGate(etArg1=out, etOp='XOR') or out == 'z45')

def isXYZeroPattern(arg1, op, arg2, out):
    if arg1 == 'x00' and arg2 == 'y00':
        if op == 'XOR':
            return out == 'z00'
        elif op == 'AND':
            return containsGate(etArg1=out, etOp='XOR')
    return False

def isXYAndPattern(arg1, op, arg2, out):
    return isXYPattern(arg1, op, arg2, out) and op == 'AND' and arg1[1:] == arg2[1:] and containsGate(etArg1=out, etOp='OR')

def isXYXorPattern(arg1, op, arg2, out):
    return isXYPattern(arg1, op, arg2, out) and op == 'XOR' and arg1[1:] == arg2[1:] and containsGate(etArg1=out, etOp='XOR')

def checIsValid(arg1, op, arg2, out):
    if isXYPattern(arg1, op, arg2, out):
        return isValidXYPattern(arg1, op, arg2, out)
    elif isZPattern(arg1, op, arg2, out):
        return isValidZPattern(arg1, op, arg2, out)
    elif isXorPatter(arg1, op, arg2, out):
        return isValidXorPattern(arg1, op, arg2, out)
    elif isOrPatter(arg1, op, arg2, out):
        return isValidOrPattern(arg1, op, arg2, out)
    return True

inValidWires = [out for arg1, op, arg2, out in gates if not checIsValid(arg1, op, arg2, out)]

print('Part 1:', zValue)                            # 52956035802096
print('Part 2:', ','.join(sorted(inValidWires)))    # hnv,hth,kfm,tqr,vmv,z07,z20,z28

inValidWires = []

def fixTwoGates(out1, out2):
    updateGate(etOut=out1, nOut='zzz')
    updateGate(etOut=out2, nOut=out1)
    updateGate(etOut='zzz', nOut=out2)
    inValidWires.extend((out1, out2))


i = 0
prevReg = None
while i < 45:
    xWire, yWire, zWire = [wire + str(i).zfill(2) for wire in ('x', 'y', 'z')]
    (_, _, _, outXor) = getGate(etArg1=xWire, etArg2=yWire, etOp='XOR')
    (_, _, _, outAnd) = getGate(etArg1=xWire, etArg2=yWire, etOp='AND')

    if i == 0:
        if outXor != zWire:
            fixTwoGates(outXor, zWire)
            continue
        prevReg = outAnd
        i += 1
        continue
    elif not containsGate(etArg1=prevReg, etArg2=outXor, etOp='XOR', etOut=zWire):
        if containsGate(etArg1=prevReg, etArg2=outXor, etOp='XOR'):
            (arg1, op, arg2, fakeOutZ) = getGate(etArg1=prevReg, etArg2=outXor, etOp='XOR')
            fixTwoGates(fakeOutZ, zWire)
        elif containsGate(etArg1=prevReg, etOp='XOR', etOut=zWire):
            (arg1, op, arg2, out) = getGate(etArg1=prevReg, etOp='XOR', etOut=zWire)
            fakeXor = arg1 if prevReg == arg2 else arg2
            fixTwoGates(fakeXor, outXor)
        elif containsGate(etArg1=outXor, etOp='XOR', etOut=zWire):
            (arg1, op, arg2, out) = getGate(etArg1=outXor, etOp='XOR', etOut=zWire)
            fakePrevReg = arg1 if outXor == arg2 else arg2
            fixTwoGates(fakePrevReg, prevReg)
            prevReg = fakePrevReg
        continue

    # if not containsGate(etArg1=prevReg, etArg2=outXor, etOp='AND'):
    #     print('not containsGate(etArg1=prevReg, etArg2=outXor, etOp=''AND'')')
    (_, _, _, outRegTmp) = getGate(etArg1=prevReg, etArg2=outXor, etOp='AND')

    # if not containsGate(etArg1=outRegTmp, etArg2=outAnd, etOp='OR'):
    #     print('not containsGate(etArg1=outRegTmp, etArg2=outAnd, etOp=''OR'')')
    (_, _, _, prevReg) = getGate(etArg1=outRegTmp, etArg2=outAnd, etOp='OR')

    i += 1

print('Part 2:', ','.join(sorted(inValidWires)))    # hnv,hth,kfm,tqr,vmv,z07,z20,z28
