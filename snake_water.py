import random

# 1. Setup dictionaries with matching data types (all integer keys)
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# 2. Get computer's choice randomly from the valid numbers
computer = random.choice([1, -1, 0])

# 3. Get user input and convert it
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Check if the user entered a valid character to prevent crash
if youstr in youDict:
    younum = youDict[youstr]

    # Print the choices clearly
    print(f"\nYou chose: {reverseDict[younum]}")
    print(f"Computer chose: {reverseDict[computer]}\n")

    # 4. Game Logic
    if computer == younum:
        print("It's a draw!")
    else:
        if computer == -1 and younum == 1:       # Water vs Snake
            print("You win!")
        elif computer == -1 and younum == 0:     # Water vs Gun
            print("You lose!")
        elif computer == 1 and younum == -1:     # Snake vs Water
            print("You lose!")
        elif computer == 1 and younum == 0:      # Snake vs Gun
            print("You win!")
        elif computer == 0 and younum == -1:     # Gun vs Water
            print("You win!")
        elif computer == 0 and younum == 1:      # Gun vs Snake
            print("You lose!")
        else:
            print("Something went wrong!")
else:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")