# recieve game results 
# games id by id
# sort number of R B G per game
# determine if possible given the number of marbles and possible combos
# save the Game ID of possible 
# sum Game ID return this

'''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

# RGB 12 13 14 

# input the csv to a nested dictionary
# read in each as string 
# - split at ; 
# - regex digit before g (b r etc), digit b => b given ,, if all three correct , yes 

given_bag = {
    "red" : "12",
    "green" : "13",
    "blue" : "14"
}

games = {
    "game1" : {
        "pull1" : {
            "red" : "4",
            "blue" : "3",
        },
        "pull2" : {
            "red" : "1",
            "green" : "2",
            "blue" : "6"
        },
        "pull3" : {
            "green" : "2",
        }
    },
    "game2" : {
        "pull1" : {
            "blue" : "1",
            "green" : "2"
        },
        "pull2": {
            "green" : "3",
            "blue" : "4",
            "red" : "1"
        },
        "pull3" : {
            "green" : "1",
            "blue" : "1"
        }    
    },
    "game3": {
        "pull1" : {
            "green" : "8",
            "blue" : "6",
            "red" : "20"
        },
        "pull2" : {
            "blue" : "5",
            "red" : "4",
            "green" : "13"
        },
        "pull3" : {
            "green" : "5",
            "red" : "1"
        } 
    },
    "game4" : {
        "pull1": {
            "green" : "1", 
            "red" : "2", 
            "blue" : "6"
        },
        "pull2" : {
            "green" : "3", 
            "red" : "6"
        },
        "pull3" : {
            "green" : "3", 
            "blue" : "15", 
            "red" : "14"
        } 
    },
    "game5" : {
        "pull1" : {
            "red" : "6", 
            "blue" : "1", 
            "green" : "3"

        },
        "pull2" : {
            "blue" : "2", 
            "red" : "1", 
            "green" : "2"
        } 
    }
    }


print (games.values)



# create a list and name the list the game number