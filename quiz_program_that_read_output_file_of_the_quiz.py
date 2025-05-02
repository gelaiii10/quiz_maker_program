import random # import module

# function that takes a filename as input
def load_questions(filename):
    questions = [] # initialize and empty list
    with open(filename, "r") as file: # open the specified file for reaing
        
        # each line in the file, it splits the line into a question and answer using the semicolon as a delimeter
        for line in file:
            question, answer = line.strip().split(";")
            questions.append((question, answer))  # it appends the tuple to the list
            return questions  # close the file and returns the list of the questions
        
def quiz_user(questions): # this function takes a list of questions as input
    # randomly selects a question and its corresponding correct answer from the list
    question, correct_answer = random.choice(questions)
    print("questions: " + question)  # prints the selected questions and promts the user for their answer
    # check if the user answer matches the correct answer
    user_answer = input("your answer: ")

# condition to check if the user answer is correct or not
    if user_answer.strip().lower() == correct_answer.lower():
        print("correct!")
    else:
        print(f"incorrect! the correct answer is: {correct_answer}")

def main(): # this function is the entry point of the program
    question = load_questions("quiz_program.txt") # to get the list of the questions from the list
    quiz_user(question) # to start the quiz
