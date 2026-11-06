import random


def guess_the_number():
    secret = random.randint(1, 20)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I picked a number between 1 and 20. Can you guess it?")

    while attempts < 5:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it! The number was {secret}.")
            return

        remaining = 5 - attempts
        print(f"Attempts left: {remaining}")

    print(f"Out of attempts! The number was {secret}.")


if __name__ == "__main__":
    guess_the_number()
