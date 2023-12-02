# recieve game results 
# games id by id
# sort number of R B G per game
# determine if possible given the number of marbles and possible combos
# save the Game ID of possible 
# sum Game ID return this

# doesn't matter b/c the i will be the game id, so treat as list and combine  R B G 
# save that in a new list with 0 as id
# compare to possibles


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

games = {
    "game1": {
        "red": "4",
        "blue": "3",
        "green": "2",
        "red": "1",
        "green": "2",
        "blue": "6"
    },
    "game2": {
        "blue": "1",
        "green": "2",
        "green": "3",
        "blue": "4",
        "red": "1", 
        "green": "1",
        "blue": "1"
    },
    "game3": {
        "green": "8",
        "blue": "6",
        "red": "20",
        "blue": "5",
        "red": "4",
        "green": "13",
        "green": "5",
        "red": "1"
    },
    "game4": {
        "green": "1", 
        "red": "2", 
        "blue": "6", 
        "green": "3", 
        "red": "6", 
        "green": "3", 
        "blue": "15", 
        "red": "14"

    },
    "game5": {
        "red": "6", 
        "blue": "1", 
        "green": "3", 
        "blue": "2", 
        "red": "1", 
        "green": "2"
    }
    
    }


print (games)