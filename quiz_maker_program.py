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