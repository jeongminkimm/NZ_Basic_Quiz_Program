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
    return
        

def age(name):
    """Component 3 - Get the user's age"""
    age = integer_checker(f"\nEnter {name}'s age: ")
    while age < 5 or age > 11:
        print("Sorry, this quiz is only meant for children from 5 to 11 years "
              "of age")
        break
    while age >= 5 and age < 8:
        print("Quiz A")
    while age > 7 and age < 12:
        print("Quiz B")


# Main routine
print(welcome())
name = input("\nPlease enter your name: ")
    # Error prevention - the user can't enter invalid value
    # The user's name contains non-alphabet
if name.isalpha():
        print(f"\nWelcome to the quiz about New Zealand, {name}!")
while name != name.isalpha():
    name = input("Your name should only contain alphabetic characters: ")
    if name.isalpha():
        print(f"\nWelcome to the quiz about New Zealand, {name}!")
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your answer should only be A, B, C, or D"
      "\n4. Your score will be shown at the end of the quiz")
age(name)