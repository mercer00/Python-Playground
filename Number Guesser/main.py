# create number guesser
# chances
# easy: 30% or 0.3
# medium: 20% or 0.2
# hard: 10% or 0.1
# god: 5% or 0.05
# if medium , then chances will be 20% of the total outcomes , therefore if total outcomes are 10 , then chances will be 2.


from random import randint


difficulties = {"easy": 0.3, "medium": 0.2, "hard": 0.1, "god": 0.05}
print("Welcome to Guess The Number!")
print("Guess the number from a range of your choosing!")

while True:
    gameStart = input("New Game?(y/n): ")
    if gameStart == "n":
        exit()
    if gameStart != "y":
        continue
    while True:
        gameDifficulty = input("Difficulty (easy, medium, hard, god): ")
        if gameDifficulty not in difficulties:
            continue
        else:
            break
    while True:
        gameRange = input("Number range(ex, 1-10): ")
        intRange = gameRange.split("-")
        try:
            rangeStart = int(intRange[0])
            rangeEnd = int(intRange[1])
        except:
            continue
        print(f"Total possible outcomes are: {rangeEnd}")
        gameChances = int(rangeEnd * difficulties[gameDifficulty])
        if gameChances < 1:
            gameChances = 1
        print(f"Total chances: {gameChances}")
        numberList = list(range(rangeStart, rangeEnd + 1))
        randomNumber = randint(rangeStart, rangeEnd)
        while True:
            if gameChances == 0:
                print(f"You lost! , the answer was {randomNumber}")
                break
            userAns = int(input("Guess: "))
            if userAns == randomNumber:
                print(f"You Win! , {randomNumber} is the correct answer!")
                break
            else:
                print("Wrong! Try again")
                gameChances -= 1
                continue
        newGame = input("Continue playing with same difficulty?(y/n): ")
        if newGame == "n":
            break
