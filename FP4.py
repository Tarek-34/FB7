def study_trivia():
    # Define a dictionary with trivia questions and answers
    trivia_questions = {
        "What is the capital of France?": "Paris",
        "Who wrote the play 'Hamlet'?": "Shakespeare",
        "What is the smallest planet in our solar system?": "Mercury",
        "What element does 'O' represent on the periodic table?": "Oxygen",
        "How many continents are there on Earth?": "7"
    }

    print("Welcome to the Trivia Study Program!")
    print("Answer the following questions:")

    # Loop through the dictionary to display each question and get user input
    for question, correct_answer in trivia_questions.items():
        user_answer = input(f"{question} ").strip()

        # Provide feedback based on the user's answer
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    # Farewell message
    print("Thanks for playing! Keep studying and good luck!")

# Call the function to run the program
study_trivia()
