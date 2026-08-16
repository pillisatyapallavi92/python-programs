import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()
window.title("Python Quiz App")
window.geometry("400x300")

# Question label
question_label = tk.Label(window, text="In which year was Python introduced?", font=("Arial", 14), wraplength=350, justify="center")
question_label.pack(pady=20)

# Store correct answer
correct_answer = "B"

# Function to check answer
def check_answer(selected_option):
    if selected_option == correct_answer:
        messagebox.showinfo("Result", " Correct! Python was introduced in 1991.")
    else:
        messagebox.showerror("Result", " Wrong! The correct answer is 1991.")
    window.destroy()  # close after answering (optional)

# Options (Multiple Choice Buttons)
button_a = tk.Button(window, text="A. 1989", width=20, command=lambda: check_answer("A"))
button_a.pack(pady=5)

button_b = tk.Button(window, text="B. 1991", width=20, command=lambda: check_answer("B"))
button_b.pack(pady=5)

button_c = tk.Button(window, text="C. 1995", width=20, command=lambda: check_answer("C"))
button_c.pack(pady=5)

button_d = tk.Button(window, text="D. 2000", width=20, command=lambda: check_answer("D"))
button_d.pack(pady=5)

# Run the GUI
window.mainloop()


