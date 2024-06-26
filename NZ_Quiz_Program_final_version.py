"""Basic quiz program about New Zealand - Final version
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
        # Error prevention - the user's age is 0
        while age == 0:
            age = integer_checker("Your age cannot be 0: ")
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
    # Constant variable for the user's age
    A_MIN_AGE = 5 # Minimum age of Quiz A
    A_MAX_AGE = 7 # Maximum age of Quiz A
    B_MIN_AGE = 8 # Minimum age of Quiz B
    B_MAX_AGE = 11 # Maximum age of Quiz B
    if age >= A_MIN_AGE and age <= A_MAX_AGE:
        quiz_a(questions_A, choices_A, answers_A) # Quiz A
    elif age >= B_MIN_AGE and age <= B_MAX_AGE:
        quiz_b (questions_B, choices_B, answers_B) # Quiz B
    else:
        print("Sorry, this quiz is only meant for children from 5 to 11 years "
              "of age") # Comment for the user who do not meet the age limit
    return age


# Set up for Quiz A
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

# List of correct answers
answers_A = ["B", "B", "C", "C", "A"]

# List of valid answers
valid_answers = ["A", "B", "C", "D"]


def quiz_a(questions_A, choices_A, answers_A):
    """Component 4 - Quiz A started"""
    score = 0 # Set up a variable for score
    # Welcome screen for Quiz A
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"Welcome to Quiz A for 5 to 7-year-olds, {name_}!"
          "\nPlease type the answer you think is correct"
          "\nLET'S GET STARTED!")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    for count in range(len(questions_A)):
        print(f"Q{count+1}: {questions_A[count]}") # Print questions
        for choice_A in choices_A[count]:
            print(choice_A) # Print choices
        # Get the user's answer
        answer = input("\nEnter your answer ('A', 'B', 'C', or 'D'): ").upper()
        # Error prevention - answers other than 'A', 'B', C', or 'D'
        while answer not in valid_answers:
            answer = input("Your answer can only be 'A', 'B', 'C', or 'D': "
                                ).upper()
        # Comment on the user's answers
        if answer == answers_A[count]:
            print("Correct!\n") # Comment for correct answers
            score += 1 # Component 6 - Increment the user's score
        # Comment for wrong answers
        else:
            print(f"Wrong. The correct answer is {answers_A[count]}\n")
    # Component 6 - Tell the user their total score and display closing screen
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"**************** Your total score is {score} out of 5 *************"
          "***")
    print("*********** Thank you for taking this quiz, goodbye! ***********")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return score


# Set up for Quiz B
# List of questions
questions_B = [
    "What is the name of the stretch of water that separates the North and "
    "South Islands?",
    "Which New Zealand city houses the Beehive?",
    "Which town has a giant carrot as a landmark?",
    "Where is 90 mile beach?",
    "When was the Treaty of Waitangi signed?"
]

# List of choices
choices_B = [
    ["A) Wellington Strait", "B) Tasman Channel", "C) Cook Strait", 
    "D) Kaikoura Strait"],
    ["A) Wellington", "B) Christchurch", "C) Paeroa", "D) Auckland"],
    ["A) Taihape", "B) Waihi", "C) Paeroa", "D) Ohakune"],
    ["A) Top of the North Island", "B) Bottom of the South Island",
     "C) Bottom of the North Island", "D) Top of the South Island"],
     ["A) 1815", "B) 1840", "C) 1855", "D) 1875"]
]

# List of correct answers
answers_B = ["C", "A", "D", "A", "B"]


def quiz_b(questions_B, choices_B, answers_B):
    """Component 5 - Quiz B started"""
    score = 0 # Set up a variable for score
    # Welcome screen for Quiz B
    print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"Welcome to Quiz B for 8 to 11-year-olds, {name_}!"
          "\nPlease type the answer you think is correct"
          "\nLET'S GET STARTED!")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
    for count in range(len(questions_B)):
        print(f"Q{count+1}: {questions_B[count]}") # Print questions
        for choice_B in choices_B[count]:
            print(choice_B) # Print choices
        # Get the user's answer
        answer = input("\nEnter your answer ('A', 'B', 'C', or 'D'): ").upper()
        # Error prevention - answers other than 'A', 'B', 'C', or 'D'
        while answer not in valid_answers:
            answer = input("Your answer can only be 'A', 'B', 'C', or 'D': "
                                ).upper()
        # Comment on the user's answers
        if answer == answers_B[count]:
            print("Correct!\n") # Comment for correct answers
            score += 1 # Component 6 - Increment the user's score
        # Comment for wrong answers
        else:
            print(f"Wrong. The correct answer is {answers_B[count]}\n")
    # Component 6 - Tell the user their total score and display closing screen
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(f"**************** Your total score is {score} out of 5 *************"
          "***")
    print("*********** Thank you for taking this quiz, goodbye! ***********")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    return score


# Main routine
count = 0
name_ = welcome()
# Component 1 - Greet the user
if name_.isalpha():
    print(f"\nWelcome to the quiz about New Zealand, {name_}!")
# Component 2 - Give the user rules/instructions for the quiz
print("\nThese are the instructions to start the quiz:"
      "\n1. This quiz consists of multiple-choice questions about New Zealand"
      "\n2. This quiz is only meant for children from 5 to 11 years of age"
      "\n3. Your score will be shown at the end of the quiz")
age(name_)