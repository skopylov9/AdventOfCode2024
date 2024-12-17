def toCombo(registers, operand):
    if operand in range(4):
        return operand
    return registers[operand - 4]

def runProgram(registers, instructions):
    A, B, C = registers
    pointer = 0

    out = []
    while pointer < len(instructions):
        opcode, operand = instructions[pointer], instructions[pointer + 1]

        if 0 == opcode:
            A = A // 2 ** toCombo((A, B, C), operand)
        elif 1 == opcode:
            B = B ^ operand
        elif 2 == opcode:
            B = toCombo((A, B, C), operand) % 8
        elif 3 == opcode:
            pointer = (operand - 2) if A else pointer
        elif 4 == opcode:
            B = B ^ C
        elif 5 == opcode:
            out.append(toCombo((A, B, C), operand) % 8)
        elif 6 == opcode:
            B = A // 2 ** toCombo((A, B, C), operand)
        elif 7 == opcode:
            C = A // 2 ** toCombo((A, B, C), operand)
        
        pointer += 2
    return out

# def runCustomProgram(A):
#     out = []
#     while A:
#         C = A >> ((A & 7) ^ 1)
#         out.append((A ^ C ^ 4) & 7)
#         A = A >> 3
#     return out

def fingARegForInstructions(instructions, A = 0):
    if runProgram((A, 0, 0), instructions) == instructions:
        return A

    for a in range(8):
        out = runProgram(((A << 3) + a, 0, 0), instructions)
        if out and out == instructions[len(instructions) - len(out):]:
            result = fingARegForInstructions(instructions, (A << 3) + a)
            if result != None:
                return result
    return None

registers, instructions = open('input.txt').read().split('\n\n')

registers = list(map(lambda line: int(line[12:]), registers.splitlines()))
instructions = list(map(int, instructions[9:].split(',')))

print('Part 1:', ','.join(map(str, runProgram(registers, instructions))))   # 4,1,7,6,4,1,0,2,7
print('Part 2:', fingARegForInstructions(instructions))                     # 164279024971453
