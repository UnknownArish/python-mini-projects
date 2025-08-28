import random

number_to_guess = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 attempts to guess it.")

while attempts < 3:
    user_guess = int(input("Take a guess: "))
    attempts += 1

    if user_guess == number_to_guess:
        print("Congratulations! You guessed the number.")
        break
    elif user_guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")

if attempts == 3:
    print("Sorry, you've used all your attempts.")
    print("The number was:", number_to_guess)