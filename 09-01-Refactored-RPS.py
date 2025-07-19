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

def checkWins(c1,c2):
    if (c1 != "rock" and c1 != "paper" and c1 !="scissors") or (c2 != "rock" and c2 != "paper" and c2 !="scissors"):
        print ("Invalid")
        return
    
    if c1 == c2:
        print("Match is Draw!")
    elif c1 == "paper":
        if c2 == "rock":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
    elif c1 == "rock":
        if c2 == "scissors":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")        
    elif c1 == "scissors":
        if c2 == "paper":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
    else:
        print("Invalid Input!")

checkWins(player1_choice,player2_choice)
