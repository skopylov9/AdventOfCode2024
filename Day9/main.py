def createUnZippedDiskMap(files, freeSpaces):
    files = [[fDesc[1]] * fDesc[0] for fDesc in files]
    freeSpaces = [['.'] * count for count in freeSpaces]
    unZippedDiskMap = [files[i] + freeSpaces[i] for i in range(len(files))]
    return [cell for block in unZippedDiskMap for cell in block]

def calcCheckSum(unZippedDiskMap):
    return sum(index * val for index, val in enumerate(unZippedDiskMap) if val != '.')

def deFragmentDiskStrong(unZippedDiskMap):
    leftIndex, rightIndex = 0, len(unZippedDiskMap) - 1
    while leftIndex != rightIndex:
        if unZippedDiskMap[leftIndex] != '.':
            leftIndex += 1
        elif unZippedDiskMap[rightIndex] == '.':
            rightIndex -= 1
        else:
            tmp = unZippedDiskMap[leftIndex]
            unZippedDiskMap[leftIndex] = unZippedDiskMap[rightIndex]
            unZippedDiskMap[rightIndex] = tmp
    return unZippedDiskMap

def deFragmentDiskLight(files, freeSpaces):
    fileIndex = len(files) - 1
    prevIndexMap = [0 for _ in range(10)]
    while fileIndex > 0:
        for freeIndex in range(prevIndexMap[files[fileIndex][0]], fileIndex):
            if freeSpaces[freeIndex] >= files[fileIndex][0]:
                prevIndexMap[files[fileIndex][0]] = freeIndex
                freeSpaces[freeIndex] -= files[fileIndex][0]
                freeSpaces[fileIndex - 1] += files[fileIndex][0] + freeSpaces.pop(fileIndex)
                freeSpaces.insert(freeIndex, 0)
                files.insert(freeIndex + 1, files.pop(fileIndex))            
                break
        else:
            fileIndex -= 1
    return files, freeSpaces

diskMap = open('input.txt').read()
files = [(int(val), index // 2) for index, val in enumerate(diskMap) if not index % 2]
freeSpaces = [int(val) for index, val in enumerate(diskMap) if index % 2]
freeSpaces.append(0)

print('Part 1:', calcCheckSum(deFragmentDiskStrong(createUnZippedDiskMap(files, freeSpaces))))  # 6432869891895
print('Part 2:', calcCheckSum(createUnZippedDiskMap(*deFragmentDiskLight(files, freeSpaces))))  # 6467290479134
