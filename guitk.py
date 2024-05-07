import tkinter as tk
from tkinter import messagebox
import subprocess

def run_translation():
    try:
        print("Executing translation script...")
        subprocess.run(["python", "test.py"])  # Replace "test.py" with your Python file name
        print("Translation script executed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        print(f"Error occurred: {str(e)}")

root = tk.Tk()
root.title("Sign Language Translator")
root.attributes('-fullscreen', True)
# Function to translate sign language
def translate_sign_language():
    # Your code to translate sign language goes here
    print("Translating sign language...")
    run_translation()

# Styling
root.geometry("400x200")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Click to Translate Sign Language", font=("Helvetica", 18), bg="#f0f0f0")
title_label.pack(pady=10)

# Button
translate_button = tk.Button(root, text="Translate", command=translate_sign_language, bg="#4CAF50", fg="white", font=("Helvetica", 14))
translate_button.pack(pady=10)

root.mainloop()
