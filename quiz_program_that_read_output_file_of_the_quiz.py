import random


def load_questions(filename):                                       # this function takes a filename as input
    questions = []                                                  # initializes an empty list
    with open(filename, 'r') as file:                               # opens the specified file for reading
        # each line in the file, it splits the line into a question and an answer using the semicolon as a delimiter
        for line in file:  
            question, answer = line.strip().split(';')
            questions.append((question, answer))                    # it appends the tuple (question, answer) to the list
    return questions                                                # it closes the file and returns the list of questions


def quiz_user(questions):                                           # this function takes a list of questions as input
    # randomly selects a question and its corresponding correct answer from the list
    question, correct_answer = random.choice(questions)
    print("question: " + question)                                  # prints the selected question and prompts the user for their answer
    user_answer = input("your answer: ")                            # checks if the user's answer matches the correct answer


    if user_answer.strip().lower() == correct_answer.lower():
        print("correct!")                                           # it prints "Correct!" if the answer is right
    else:
        print(f"incorrect! The correct answer is: {correct_answer}")    # otherwise, it prints the correct answer


def main():                                                         # this function is the entry point of the program
    questions = load_questions('quiz_program.txt')                  # to get the list of questions from the file
    quiz_user(questions)                                            # to start the quiz


if __name__ == "__main__":                                          # checks whether the script is being executed directly or imported
        main()
