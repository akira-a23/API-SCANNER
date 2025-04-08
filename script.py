import tkinter as tk
from tkinter import filedialog
import re
import os

def check_for_potential_keys(filepath, output_text):
    """Checks a file for lines that might contain API keys and displays the results in the GUI."""
    try:
        with open(filepath, 'r') as file:
            for line_number, line in enumerate(file, 1):
                # This is a simple pattern to look for: long strings of letters and numbers
                potential_key_pattern = r"[a-zA-Z0-9]{20,}"
                if re.search(potential_key_pattern, line):
                    output_text.insert(tk.END, f"Possible key found on line {line_number}: {line.strip()}\n")
    except FileNotFoundError:
        output_text.insert(tk.END, f"Error: File not found at {filepath}\n")
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {e}\n")
    output_text.insert(tk.END, "\nRemember: This tool looks for patterns and might show things that aren't actually keys. Always double-check!\n")

def browse_file(file_path_entry):
    """Opens a file dialog and updates the file path entry field."""
    filename = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)  # Clear the current text
    file_path_entry.insert(0, filename)  # Insert the selected file path

def check_file_button_click(file_path_entry, output_text):
    """Handles the button click event, gets the file path, and checks for keys."""
    filepath = file_path_entry.get()
    output_text.delete(1.0, tk.END)  # Clear previous output, keep the title
    check_for_potential_keys(filepath, output_text)

def create_gui():
    """Creates the main window and its elements."""
    window = tk.Tk()
    window.title("Potential API Key Checker")
    window.geometry("600x400")  # Increased size for better usability

    # Title Label
    title_label = tk.Label(window, text="Potential API Key Checker", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    # File Path Selection
    file_path_frame = tk.Frame(window)
    file_path_frame.pack(pady=10, fill=tk.X, padx=20)  # Use padx for horizontal margin

    file_path_label = tk.Label(file_path_frame, text="File Path:", width=8)
    file_path_label.pack(side=tk.LEFT)

    file_path_entry = tk.Entry(file_path_frame, width=40)
    file_path_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)  # Make entry expand

    browse_button = tk.Button(file_path_frame, text="Browse", command=lambda: browse_file(file_path_entry))
    browse_button.pack(side=tk.LEFT)

    # Check File Button
    check_button = tk.Button(window, text="Check File", command=lambda: check_file_button_click(file_path_entry, output_text), bg="#4CAF50", fg="white", font=("Arial", 12))  # Styled button
    check_button.pack(pady=15)

    # Output Text Area
    output_text = tk.Text(window, wrap=tk.WORD, height=10, width=70, font=("Courier New", 10))  # Fixed width and Courier New for better readability
    output_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)  # Fill both directions and expand

    # Add a title to the output box
    output_text.insert(tk.END, "Results:\n")
    output_text.config(state=tk.DISABLED) # Make it read-only by default
    output_text.config(state=tk.NORMAL) # Make it writable when adding text

    # Make the window resizable
    window.columnconfigure(0, weight=1)  # Make the main column resizable
    window.rowconfigure(3, weight=1)     # Make the text area row resizable

    return window

if __name__ == "__main__":
    window = create_gui()
    window.mainloop()
