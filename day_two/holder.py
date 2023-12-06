#Enter Python code here and hit the Run button.
import re

bl = []
rd = []
gr = []

def main(): 
    pull = "12 blue, 6 green, 5 red"
    pluck = "9 blue, 3 green, 2 red"
    grab = "4 blue, 12 red, 32 green"
    
    lofLs = [pull, pluck, grab]
    
    for lol in lofLs:
        divided = lol.split(',')
        checkGreatest(divided)

    rd.sort(reverse = True)
    poppy = rd.pop(0)
    bl.sort(reverse = True)
    moon = bl.pop(0)
    gr.sort(reverse = True)
    tree = gr.pop(0)
    
    print (poppy, moon, tree)
    powerGame = (poppy * moon * tree)
    
    print (powerGame)
    

def checkGreatest(smurf): 
    
    for i in range(len(smurf)):
        if "blue" in smurf[i]:
            temp = re.findall(r'\d+', smurf[i])
            bl.append(int(temp[0]))
            
        elif "red" in smurf[i]:
            temp = re.findall(r'\d+', smurf[i])
            rd.append(int(temp[0]))
            
        elif "green" in smurf[i]:
            temp = re.findall(r'\d+', smurf[i])
            gr.append(int(temp[0]))
  
    
main()
