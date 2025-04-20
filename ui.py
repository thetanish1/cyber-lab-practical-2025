import tkinter as tk
from tkinter import messagebox

# Import your practicals (ensure your practical scripts are named as 'practical_1.py', 'practical_2.py', etc.)
from practical_1 import run_practical_1
from practical_2 import run_practical_2
from practical_3 import run_practical_3
from practical_4 import run_practical_4
from practical_5 import run_practical_5
from practical_6 import run_practical_6
from practical_7 import run_practical_7
from practical_8 import run_practical_8
from practical_9 import run_practical_9
from practical_10 import run_practical_10

def run_practical(practical_number, status_label, output_text, input_text=None):
    try:
        status_label.config(text=f"Running Practical {practical_number}...")  # Update the status label

        # Handle user input for practicals requiring input
        if practical_number == 1:
            output = run_practical_1(input_text) if input_text else run_practical_1()
        elif practical_number == 2:
            output = run_practical_2(input_text) if input_text else run_practical_2()
        elif practical_number == 3:
            output = run_practical_3(input_text) if input_text else run_practical_3()
        elif practical_number == 4:
            output = run_practical_4(input_text) if input_text else run_practical_4()
        elif practical_number == 5:
            output = run_practical_5(input_text) if input_text else run_practical_5()
        elif practical_number == 6:
            output = run_practical_6(input_text) if input_text else run_practical_6()
        elif practical_number == 7:
            output = run_practical_7(input_text) if input_text else run_practical_7()
        elif practical_number == 8:
            output = run_practical_8(input_text) if input_text else run_practical_8()
        elif practical_number == 9:
            output = run_practical_9(input_text) if input_text else run_practical_9()
        elif practical_number == 10:
            output = run_practical_10(input_text) if input_text else run_practical_10()
        else:
            messagebox.showerror("Error", "Invalid practical number")
            return

        # Display output in the text box
        output_text.config(state=tk.NORMAL)  # Enable editing
        output_text.delete(1.0, tk.END)  # Clear existing text
        output_text.insert(tk.END, output)  # Insert the new output
        output_text.config(state=tk.DISABLED)  # Disable editing
        status_label.config(text=f"Practical {practical_number} completed!")  # Update status after completion

    except Exception as e:
        status_label.config(text="Error occurred!")  # Update status if error occurs
        messagebox.showerror("Error", str(e))

def run_all_practicals(status_label, output_text, input_text=None):
    for i in range(1, 11):  # Loop through all 10 practicals
        run_practical(i, status_label, output_text, input_text)  # Run each practical one by one
        status_label.config(text=f"Practical {i} completed!")  # Update status after each practical
        output_text.update_idletasks()  # Update the GUI to reflect the output instantly

def create_gui():
    root = tk.Tk()
    root.title("Cyber Lab Practicals")

    # Set the window size
    root.geometry("400x600")  # Increased height for 10 buttons

    # Create a status label that will show which practical is running
    status_label = tk.Label(root, text="Select a practical to run", font=("Arial", 12))
    status_label.pack(pady=20)

    # Create a text box to show output of the practical
    output_text = tk.Text(root, height=10, width=40, wrap=tk.WORD, state=tk.DISABLED)
    output_text.pack(pady=10)

    # Create a text box for user input (for practicals that require input)
    input_label = tk.Label(root, text="Enter Input (if required)", font=("Arial", 10))
    input_label.pack(pady=5)

    input_text = tk.Entry(root, width=40)
    input_text.pack(pady=5)

    def run_practical_button(practical_number):
        # If the practical requires input, pass the value of input_text
        user_input = input_text.get() if input_text.get() else None
        run_practical(practical_number, status_label, output_text, user_input)

    def submit_all_practicals():
        # If the user wants to run all practicals, get input and run sequentially
        user_input = input_text.get() if input_text.get() else None
        run_all_practicals(status_label, output_text, user_input)

    # Add buttons for each practical
    button_1 = tk.Button(root, text="Run Practical 1", command=lambda: run_practical_button(1))
    button_1.pack(pady=5)

    button_2 = tk.Button(root, text="Run Practical 2", command=lambda: run_practical_button(2))
    button_2.pack(pady=5)

    button_3 = tk.Button(root, text="Run Practical 3", command=lambda: run_practical_button(3))
    button_3.pack(pady=5)

    button_4 = tk.Button(root, text="Run Practical 4", command=lambda: run_practical_button(4))
    button_4.pack(pady=5)

    button_5 = tk.Button(root, text="Run Practical 5", command=lambda: run_practical_button(5))
    button_5.pack(pady=5)

    button_6 = tk.Button(root, text="Run Practical 6", command=lambda: run_practical_button(6))
    button_6.pack(pady=5)

    button_7 = tk.Button(root, text="Run Practical 7", command=lambda: run_practical_button(7))
    button_7.pack(pady=5)

    button_8 = tk.Button(root, text="Run Practical 8", command=lambda: run_practical_button(8))
    button_8.pack(pady=5)

    button_9 = tk.Button(root, text="Run Practical 9", command=lambda: run_practical_button(9))
    button_9.pack(pady=5)

    button_10 = tk.Button(root, text="Run Practical 10", command=lambda: run_practical_button(10))
    button_10.pack(pady=5)

    # Add Submit button to run all practicals
    submit_button = tk.Button(root, text="Submit All Practicals", command=submit_all_practicals)
    submit_button.pack(pady=20)

    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    create_gui()
