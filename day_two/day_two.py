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

def checkRow(games):
    # games is one row of data, one game, pull is one pull of dice
    for game in games:
    
        newGame = list(filter(None, game))
 
        for i in range(len(newGame)):
            game_id = newGame[0]
            check_Group(newGame[i].split())           

def check_Group(dice):

    for i in range(len(dice)): 

        bl = "blue"
        gr = "green"
        rd = "red"
        gm = "Game"

        numB = ""
        numG = ""
        numR = ""
        gameID = ""

        if bl in dice: 
            x = dice.index(bl) - 1
            print(x)
            numB = int(dice[x])
            print(numB)
        else:
            numB = 24
        
        if gr in dice:
            x = dice.index(gr) - 1
            numG = int(dice[x])
        else:
            numG = 24
        
        if rd in dice: 
            x = dice.index(rd) - 1
            numR = int(dice[x])
        else:
            numR = 24

    if (numB <= blue) and (numR <= red) and (numG <= green):
        herd.append("goat")
        print("Goat")

def findRetColor():
    

main() 
