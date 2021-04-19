#   IMPORT THE random MODULE, SO WE HAVE ACCESS TO THE randint() FUNCTION
import random

guesses_left = 3
player_won = False

while guesses_left > 0 and player_won == False:
    # GENERATE A RANDOM NUMBER BETWEEN 0 AND 10
    random_number = random.randint(0, 10)
    #   FOR TESTING PURPOSE RIGHT NOW
    print("THe random number is " + str(random_number))
    #   GET THE USERS GUESS
    user_guess = int(input("Guess a number between 0 and 10: "))
    #   CHECK IF THE user_guess MATCHES THE random_number
    if user_guess == random_number:
        print("Congrats, you won!")
        player_won = True
    else:
        print("I'm sorry please try again")
        #   UPDATE THE guesses_left VARIABLE
        guesses_left = guesses_left - 1
        print("You have " + str(guesses_left) + " guesses left")
