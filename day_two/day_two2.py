import csv
import re

holder = []
herd = []

redHold = []
blueHold = []
greenHold = []

powerCube = []

with open("dataCat.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        holder.append(row)

def main():
    checkRow(list(filter(None, holder)))
    print (sum(list(map(int, herd))))
    print (sum(list(map(int, powerCube))))

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
    
    temp = re.findall(r'\d+', pull[0])
    GMid = int(temp[0])
    poss = []
    pull.pop(0)
    
    checkGreatest(pull)
        
    for i in range(len(pull)): 
        pullOne = pull[i]
        poss.append(checkOneGroup(pullOne.split(',')))
        
    if sum(poss) == (count - 1):
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
            bl = int(temp[0])
        elif "red" in cube[i]:
            temp = re.findall(r'\d+', cube[i])
            rd = int(temp[0])
        elif "green" in cube[i]:
            temp = re.findall(r'\d+', cube[i])
            gr = int(temp[0])
    
    
    if ((bl <= blue) and (rd <= red) and (gr <= green)):
        return 1
    else:
        return 0
        
def checkGreatest(cubes): 
    blueHold = []
    redHold = []
    greenHold = []
        
    for i in range(len(cubes)): 
        cube = cubes[i]
        smurf = cube.split(',')
       
        for i in range(len(smurf)):
            if "blue" in smurf[i]:
                temp = re.findall(r'\d+', smurf[i])
                blueHold.append(int(temp[0]))
                
            elif "red" in smurf[i]:
                temp = re.findall(r'\d+', smurf[i])
                redHold.append(int(temp[0]))
                
            elif "green" in smurf[i]:
                temp = re.findall(r'\d+', smurf[i])
                greenHold.append(int(temp[0]))
        
    #print(f"Blue {blueHold}, Red {redHold}, Green {greenHold}")

    redHold.sort(reverse = True)
    poppy = redHold.pop(0)
    blueHold.sort(reverse = True)
    moon = blueHold.pop(0)
    greenHold.sort(reverse = True)
    tree = greenHold.pop(0)

    powerRanger = (poppy * moon * tree)

    powerCube.append(powerRanger)

main() 
