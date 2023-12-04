import re
import numpy as np

textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Advent Day 4 Inputs.txt")
# textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Testing Day 4.txt")

totalCopies = np.ones(len(textFile.readlines()), dtype=int)
# print(len(totalCopies))

textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Advent Day 4 Inputs.txt")
# textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Testing Day 4.txt")

totalScratchcards = 0
pointsPerCard = np.zeros(len(textFile.readlines()), dtype=int)
winningNumsPerCard = np.zeros_like(pointsPerCard)

textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Advent Day 4 Inputs.txt")
# textFile = open("C:\\Users\Predinchuk\AdventOfCode2023\Testing Day 4.txt")

for line in textFile.readlines():
    # print(line)
    cardWinsNums = line.replace('|', ':').replace('\n', '').split(':')
    # print(cardWinsNums)
    
    cardNum = re.findall(r'\d+', cardWinsNums[0])
    # print(cardNum)

    winningNums = re.findall(r'\d+', cardWinsNums[1])
    # print(winningNums)

    yourNums = re.findall(r'\d+', cardWinsNums[2])

    overlapNums = set(winningNums) & set(yourNums)
    # print(overlapNums)
    # print(len(overlapNums))

    if len(overlapNums) > 0:
        pointsPerCard[int(cardNum[0]) - 1] = 2**(len(overlapNums) - 1)
        winningNumsPerCard[int(cardNum[0]) - 1] = len(overlapNums)

# print(f"totalCopies: {totalCopies}")
# print(f"winningNumsPerCard {winningNumsPerCard}")

for currentCard in np.arange(len(totalCopies)):
    # print(currentCard)
    
    copyDepth = winningNumsPerCard[currentCard]
    # print(f"copydepth: {copyDepth}")
    copyPlace = currentCard + 1
    # print(f"copyplace: {copyPlace}")
    
    while copyPlace <= copyDepth + currentCard and copyPlace < len(totalCopies):
        totalCopies[copyPlace] += totalCopies[currentCard]
        copyPlace += 1
    # print(f"totalCopies: {totalCopies}")
    
# print(f"totalcopies: {totalCopies}")
# print(f"pointPerCard: {pointsPerCard}")
# print(f"winningNumsPerCard {winningNumsPerCard}")

index = 0
while index < len(totalCopies):
    totalScratchcards += totalCopies[index]
    index += 1
        
print(totalScratchcards)