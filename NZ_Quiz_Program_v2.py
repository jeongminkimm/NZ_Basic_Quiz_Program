"""Basic quiz program about New Zealand - v2
Give the user rules/instructions for the quiz
Created By Jeongmin Kim
"""


def welcome():
    """Component 1 - Display welcome screen and get the user's name"""
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("******************** QUIZ ABOUT NEW ZEALAND ********************")
    print("********** How well do you know Aotearoa New Zealand? **********")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    name = input("\nPlease enter your name: ") # Get the user's name
    # Error prevention - the user's name contains non-alphabet
    while not name.isalpha():
        name = input("Your name should only contain alphabetic characters: ")
    return name


# Main routine
name_ = welcome()
# Component 1 - Greet the user
if name_.isalpha():
    print(f"\nWelcome to the quiz about New Zealand, {name_}!")
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your score will be shown at the end of the quiz")