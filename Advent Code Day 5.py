import numpy as np
import re

# textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Advent Day 5 Inputs.txt")
textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Testing Day 5.txt")

parsedData = []
mapData = []

for line in textFile.readlines():
    if line != "\n":
        # print(f"appending to parsedData: {line}")
        parsedData.append(line)
    else:
        mapData.append(parsedData)
        parsedData = []
mapData.append(parsedData)

seedRange = re.findall(r'\d+', (mapData[0])[0])
seedRange = [int(x) for x in seedRange]
seeds = []
i = 0
# print(seedRange)
# print(list(np.arange(seedRange[i], seedRange[i] + seedRange[i+1])))
# print("printed above")


while i < len(seedRange):
    seeds = seeds + [seedRange[i], seedRange[i] + seedRange[i+1] - 1]
    i += 2
# print(seeds)

seedsToAdd = []

for mapper in mapData[1:]:
    for mapInstruction in mapper[1:]:

        destSourceAmount = re.findall(r'\d+', mapInstruction)
        source = int(destSourceAmount[1])
        amount = int(destSourceAmount[2])

        i = 0
        while i < len(seeds):
            if seeds[i] < source < seeds[i+1]:
                seedsToAdd = seedsToAdd + [source]
            if seeds[i] < source + amount - 1 < seeds[i+1]:
                seedsToAdd = seedsToAdd + [source + amount -1]
            i += 2

seeds = seeds + seedsToAdd
print(seeds)

for mapper in mapData[1:]:
    print(f"mapper: {mapper}")

    alreadyUpdated = []
    oldseeds = seeds.copy()

    for mapInstruction in mapper[1:]:
        print(f"seeds: {seeds}")

        # print(f"current instruction: {mapInstruction}")
        
        destSourceAmount = re.findall(r'\d+', mapInstruction)
        destination = int(destSourceAmount[0])
        source = int(destSourceAmount[1])
        amount = int(destSourceAmount[2])


        for seed in oldseeds:
            # print(f"current seed {seed}")
            if source <= seed < source + amount:
                # print(f"source ({source}) <= seed ({seed}) < source + amount ({source + amount})")
                seedIndex = oldseeds.index(seed)
                if seedIndex not in alreadyUpdated:
                    # print(f"seedIndex ({seedIndex}) is not is {alreadyUpdated}")
                    seeds[seedIndex] = destination - source + seed
                    # print(f"seed {seed} updated to {seeds[seedIndex]}")
                    alreadyUpdated.append(seedIndex)

print(seeds)
print(min(seeds))