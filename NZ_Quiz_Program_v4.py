"""Basic quiz program about New Zealand - v4
Quiz started (Show questions)
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
        quiz_a()
    elif age > 7 and age < 12:
        print("Quiz B")
    else:
        print("Sorry, this quiz is only meant for children from 5 to 11 years "
              "of age")
    return age


def quiz_a():
    """ Component 4 - Quiz A Started"""
    count = 0
    print("\nWelcome to Quiz A for 5 to 7-year-olds"
          "\nPlease type the answer you think is correct"
          "\nLET'S GET STARTED!")
    print({Quiz_A_questions})

    Quiz_A_questions = [
        "1. What is the capital of New Zealand?\nA. Auckland\nB. Wellington"
        "\nC. Christchurch\nD. Hamilton",
        "2. Which city is known as 'The Garden City'?\nA. Wellington"
        "\nB. Christchurch\nC. Paeroa\nD. Auckland",
        "3. Where did L&P soda originally come from?\nA. Putaruru"
        "\nB. Waihi\nC. Paeroa\nD. Auckland",
        "4. In what month is Matariki celebrated?\nA. April\nB. May"
        "\nC. May, June, or July\nD. July",
        "5. What colour is Kakariki?\nA. Green\nB. Blue\nC. Black\nD.Grey"
    ]


# Main routine
name_ = welcome()
if name_.isalpha():
    print(f"\nWelcome to the quiz about New Zealand, {name_}!")
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your answer should only be A, B, C, or D"
      "\n4. Your score will be shown at the end of the quiz")
age(name_)
quiz_a