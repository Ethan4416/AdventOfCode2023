textFile = open("D:\\predi\Advent Code 2023\Advent Day 1 Inputs.txt")
# textFile = open("D:\\predi\Advent Code 2023\input.txt")
# textFile = open("D:\\predi\Advent Code 2023\Testing Day 1.txt")

sum = 0

numDictionary = {"one" : "1",
              "two" : "2",
              "three" : "3",
              "four" : "4",
              "five" : "5",
              "six" : "6",
              "seven" : "7",
              "eight" : "8",
              "nine" : "9"
              }

numWords = ["one", "two", "three", "four", 'five', "six", "seven", "eight", "nine"]

for line in textFile.readlines():

    indexInLine = []
    replacementDict = {}

    for number in numWords:
        try:
            firstindex = line.index(number)
            lastindex = line.rindex(number)

            indexInLine.append(firstindex)
            replacementDict[firstindex] = number

            if(firstindex != lastindex):
                indexInLine.append(lastindex)
                replacementDict[lastindex] = number  
        except:
            pass

    indexInLine.sort()

    offset = 0
    for entry in indexInLine:
        line = line[:(entry+offset)] + numDictionary[replacementDict[entry]] + line[(entry+offset):]
        offset += 1    
    firstOccurance = True
    first = 0
    last = 0
    for char in line:
        if char.isdigit():
            if firstOccurance:
                first = char
                firstOccurance = False
            last = char
    combinedNum = first+last
    sum += int(combinedNum)
print(sum)