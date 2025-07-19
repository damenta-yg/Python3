from random import randint

comp_rps_choices = randint(0,2)
rps_choices = ["rock","paper","scissors"]

player1_choice = input("Player 1 Choice:\n").lower()
player2_choice = rps_choices[comp_rps_choices]

def winners_check(c1,c2):
    if(c1 != "rock" and c1 != "paper" and c1 != "scissors"):
        print("Invalid Input From Players!")
    elif c1 == c2:
        print("Draw Match!")
    elif c1 == "rock" and c2 == "scissors":
        print("Player 1 Wins!")
    elif c1 == "paper" and c2 == "rock":
        print("Player 1 Wins!")
    elif c1 == "scissors" and c2 == "rock":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

print("Player 1 Choice is:",player1_choice)
print("Computer Choice is:",player2_choice)
winners_check(player1_choice,player2_choice)