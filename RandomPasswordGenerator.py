import random
import string
import tkinter as tk
from tkinter import Checkbutton, Entry, Label, StringVar, IntVar, Button, messagebox

def generate_password():
    length = length_var.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += '!@#$%^&*()'

    if length < 1:
        messagebox.showerror("Cannot Generate Password", " The Password length must be at least 1.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Create a Tkinter window
window = tk.Tk()
window.geometry('280x300')
window.resizable(0,0)
window.title("Random Password Generator")

# Variables to store user choices
length_var = IntVar()
uppercase_var = IntVar()
lowercase_var = IntVar()
digits_var = IntVar()
special_chars_var = IntVar()
result_var = StringVar()

# Create GUI elements
Label(window, text="Enter Password Length:").pack()
Entry(window, textvariable=length_var).pack()
Checkbutton(window, text="Include Uppercase", variable=uppercase_var).pack()
Checkbutton(window, text="Include Lowercase", variable=lowercase_var).pack()
Checkbutton(window, text="Include Digits", variable=digits_var).pack()
Checkbutton(window, text="Include Special Characters", variable=special_chars_var).pack()
Button(window, text="Generate Password", command=generate_password).pack()
Label(window, text="Generated Password:").pack()
Entry(window, textvariable=result_var, state='readonly').pack()

# Start the GUI main loop
window.mainloop()
