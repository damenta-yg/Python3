from random import randint

random_number = randint(1,10)




guess_flag = False

#check the guess flag
while guess_flag != True:
    #first input of the game
    user_input = int(input("Guess the number between 1 and 10: "))

    #check wins
    if user_input == random_number:
        guess_flag = True
        print("Correctly guess! You win the match. . .")

        #check for replay games
        user_input_2 = input("Do you want to play again? (y/n): ").lower()
        while user_input_2 != 'y' and user_input_2 != 'n':
            user_input_2 = input("Do you want to play again? (y/n): ").lower()

        if user_input_2 == "y":
            random_number = randint(1,10)
            guess_flag = False
        elif user_input_2 == 'n':
            guess_flag = True
            print("Thank you for playing this games")
        else:
            print("Invalid Input")
            guess_flag = True
    elif user_input < random_number:
        print("Too low! Guess again please. . .")
    elif user_input > random_number:
        print("Too high! Guess again please. . .")