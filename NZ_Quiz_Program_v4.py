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
        quiz_a(questions_A, choices_A, answers_A)
    elif age > 7 and age < 12:
        print("Quiz B")
    else:
        print("Sorry, this quiz is only meant for children from 5 to 11 years "
              "of age")
    return age


# Component 4 - Quiz A started
# List of questions
questions_A = [
    "What is the capital of New Zealand?",
    "Which city is known as 'The Garden City'?",
    "Where did L&P soda originally come from?",
    "In what month is Matariki celebrated?",
    "What colour is Kakariki?"
]

# List of choices
choices_A = [
    ["A) Auckland", "B) Wellington", "C) Christchurch", "D) Hamilton"],
    ["A) Wellington", "B) Christchurch", "C) Paeroa", "D) Auckland"],
    ["A) Putaruru", "B) Waihi", "C) Paeroa", "D) Auckland"],
    ["A) April", "B) May", "C) May, June, or July", "D) July"],
    ["A) Green", "B) Blue", "C) Black", "D) Grey"]
]

# List of answers
answers_A = ["B", "B", "C", "C", "A"]

# List of valid answers
valid_answers = ["A", "B", "C", "D"]

def quiz_a(questions_A, choices_A, answers_A):
    score = 0
    print("\nWelcome to Quiz A for 5 to 7-year-olds"
          "\nPlease type the answer you think is correct"
          "\nLET'S GET STARTED!\n")
    count = 0
    for count in range(len(questions_A)):
        print(f"Q{count+1}: {questions_A[count]}") # Print questions
        for choice_A in choices_A[count]: # Print choices
            print(choice_A)
        # Get the user's answer
        answer = input("\nEnter your answer ('A', 'B', 'C', or 'D'): ").upper()

        if answer == answers_A[count]:
            print("Correct!\n")
            score += 1
        while answer not in valid_answers:
            answer = input("Your answer can only be 'A', 'B', 'C', or 'D': "
                            ).upper()
            if answer == answers_A[count]:
                print("Correct!\n")
                score += 1
        else:
            print(f"Wrong. The correct answer is {answers_A[count]}\n")
    return score


# Main routine
name_ = welcome()
if name_.isalpha():
    print(f"\nWelcome to the quiz about New Zealand, {name_}!")
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your score will be shown at the end of the quiz")
age(name_)