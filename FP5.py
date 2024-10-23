import random

# Define functions to return colored text using ANSI escape codes
def red_text(text):
    return f"\033[31m{text}\033[0m"  # Red

def blue_text(text):
    return f"\033[34m{text}\033[0m"  # Blue

def green_text(text):
    return f"\033[32m{text}\033[0m"  # Green

def yellow_text(text):
    return f"\033[33m{text}\033[0m"  # Yellow

def magenta_text(text):
    return f"\033[35m{text}\033[0m"  # Magenta

# Optional: Random color function
def random_color(text):
    color_functions = [red_text, blue_text, green_text, yellow_text, magenta_text]
    return random.choice(color_functions)(text)

# Main program logic
def main():
    print("Welcome to the Text Colorizer!")
    colors = {
        "red": red_text,
        "blue": blue_text,
        "green": green_text,
        "yellow": yellow_text,
        "magenta": magenta_text,
        "random": random_color
    }

    while True:
        # Prompt the user to select a color or quit
        color_choice = input("Choose a color (red, blue, green, yellow, magenta, random) or 'quit' to exit: ").strip().lower()

        if color_choice == 'quit':
            print("Goodbye! Thanks for using the Text Colorizer.")
            break

        if color_choice in colors:
            user_text = input("Enter the text to colorize: ")
            # Print the text in the selected color
            print(colors[color_choice](user_text))
        else:
            print("Invalid color. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
