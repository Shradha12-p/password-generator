import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number greater than 0.")

# GUI setup
root = tk.Tk()
root.title("Smart Password Generator")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Heading
tk.Label(root, text="Smart Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Entry for length
tk.Label(root, text="Enter password length:", bg="#f0f0f0", font=("Helvetica", 12)).pack()
entry = tk.Entry(root, font=("Helvetica", 12), justify='center')
entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="green")
result_label.pack(pady=5)

# Run the GUI
root.mainloop()
