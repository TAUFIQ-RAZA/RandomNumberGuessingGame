import random

print("Welcome to the Guessing Number Guessing Challenge!\nGuess the number between 1-100")
computer_choice = random.randint(1, 100)

attempts = 0
while True:
    user_choice = int(input("Guess the Number: "))
    if computer_choice == user_choice:
        print(f"Correct! you guessed the number in {computer_choice}!")
        attempts += 1
        break

    elif computer_choice > user_choice:
        print("Sorry, you guessed too low.")
        attempts += 1

    elif computer_choice < user_choice:
        print("Sorry, you guessed too high.")
        attempts += 1

print(f"You guessed the number in {attempts} attempts")