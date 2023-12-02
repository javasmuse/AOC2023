import csv

number_set = []

with open("AdventDay1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        number_set.append(f"{row[1]}")

# test number set provided answer is 142
#number_set = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

charlie_hold_numbs = []

def main(): 
    print(number_set[0], number_set[-1])
    pull_groups(number_set)
    print(totes_charles(charlie_hold_numbs))

def pull_groups(set_here):
    for sets in set_here:
        word_digit = []
        for i in range(len(sets)):
            if sets[i].isdigit():
                word_digit.append(sets[i])
        y = int(word_digit[0] + word_digit[-1])
        charlie_hold_numbs.append(y)

def totes_charles(x):
    y = 0
    for xs in x:
        y = y + xs

    return y

main()
