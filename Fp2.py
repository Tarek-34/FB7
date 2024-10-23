import random

def generate_powerball_numbers():
    # Greeting message
    print("Welcome to the PowerBall Number Generator!")
    print("Your lucky numbers are:")

    # Generate five white ball numbers (1-69)
    white_balls = [random.randint(1, 69) for _ in range(5)]

    # Generate one red ball number (1-26)
    red_ball = random.randint(1, 26)

    # Print white balls with single space between them
    print(" ".join(map(str, white_balls)), end="   ")

    # Print red ball (with three spaces before it)
    print(red_ball)

    # Farewell message
    print("Good luck! Thank you for using the PowerBall Number Generator.")

# Call the function to generate and display the numbers
generate_powerball_numbers()
