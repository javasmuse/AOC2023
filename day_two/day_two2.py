import csv
import re

holder = []
herd = []

with open("dataCat.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        holder.append(row)

def main():
    res = list(filter(None, holder))
    checkRow(res)
    print (finalCheck(herd))

def checkRow(games):
    # games is one row of data, one game, pull is one pull of dice
    for game in games:
        #remove blanks
        newGame = list(filter(None, game))
        #for i in range(len(newGame)):
        gameIDnumber = check_pull(newGame)
        herd.append(gameIDnumber)

def check_pull(pull):
    count = len(pull)
    topNumber = (count - 1)
            
    temp = re.findall(r'\d+', pull[0])
    res = temp
    GMid = int(res[0])
    poss = []
    newPull = pull.pop(0)
    
    for i in range(len(pull)): 
        pullOne = pull[i]
        poss.append(checkOneGroup(pullOne.split(',')))
    
    sumPoss = sum(poss)
 
    if sumPoss == topNumber:
        return GMid
    else:
        return 0

def checkOneGroup(cube):
    
    red = 12
    green = 13
    blue = 14
    bl = 0
    rd = 0
    gr = 0
    
    for i in range(len(cube)):
        
        if "blue" in cube[i]:
            temp = re.findall(r'\d+', cube[i])
            res = temp
            bl = int(res[0])
        elif "red" in cube[i]:
            temp = re.findall(r'\d+', cube[i])
            res = temp
            rd = int(res[0])
        elif "green" in cube[i]:
            temp = re.findall(r'\d+', cube[i])
            res = temp
            gr = int(res[0])
    
    if ((bl <= blue) and (rd <= red) and (gr <= green)):
        return 1
    else:
        return 0

def finalCheck(x):
    #x = list(dict.fromkeys(x))
    x = list(map(int, x))
    final = sum(x)
    return final

main() 
