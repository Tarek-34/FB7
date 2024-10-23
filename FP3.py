import random

def number_guessing_game():
    # Greeting and asking if the user wants to play
    play = input("Welcome! Do you want to play the number guessing game? (yes/no): ").strip().lower()

    if play == "no":
        print("Maybe next time! Goodbye!")
        return  # Exit the program if the user says no

    elif play == "yes":
        print("Great! I have chosen a number between 1 and 10. Try to guess it!")

        # Generate a random secret number between 1 and 10
        secret_number = random.randint(1, 10)

        while True:
            try:
                # Ask the user to guess the number
                guess = int(input("Enter your guess: "))

                # Check if the guess is correct, too high, or too low
                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You've guessed the number!")
                    break  # Exit the loop if the guess is correct

            except ValueError:
                print("Please enter a valid number.")  # Handle non-integer input

    else:
        print("Invalid input. Please restart the game.")

    # Farewell message after the game ends
    print("Thanks for playing! Goodbye!")

# Call the function to run the game
number_guessing_game()
