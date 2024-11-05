#importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import random
import re

# Download resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

#updating intents
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hello! Ready to learn some Python?", "Hi there! What do you want to learn about Python today?"]
    },
    "python_variables": {
        "patterns": ["What are variables?", "Explain variables in Python", "What is a variable?"],
        "responses": ["Variables are used to store data values. For example, `x = 5` assigns the value 5 to the variable x."]
    },
      "python_data_types": {
        "patterns": ["What are data types?", "Explain data types in Python", "What is a data type?"],
        "responses": ["Each variable has a data type that determines the kind of data it can store, such as integers (whole numbers), floats (decimal numbers), strings (text), and Booleans (true/false values)"]
    },
    "python_loops": {
        "patterns": ["What are loops?", "Explain loops in Python", "What is a loop?"],
        "responses": ["Loops are used to repeat a block of code multiple times. There are two main types of loops: `for` loops and `while` loops."]
    },
    "python_functions": {
        "patterns": ["What are functions?", "Explain functions in Python", "What is a function?"],
        "responses": ["Functions are blocks of reusable code that perform a specific task. You can define a function using the `def` keyword."]
    },
    "python_operators": {
        "patterns": ["What are operators?", "Explain operators in Python", "What is an operator?"],
        "responses": ["Operators are symbols used to perform operations on variables and values. Common operators include arithmetic operators (+, -, *, /), comparison operators (==, !=, <, >), and logical operators (and, or, not). "]
    },
    "python_print": {
        "patterns": ["What is print?", "Explain print in Python", "Tell me about print()"],
        "responses": ["The print() function prints the specified message to the screen or other standard devices."]
    },
    "python_inputoutput": {
        "patterns": ["What is input and output?", "Explain input output in Python", "Tell me about input and output"],
        "responses": ["Input is data that is provided to a program, while output is the result produced by the program. Input can come from sources like the keyboard, mouse, or files, while output can be displayed on the screen, saved to a file, or sent to other devices"]
    },
    "python_conditional": {
        "patterns": ["What is conditional statements?", "Explain conditional statements in Python", "Tell me about conditional statements"],
        "responses": ["Conditional statements allow our programs to make decisions based on certain conditions. They use keywords like `if`, `else if`, and `else`."]
    },
    "python_syntaxerror": {
        "patterns": ["What is syntax error?", "Explain syntax error in Python", "Tell me about syntax error"],
        "responses": ["Syntax errors occur when the rules of the programming language are not followed correctly. These errors are indicated by error messages and must be fixed before the program can run. "]
    },
    "python_comments": {
        "patterns": ["What is a comment?", "Explain comments in Python", "Tell me about comments"],
        "responses": ["Comments are notes that we can add to our code to explain what it does. Comments are not executed by the computer and are only for humans to read."]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "exit", "quit"],
        "responses": ["Goodbye! Happy learning!"]
    }
}


#adding quiz
quizzes = {
    "quiz1": {
        "question": "What is the output of print(2 + 2)?",
        "options": ["2", "4", "22"],
        "answer": "4"
    },
    "quiz2": {
        "question": "What keyword is used to define a function in Python?",
        "options": ["function", "def", "define"],
        "answer": "def"
    },
    "quiz3": {
       "question": "What type of loop iterates over a sequence (like a list or string)?",
        "options": ["while loop", "for loop", "do while loop"],
        "answer": "for loop"
    },
    "quiz4": {
   "question": "What keyword is used to create a conditional statement in Python?",
        "options": ["if", "when", "condition"],
        "answer": "if"
    },
    "quiz5": {
    "question": "What will the following code print? print('Hello, World!')",
        "options": ["Hello, World!", "Hello World", "Hello"],
        "answer": "Hello, World!"
    },
    "quiz6": {
  "question": "How do you read user input in Python?",
        "options": ["input()", "get()", "read()"],
        "answer": "input()"
    },
    "quiz7": {
      "question": "What symbol is used for comments in Python?",
        "options": ["//", "#", "--"],
        "answer": "#"
    },
    "quiz8": {
         "question": "Which operator is used for addition in Python?",
        "options": ["+", "-", "*"],
        "answer": "+"
    },
       "quiz9": {
        "question": "What is the output of the expression 100 > 5?",
        "options": ["True", "False", "Error"],
        "answer": "True"
    },
       "quiz10": {
        "question": "What does the operator '==' mean?",
        "options": ["Equal", "Assign", "Error"],
        "answer": "Equal"
    }
}

#preprocessing text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Tokenize text
    words = word_tokenize(text)
    # Remove punctuation and stop words
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return words

# print("PythonBot intents loaded:", intents)

# print("Processed text:", preprocess_text("Hello! How are you doing today?"))


#adding response function
def get_response(user_input):
    # Preprocess the user input
    processed_input = preprocess_text(user_input)

    # Match the processed input with intents
    for intent, data in intents.items():
        for pattern in data['patterns']:
            if any(word in pattern for word in processed_input):
                return random.choice(data['responses'])

    # Return a generic error message if no intent matches
    return "I'm sorry, I didn't understand that. Could you please ask something else?"


#quizz function
def get_quiz_response(quiz_key, user_answer):
    correct_answer = quizzes[quiz_key]['answer']
    if user_answer == correct_answer:
        return "Correct! Well done!"
    else:
        return "That's not right. Try again!"


#user input is yes/no
def handle_yes_no_response(user_input):
    """Handle yes or no responses."""
    user_input = user_input.lower()
    if user_input in ['yes', 'y']:
        return "Great! Let's get started! You can ask question about Python or play a game of quiz!"
    elif user_input in ['no', 'n']:
        return "No worries! Feel free to ask whenever you're ready."
    else:
        return "I didn't understand that. Please answer with yes or no."


#interaction loop
def main():
    print("Welcome to the Python Learning ChatPython! Type 'bye' to exit.")
    
    # Ask if the user is ready to learn
    while True:
        user_input = input("ChatPython: Are you ready to learn some Python? (yes/no) ")
        
        # Error handling for yes/no response
        if user_input.lower() not in ['yes', 'no']:
            print("ChatPython: Please answer with 'yes' or 'no'.")
            continue  # Ask the question again

        response = handle_yes_no_response(user_input)
        print("ChatPython:", response)

        if "Great! Let's get started!" in response:
            break  # Exit the loop if the user is ready
        elif "Okay! Let me know when you are ready!" in response:
            print("ChatPython: Whenever you're ready, just let me know!")
            return  # Exit the main function if the user is not ready
    
    # If user is ready, enter the main loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print("ChatPython: Goodbye! Happy learning!")
            break
        elif "quiz" in user_input.lower():
            while True:  # Starting a loop for quizzes
                quiz_key = random.choice(list(quizzes.keys()))
                print("ChatPython:", quizzes[quiz_key]['question'])
                print("Options:", ", ".join(quizzes[quiz_key]['options']))
                
                user_answer = input("Your answer: ")
                print("ChatPython:", get_quiz_response(quiz_key, user_answer))
                
                continue_quiz = input("Do you want to continue the quiz? (yes/no): ")
                if continue_quiz.lower() not in ['yes', 'y']:
                    print("ChatPython: Okay, let's move on. Type 'quiz' to start again or 'bye' to exit. You can try asking questions about basics of Python also!")
                    break  # Exit the quiz loop
        else:
            response = get_response(user_input)
            print("ChatPython:", response)

if __name__ == "__main__":
    main()


# print("PythonBot response to 'What is a variable?':", get_response("What is a variable?"))
# print("PythonBot response to 'Tell me about loops':", get_response("Tell me about loops"))
# print("PythonBot response to 'Explain functions in Python':", get_response("Explain functions in Python"))
