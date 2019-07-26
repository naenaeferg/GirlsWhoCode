from random import*
aRandomNumber = randint(1, 20)
i=0
while i < 3:
    i += 1
    guess = input ("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric():
        print("that's not a positive whole number, try again!")
    else:
        guess = int(guess)

    if guess==aRandomNumber
        print("good job!")
        guessedNum = True
    elif guess < randomNum:
        print("guess higher")
    else:
        print ("guess lower")
    i += 1

    if not guessedNum:
        print ("Sorry you lost" "try again")
    
    
