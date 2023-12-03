import csv
import re

red = int(12)
green = int(13)
blue = int(14)

holder = []
herd = []

with open("dataCat.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        holder.append(row)

def main():
    res = list(filter(None, holder))
    checkRow(res)  
    print(len(herd))
    print(sum(herd))

def checkRow(games):
    # games is one row of data, one game, pull is one pull of dice
    for game in games:
        #remove blanks
        newGame = list(filter(None, game))

        # assign game id
        gameIDgroup = newGame[0]

        yars = []
        for i in range(len(gameIDgroup)):
            if (gameIDgroup[i].isdigit()):
                yars.append(gameIDgroup[i])
        
        converted_list = map(str, yars)
        result = ''.join(converted_list)
        gmIDnum = int(result)
 
        gameLen = (len(newGame) - 1) 
        # counter to check for possible games, will check vs gameLen at end
        checkGL = 0 

        # check each pull for possible or not, parse in next function return 1 or 0 for yes or no eval in next set of code
        for k in range(len(newGame)):
            checkGL = (checkGL + check_Group(newGame[k]))
       
            # split and send index 
            # parse yes or no and return int
        # check sum return int to length game - 1 for yes or no
        # set gm value to id or zero and send to herd
        if checkGL == gameLen:
            herd.append(gmIDnum)
        else: 
            herd.append(int(0))
            print(0)

        # back in main sum herd '''

def check_Group(dice):
    
    if (dice[0] == "G"):
        return 0
    
    newDice = dice.split()
    bl = "blue"
    gr = "green"
    rd = "red"
    numB = ""
    numG = ""
    numR = ""

    for i in range(len(newDice)):
        if bl in newDice: 
            x = newDice.index(bl) - 1
            numB = int(newDice[x])
        else:
            numB = 0

        if gr in newDice:
            x = newDice.index(gr) - 1
            numG = int(newDice[x])
        else:
            numG = 0

        if rd in newDice: 
            x = newDice.index(rd) - 1
            numR = int(newDice[x])
        else:
            numR = 0

    if (numB <= blue) and (numR <= red) and (numG <= green):
        return 1
    else:
        return 0 
main() 
