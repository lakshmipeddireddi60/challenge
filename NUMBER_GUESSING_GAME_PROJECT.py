import tkinter as tk    #for GUI purpose
from tkinter import messagebox as mb
import random

num_to_guess = random.randint(1, 100)   # generates random number b/w 1 &100
attempts = 0
max_attempts = 7

def play():
    global attempts, number_to_guess

    guess = input_values.get()   # get input from widgets

    try:
        guess = int(guess)  # checks whether it integer or not
        
    except ValueError:  # executes when non integer value entered
        mb.showwarning("Invalid Input", "Please enter a valid number!")     # shows a warning window
        input_values.delete(0, tk.END)  # clears the value inserted from the "text box" provided for input values


    attempts += 1   #attempts incremented when value inserted

    if guess < num_to_guess:
        hint.config(text="Too low! Try again.")     # changes the property-value/text based on the status of guess value
    elif guess > num_to_guess:
        hint.config(text="Too high! Try again.")    # changes the text based on the status of guess value
    else:
        mb.showinfo("You Win!", f"Correct! You guessed the number in {attempts} attempts.")     # to inform the user that he win
        restart_game()  # restarts the game

    if attempts>=max_attempts:  #if attempts are completed (reached to 7)
        mb.showerror("Game Over!", f"Your 7 attempts were Completed.\n\nThe number was {num_to_guess}.")    # shows error window that we loss the game
        restart_game()  # restarts the game
        #return
    input_values.delete(0, tk.END)  # clears the value inserted from the text feild

def restart_game():     #resets the game

    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)    # generates random number b/w 1 &100
  
    attempts = 0
    
    input_values.delete(0, tk.END)  # clears the value inserted from the text feild
    hint.config(text="Hint:")   #changes the text to Hint: from the status of guess 

def exit_game():
    window.destroy()    # exit from the game

# GUI setup
window = tk.Tk()    # main window created

window.title("Game Time")   # title given to the main window

window.geometry("700x400")   #given width &height to the main window

window.config(bg="light pink")  #changes th window properties after it has created

# displays the text
game_name=tk.Label(window, text="Number Guessing Game (1-100)",font=("Times New Roman",35),bg="light pink",fg="blue")
game_name.pack(pady=10)

# Frame1: parent for text & text box
input_frame=tk.Frame(window,bg="light pink")
input_frame.pack(pady=5)

# displays the text
input_feild=tk.Label(input_frame, text="Enter your guess:", font=("Times New Roman", 30),bg="light pink",fg="blue")
input_feild.pack(side="left")

#creates text box & get the guess value into it
input_values = tk.Entry(input_frame,font=("Times New Roman",25))
input_values.pack(pady=5,side="right")

#submit Button
submit_button=tk.Button(window, text="Submit", font=("Times New Roman",20),command=play,bg="green",fg="white")
submit_button.pack(pady=5)

#Display Hint in Text
hint= tk.Label(window, text="Hint:", font=("Times New Roman", 15),bg="purple",fg="yellow")
hint.pack(pady=15)

# Frame2: parent for submit & exit buttons
button_frame=tk.Frame(window,bg="light pink")
button_frame.pack(pady=10,padx=20)

#Restart Game
restart=tk.Button(button_frame, text="Restart Game",  font=("Times New Roman",20),command=restart_game,bg="blue",fg="white")
restart.pack(pady=1,padx=25,side="left")

#Exit Button
exit_button=tk.Button(button_frame, text="Exit Game",  font=("Times New Roman",20),command=exit_game,bg="red",fg="white")
exit_button.pack(pady=1,padx=25,side="right")

# to run the tkinter code
window.mainloop()
