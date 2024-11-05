import tkinter as tk
import random
from chatbot import handle_yes_no_response, get_quiz_response, get_response, quizzes  

#Initializing global variables
current_quiz_key = None
awaiting_command = False
awaiting_yes_no = True  #asking if the user is ready

#main application window
root = tk.Tk()
root.title("Python Learning ChatPython")
root.geometry("400x500")

#chat history area
chat_history = tk.Text(root, state=tk.DISABLED, wrap=tk.WORD)
chat_history.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

#entry widget for user input
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=10, padx=10)

def handle_input():
    global current_quiz_key, awaiting_command, awaiting_yes_no
    user_input = user_entry.get().strip()

    if user_input:  #If the user input is not empty
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, "You: " + user_input + "\n")
        
        if awaiting_yes_no:
            #yes/no response to the question
            response = handle_yes_no_response(user_input)
            chat_history.insert(tk.END, "ChatPython: " + response + "\n\n")
            
            if "Great! Let's get started!" in response:
                awaiting_yes_no = False  #main interaction loop 
                chat_history.insert(tk.END, "ChatPython: Type 'quiz' to start a quiz or ask any Python question!\n\n")
            elif "Okay! Let me know when you are ready!" in response:
                chat_history.insert(tk.END, "ChatPython: Whenever you're ready, just let me know!\n\n")
                user_entry.delete(0, tk.END)  #Clear input
                chat_history.config(state=tk.DISABLED)
                return  #exiting handle_input to wait for new input

        elif "quiz" in user_input.lower() and current_quiz_key is None:
            #Starting a quiz
            current_quiz_key = random.choice(list(quizzes.keys()))
            quiz_question = quizzes[current_quiz_key]['question']
            quiz_options = ", ".join(quizzes[current_quiz_key]['options'])
            chat_history.insert(tk.END, f"ChatPython: {quiz_question}\nOptions: {quiz_options}\n\n")
        
        elif current_quiz_key:
            #Handling quiz answer
            quiz_response = get_quiz_response(current_quiz_key, user_input)
            chat_history.insert(tk.END, "ChatPython: " + quiz_response + "\n\n")
            
            #ask if they want to continue or ask something else
            chat_history.insert(tk.END, "ChatPython: Do you want to continue the quiz, ask a question, or quit? (type 'continue', 'question', or 'quit')\n")
            awaiting_command = True  
            current_quiz_key = None  
            
        elif awaiting_command:
            if user_input.lower() in ['continue']:
                current_quiz_key = random.choice(list(quizzes.keys()))
                quiz_question = quizzes[current_quiz_key]['question']
                quiz_options = ", ".join(quizzes[current_quiz_key]['options'])
                chat_history.insert(tk.END, f"ChatPython: {quiz_question}\nOptions: {quiz_options}\n\n")
                awaiting_command = False 
            elif user_input.lower() in ['question', 'ask']:
                current_quiz_key = None  
                chat_history.insert(tk.END, "ChatPython: You can ask questions about Python!\n\n")
                awaiting_command = False  
            elif user_input.lower() in ['quit', 'exit']:
                chat_history.insert(tk.END, "ChatPython: Goodbye! Happy learning!\n\n")
                root.quit()  
            else:
                chat_history.insert(tk.END, "ChatPython: I didn't understand that. Please type 'continue', 'question', or 'quit'.\n")
        
        else:
            response = get_response(user_input)
            chat_history.insert(tk.END, "ChatPython: " + response + "\n\n")
        
        user_entry.delete(0, tk.END)  
    chat_history.yview(tk.END)  
    chat_history.config(state=tk.DISABLED)  


user_entry.bind("<Return>", lambda event: handle_input())

#Welcome message
chat_history.config(state=tk.NORMAL)
chat_history.insert(tk.END, "Welcome to the Python Learning ChatPython! Type 'bye' to exit.\n")
chat_history.insert(tk.END, "ChatPython: Are you ready to learn some Python? (yes/no)\n")
chat_history.config(state=tk.DISABLED)

#Tkinter main loop
root.mainloop()
