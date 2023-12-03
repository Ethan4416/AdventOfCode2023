textFile = open("D:\\predi\Advent Code 2023\Advent Day 2 Inputs.txt")
# textFile = open("D:\\predi\Advent Code 2023\Testing Day 2.txt")

currentGame = 0
colourOptions = ["blue", "red", "green"]
viableGameTotal = 0

for game in textFile:
    
    gamePower = 1
    colourNeededDict = {"blue" : 0,
                        "red" : 0,
                        "green" : 0}
    currentGame += 1

    if 0 < currentGame < 10:
        game = game[8:-1]
    elif 10 <= currentGame < 100:
        game = game[9:-1]
    else:
        game = game[10:-1]
    matchList = game.split(";")

    for match in matchList:
        match = match.replace(" ", "")
        results = match.split(",")
        for result in results:
            for colour in colourOptions:
                if colour in result:
                    resultNum = result.replace(colour, "")
                    if int(resultNum) > int(colourNeededDict[colour]):
                        colourNeededDict[colour] = int(resultNum)
    
    for colour in colourOptions:
        gamePower = gamePower * colourNeededDict[colour]
    viableGameTotal += gamePower


print(viableGameTotal)
                    

