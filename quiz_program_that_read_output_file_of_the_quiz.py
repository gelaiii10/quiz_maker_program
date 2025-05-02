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
