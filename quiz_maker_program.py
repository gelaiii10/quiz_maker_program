def get_valid_answer(prompt):
    # docstring to explain the purpose of the function
    """Function to get a valid answer option from the user"""   
    while True: # while loop to continue collecting questions and answers until the user types 'exit'
        answer = input(prompt).lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        else:
            # if the input is invalid, it will print an error message and prompt the user to enter again.
            print("Invalid input. Please enter a valid option (a, b, c, or d)") 

def main(): 
    # initial messages
    print("welcome to the question collector")
    print("you can create multiple questions with four answer options each")
    print("type 'exit' at any time to quit the program")

    questions_data = []  # list to store all questions and answers

    while True:
        # ask for the question
        question = input("enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break 

    # ask for the possible answers
        answers = {}
        for option in ['a', 'b', 'c', 'd']:
            answer = input(option)
            answers[option] = answer

        # ask for the correct answer
        print("enter the correct answer (a, b, c, or d):")
        correct_answer = get_valid_answer("your choice: ")

        # store the question and answers in a dictionary
        question_entry = {
            "question": question,
            "answers": answers,
            "correct_answer": correct_answer
        }
        questions_data.append(question_entry)  # add to the list of questions

        # write the collected data to a text file
        with open("questions.txt", "a") as file:
            file.write(f"Question: {question}\n")
            for option, answer in answers.items():
                file.write(f"Option {option}: {answer}\n")
            file.write(f"Correct Answer: {correct_answer}\n")
            file.write("\n")  # add a newline for better readability