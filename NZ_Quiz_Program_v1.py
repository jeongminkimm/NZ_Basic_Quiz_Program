"""Basic quiz program about New Zealand - v1
Display welcome screen and get the user's name and greet them
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