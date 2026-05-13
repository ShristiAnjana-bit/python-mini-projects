print("Guess the number")
import random
number = random.randint(1,100)
attempts = 0
while True:
    guess = int(input("Enter your guess:"))
    attempts += 1
    if guess == number:
        print("Correct!")
        break
    elif guess < number:
         print("Too low!")
    else:
        print("Too high!")