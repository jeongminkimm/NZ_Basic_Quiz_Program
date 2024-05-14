"""Basic quiz program about New Zealand - v1
Display welcome screen and get the user's name
Created By Jeongmin Kim
"""


def welcome():
    """Component 1 - Display welcome screen and get the user's name"""
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("******************** QUIZ ABOUT NEW ZEALAND ********************")
    print("********** How well do you know Aotearoa New Zealand? **********")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    name = input("\nPlease enter your name: ")
    # Error prevention - the user can't enter invalid value
    # The user's name contains non-alphabet
    if name.isalpha():
        return f"Welcome to the quiz about New Zealand, {name}!"
    while name != name.isalpha():
        name = input("Your name should only contain alphabetic characters: ")
        if name.isalpha():
            return f"Welcome to the quiz about New Zealand, {name}!"
        

# Main routine
print(welcome())