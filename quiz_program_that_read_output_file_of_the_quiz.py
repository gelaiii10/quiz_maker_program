import random # import module

# function that takes a filename as input
def load_questions(filename):
    questions = [] # initialize and empty list
    with open(filename, "r") as file: # open the specified file for reaing
        