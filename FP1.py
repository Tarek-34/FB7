
def mad_lib():
    print("Welcome to the Mad Libs Game!")
    print("Follow the instructions below and provide the requested words to complete a fun story.\n")

    # Collecting user inputs
    adjective = input("Enter an adjective: ")
    large_objects = input("Enter large objects (plural): ")
    body_part = input("Enter a body part: ")
    restaurant = input("Enter a restaurant: ")
    food1 = input("Enter a type of food: ")
    food2 = input("Enter another type of food: ")
    large_object = input("Enter a large object (singular): ")

    # Story template
    story = f"""
    I’ve had a very {adjective} day.
    This morning, I dropped a box of {large_objects} on my {body_part}.
    Then, at lunch, I went to {restaurant} for their delicious {food1},
    but the waiter brought me {food2}, which I was not hungry for.
    Finally, on my way home, I was cut off by a van with a large {large_object}
    strapped to the roof.
    """

    # Display the final story
    print("\nHere is your Mad Lib story:")
    print(story)

# Run the Mad Lib game
if __name__ == "__main__":
    mad_lib()
