import os

def get_valid_answer(prompt):
    """Function to get a valid answer option from the user."""
    while True:
        answer = input(prompt).lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print("Invalid input. Please enter a valid option (a, b, c, or d).")

def main():
    print("Welcome to the Question Collector!")
    print("You can create multiple questions with four answer options each.")
    print("Type 'exit' at any time to quit the program.\n")
    
    questions_data = []  # list to store all questions and answers

    while True:
        # ask for the question
        question = input("Please enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        
        # ask for the possible answers
        answers = {}
        for option in ['a', 'b', 'c', 'd']:
            answer = input(f"Please enter answer option {option}: ")
            answers[option] = answer
        
        # ask for the correct answer
        print("Please enter the correct answer (a, b, c, or d):")
        correct_answer = get_valid_answer("Your choice: ")
        
        # store the question and answers in a dictionary
        question_entry = {
            "question": question,
            "answers": answers,
            "correct_answer": correct_answer
        }
        questions_data.append(question_entry)  # add to the list of questions
        
        print("Question added successfully!\n")

    # write the collected data to the Desktop
    try:
        file_path = "questions.txt"

        print(f"File saved to: {os.path.abspath(file_path)}")
        
        with open(file_path, "w") as file:
            for entry in questions_data:
                file.write(f"Question: {entry['question']}\n")
                for option, answer in entry['answers'].items():
                    file.write(f"  Option {option}: {answer}\n")
                file.write(f"  Correct Answer: {entry['correct_answer']}\n\n")
        
        print(f"Questions saved to: {file_path}")
        os.system(f'notepad "{file_path}"')  # open file in Notepad (Windows only)

        print("Questions saved successfully!")

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

    # summary of all questions added
    print("\nThank you for using the Question Collector!")
    print("Here is a summary of the questions you added:\n")
    for entry in questions_data:
        print(f"Question: {entry['question']}")
        for option, answer in entry['answers'].items():
            print(f"  Option {option}: {answer}")
        print(f"  Correct Answer: {entry['correct_answer']}\n")

if __name__ == "__main__":
    main()