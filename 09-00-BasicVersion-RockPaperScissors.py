print("...rock...")
print("...paper...")
print("...scissors...")

print("Enter Player 1 Choice: ")
player1_choice = input()

i = 0

while i < 10:
    print("***No Cheating Allowed***")
    print("\n")
    print("\n")
    i = i + 1


print("Enter Player 2 Choice: ")
player2_choice = input()

if player1_choice == player2_choice:
    print("It is a draw match!")
elif player1_choice == "rock" and player2_choice == "scissors":
    print("Player 1 Wins!")
elif player1_choice == "paper" and player2_choice == "rock":
    print("Player 1 Wins!")
elif player1_choice == "scissors" and player2_choice == "paper":
    print("Player 1 Wins!")
elif player2_choice == "rock" and player1_choice == "scissors":
    print("Player 2 Wins!")
elif player2_choice == "paper" and player1_choice == "rock":
    print("Player 2 Wins!")
elif player2_choice == "scissors" and player1_choice == "paper":
    print("Player 2 Wins!")
else:
    print("Invalid Input")    