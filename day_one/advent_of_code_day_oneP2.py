import csv

number_set = []

# reads and removes junk from my csv
with open("DataDogOne.csv") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        number_set.append(row[0])

# test number set provided answer is 142
#number_set = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
charlie_hold_numbs = []

def main(): 
    pull_groups(number_set)
    print(totes_charles(charlie_hold_numbs))

def pull_groups(set_here):
    for sets in set_here:
        word_digit = []
        x = sets.lower().replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "nine").replace("zero","0").replace("on", "1").replace("tw", "2").replace("thre", "3").replace("fiv", "5").replace("seve", "7").replace("eigh", "8").replace("nin", "9").replace("on", "1").replace("wo", "2").replace("hree", "3").replace("ight", "8").replace("ine", "9")
        for i in range(len(x)):
            if x[i].isdigit():
                word_digit.append(x[i])
        y = int(word_digit[0] + word_digit[-1])
        charlie_hold_numbs.append(y)       

def totes_charles(x):
    y = 0
    for xs in x:
        y = y + xs

    return y

main()
