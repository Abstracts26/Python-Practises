import random

number_range = (1, 100)

guess_history = []

secret_number = random.randint(number_range[0], number_range[1])
print("Guess the secret number between", number_range[0], "and", number_range[1])

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    guess_history.append(guess)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {len(guess_history)} attempts.")
        print("Your guesses were:", guess_history)
        break

print("Thank you for playing!")




        


