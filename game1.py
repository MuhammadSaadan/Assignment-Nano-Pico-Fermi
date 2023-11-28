import tkinter as tk
from tkinter import messagebox
import random

# generate 3 random digit numbers between 0 - 9
def generate_numbers():
    numbers = random.sample(range(10), 3)
    return numbers

# store the function generate_numbers to secret_numbers 
secret_numbers = generate_numbers()

# store the guess counter
attempts_count = 0

# handle guess submission
def submit_guess():
    global attempts_count
    guess_str = entry.get()

    try:
        # convert the guess string to a list of integers
        guess = [int(char) for char in guess_str]

        # Check if the guess has 3 digits if not display the error
        if len(guess) != 3:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a 3-digit number.")
        return

    # evaluate the guess and hints
    attempts = evaluate_guess(guess)

    # display the hints in a messagebox
    display_hints(guess, attempts)

    # increment the attempts counter
    attempts_count += 1

    # show successful message if user guesses all Fermi
    if all(hint == "Fermi" for hint in attempts):
        messagebox.showinfo("Congratulations!", f"You guessed the correct numbers in {attempts_count} attempts.\nThe correct numbers are: {secret_numbers}")
        reset_game()

# evaluate user's guess and provide hints 
def evaluate_guess(guess):
    hints = []
    for i in range(3):
        try:
            if guess[i] == secret_numbers[i]:
                hints.append("Fermi")
            elif guess[i] in secret_numbers:
                hints.append("Pico")
            else:
                hints.append("Nano")
        except IndexError:
            hints.append("Nano")
    return hints

# display the hints in a message box 
def display_hints(guess, hints):
    hint_str = "\n".join([f"{guess[i]}. {hints[i]}" for i in range(3)])
    messagebox.showinfo("Hints", f"Hints\n{hint_str}")

# handle the window close event
def on_closing():
    result = messagebox.askquestion("Quit", "Do you want to quit the game?")
    if result == "yes":
        messagebox.showinfo("Game Over", f"Thank you for playing! You made {attempts_count} guesses.\nThe correct numbers were: {secret_numbers}")
        root.destroy()

# function to reset the game
def reset_game():
    global secret_numbers, attempts_count
    secret_numbers = generate_numbers()
    attempts_count = 0
    entry.delete(0, tk.END)

# create the main tkinter window
root = tk.Tk()
root.title("Fermi-Pico-Nano Game")
root.geometry("400x300")

# display game instructions
instructions = (
    "Welcome to the Fermi-Pico-Nano game!\n"
    "\nInstruction: \n"
    "Try to guess the 3-digit number with the least number of attempts.\n"
    "After each guess, you will receive hints:\n"
    "  - Fermi: Correct number in the correct position\n"
    "  - Pico: Correct number but in a different position\n"
    "  - Nano: Incorrect number\n"
)

instruction_label = tk.Label(root, text=instructions, justify=tk.LEFT, font=("Arial", 10))
instruction_label.pack(pady=10)

label = tk.Label(root, text="Enter your guess:", font=("Arial", 12))
label.pack()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Submit Guess", command=submit_guess, font=("Arial", 10), bg="green", fg="white")
button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
