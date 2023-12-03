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
    numB = int(0)
    numG = int(0)
    numR = int(0)
    print(newDice)
    
    for d in range(len(newDice)):
        if newDice[d].isdigit(): 
            g = d + 1
            if newDice[g] == "red":
                numR = int(newDice[d])
            elif newDice[g] == "blue":
                numB = int(newDice[d])
            elif newDice[g] == "green":
                numG = int(newDice[d])
            

    print(numB, numG, numR)
    if (numB <= blue) and (numR <= red) and (numG <= green):
        return 1
    else:
        return 0 
main() 
