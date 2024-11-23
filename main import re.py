import re
import tkinter as tk
from tkinter import messagebox

def analyze_password(password):
    # Define password strength criteria
    length = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Strength calculation
    score = sum([length, has_upper, has_lower, has_digit, has_special])
    
    # Determine password strength
    if score == 5:
        return "Strong", []
    elif score >= 3:
        suggestions = []
        if not length:
            suggestions.append("Increase password length to at least 8 characters.")
        if not has_upper:
            suggestions.append("Include at least one uppercase letter.")
        if not has_lower:
            suggestions.append("Include at least one lowercase letter.")
        if not has_digit:
            suggestions.append("Include at least one number.")
        if not has_special:
            suggestions.append("Include at least one special character.")
        return "Moderate", suggestions
    else:
        return "Weak", ["Use a longer password with uppercase, lowercase, numbers, and special characters."]

def analyze_password_gui():
    password = password_entry.get()
    strength, suggestions = analyze_password(password)
    result_label.config(text=f"Password Strength: {strength}")
    suggestions_text.delete("1.0", tk.END)
    if suggestions:
        suggestions_text.insert(tk.END, "\n".join(suggestions))

def toggle_password_visibility():
    # Toggle the 'show' attribute of the password entry
    if password_entry.cget('show') == '●':
        password_entry.config(show='')  # Make password visible
        show_password_button.config(text="Hide Password")
    else:
        password_entry.config(show='●')  # Use bullet instead of asterisk
        show_password_button.config(text="Show Password")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")

tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="●", width=30)  # Initially hide the password using bullet symbol
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Add the "Show Password" button
show_password_button = tk.Button(root, text="Show Password", command=toggle_password_visibility)
show_password_button.grid(row=0, column=2, padx=10, pady=10)

analyze_button = tk.Button(root, text="Analyze", command=analyze_password_gui)
analyze_button.grid(row=1, column=0, columnspan=3, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.grid(row=2, column=0, columnspan=3)

tk.Label(root, text="Suggestions:").grid(row=3, column=0, padx=10, pady=5)
suggestions_text = tk.Text(root, height=5, width=50)
suggestions_text.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
