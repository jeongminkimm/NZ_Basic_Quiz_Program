"""Basic quiz program about New Zealand - v3
Get the user's age
Created By Jeongmin Kim
"""


def integer_checker(question):
    """Checking for valid number for the user's age"""
    # Error prevention - the user's age is not an integer
    age = ""
    while not age:
        try:
            age = int(input(question))
        except ValueError:
            age = integer_checker("Your age must be an integer: ")
    return age


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


def age(name):
    """Component 3 - Get the user's age"""
    age = integer_checker(f"\nEnter {name}'s age: ") # Get the user's age
    # Error prevention - the user's age is a negative value
    while age < 0:
        age = integer_checker("Your age cannot be a negative value: ")
    if age >= 5 and age < 8:
        print("Quiz A")
    elif age > 7 and age < 12:
        print("Quiz B")
    else:
        print("Sorry, this quiz is only meant for children from 5 to 11 years "
              "of age") # Comment for the user who do not meet the age limit
    return age


# Main routine
name_ = welcome()
# Component 1 - Greet the user
if name_.isalpha():
    print(f"\nWelcome to the quiz about New Zealand, {name_}!")
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your answer should only be A, B, C, or D"
      "\n4. Your score will be shown at the end of the quiz")
age(name_)