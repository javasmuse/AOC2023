import csv
import re

red = int(12)
green = int(13)
blue = int(14)

sum_id = "int(0)"

holder = []
herd = []

def destruc(x):
    holder = []
    holder.append(x)
    game = holder[0]
    for i in range(len(holder)):
        m = re.search("1")
        herd.append(m)

with open("dataCat.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        destruc(row)



print(herd)
     



# create a list and name the list the game number