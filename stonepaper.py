import random
player_score = 0
computer_score =0
#the game option availabe
options = ["stone", "paper","scissor"]

print("--- Welcome to Stone, Paper, Scissors! Best of 5 Rounds---")

#Run the game for exactly 5 rounds
for round_num in range(1,6):
    print(f"\n---Round {round_num} ---")

    #Get player input
    choices = input("Enter  stone, paper, or scissor: ").lower()

    #Input validation: make sure the player typed a valid option
    if choices not in options:
        print("Invalid choice! Computer gets a free point for your mistake.")
        computer_score += 1
        continue

     #computer makes a random choice from the list
    computer = random.choice(options)
    if choices == computer:
        print("It's a tie for this round!(no points given)")
    elif(choices == "stone" and computer == "scissor") or \
        (choices == "paper" and computer ==  "stone") or \
        (choices == "scissor" and computer == "paper"):
        player_score += 1
    else:
        print("Computer won this round!")
        computer_score += 1

#after the loop ends
if player_score > computer_score:
    print("Congratulation! you won the game!")
elif computer_score > player_score:
    print("Game over! The computer won.")
else:
    print("The entire game ended in a tie!")
