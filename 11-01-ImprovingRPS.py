from random import randint
import math



#comp_rps_choices = randint(0,2)
rps_choices = ["rock","paper","scissors"]
player1_choice = ""
set_round = 3
player_wins = 0
comp_wins = 0

#function section
def winners_check(c1,c2): #check wins
    global player_wins
    global comp_wins
    if(c1 != "rock" and c1 != "paper" and c1 != "scissors"):
        print("Invalid Input From Players!")
    elif c1 == c2:
        print("Draw Match!")
    elif c1 == "rock" and c2 == "scissors":
        player_wins += 1
        print("Player 1 Wins!")
    elif c1 == "paper" and c2 == "rock":
        player_wins += 1
        print("Player 1 Wins!")
    elif c1 == "scissors" and c2 == "paper":
        player_wins += 1
        print("Player 1 Wins!")
    else:
        comp_wins += 1
        print("Computer Wins!")





print(f"set round wins: {(math.ceil(set_round/2))}")

for num in range(set_round):
    player1_choice = input("Player 1 Choice:\n").lower()
    comp_rps_choices = randint(0,2)
    while player1_choice != "rock" and player1_choice !="paper" and player1_choice != "scissors":
        player1_choice = input("Player 1 Choice:\n").lower()
    player2_choice = rps_choices[comp_rps_choices]
    print("Player 1 Choice is:",player1_choice)
    print("Computer Choice is:",player2_choice)
    winners_check(player1_choice,rps_choices[comp_rps_choices])
    if(player_wins == math.ceil(set_round/2)): 
        print("Player Has Wins the game!")
        break
    elif(comp_wins == math.ceil(set_round/2)):
        print("Computer wins!")
        break


#winners_check(player1_choice,player2_choice)