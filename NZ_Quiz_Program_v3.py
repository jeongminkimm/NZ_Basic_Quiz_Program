"""Basic quiz program about New Zealand - v3
Get the user's age
Created By Jeongmin Kim
"""


def integer_checker(question):
    """Checking for valid number for the user's age"""
    age = ""
    while not age:
        try:
            age = int(input(question))
        except ValueError:
            print("Your age must be an integer")
    return age


def welcome():
    """Component 1 - Display welcome screen and get the user's name and greet
    them"""
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("******************** QUIZ ABOUT NEW ZEALAND ********************")
    print("********** How well do you know Aotearoa New Zealand? **********")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    name = input("\nPlease enter your name: ")
    # Error prevention - the user can't enter invalid value
    # The user's name contains non-alphabet
    while not name.isalpha():
        name = input("Your name should only contain alphabetic characters: ")
    return name


def age(name):
    """Component 3 - Get the user's age"""
    age = integer_checker(f"\nEnter {name}'s age: ")
    if age >= 5 and age < 8:
        print("Quiz A")
    elif age > 7 and age < 12:
        print("Quiz B")
    else:
        print("Sorry, this quiz is only meant for children from 5 to 11 years "
              "of age")


# Main routine
name_ = welcome()
print(name_)
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your answer should only be A, B, C, or D"
      "\n4. Your score will be shown at the end of the quiz")
age(name_)