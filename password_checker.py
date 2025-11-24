import tkinter as tk
from tkinter import messagebox
import re

class PasswordCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker By ATAMA")
        self.root.geometry("450x380")
        self.root.configure(bg="#0A1A2F")  # Dark blue background
        self.root.resizable(True, True)

        # State for password visibility
        self.password_visible = False

        # Title
        tk.Label(
            root,
            text="Password Strength Checker",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#0A1A2F"
        ).pack(pady=15)

        # Input Label
        tk.Label(
            root,
            text="Enter Password:",
            font=("Arial", 12),
            fg="white",
            bg="#0A1A2F"
        ).pack()

        # Entry frame to hold entry + eye button
        entry_frame = tk.Frame(root, bg="#0A1A2F")
        entry_frame.pack(pady=5)

        # Password Entry
        self.password_entry = tk.Entry(
            entry_frame, width=36, show="*",
            font=("Arial", 12),
            bg="white"
        )
        self.password_entry.grid(row=0, column=0)

        # Eye toggle button
        self.eye_button = tk.Button(
            entry_frame,
            text="👁",  # eye icon
            font=("Arial", 10),
            width=3,
            command=self.toggle_password_visibility
        )
        self.eye_button.grid(row=0, column=1, padx=5)

        # Check strength button
        tk.Button(
            root,
            text="Check Strength",
            width=20,
            command=self.check_strength
        ).pack(pady=10)

        # Output Result
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#0A1A2F"
        )
        self.result_label.pack(pady=10)

        # Details Box
        self.details_box = tk.Text(
            root,
            height=7,
            width=50,
            wrap="word",
            state="disabled",
            bg="white"
        )
        self.details_box.pack(pady=10)

    def toggle_password_visibility(self):
        """Toggles the visibility of the password field."""
        if self.password_visible:
            self.password_entry.config(show="*")
            self.eye_button.config(text="👁")  # Show eye icon
            self.password_visible = False
        else:
            self.password_entry.config(show="")
            self.eye_button.config(text="🚫")  # Hide icon
            self.password_visible = True

    def check_strength(self):
        password = self.password_entry.get().strip()

        if not password:
            messagebox.showerror("Error", "Password field cannot be empty!")
            return

        # Criteria checks
        length = len(password) >= 8
        lower = re.search(r"[a-z]", password)
        upper = re.search(r"[A-Z]", password)
        digit = re.search(r"[0-9]", password)
        special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

        score = sum([length, bool(lower), bool(upper), bool(digit), bool(special)])

        # Strength levels
        if score <= 2:
            strength = "Weak"
            color = "red"
        elif score in [3, 4]:
            strength = "Medium"
            color = "orange"
        else:
            strength = "Strong"
            color = "green"

        # Update label
        self.result_label.config(
            text=f"Password Strength: {strength}",
            fg=color
        )

        # Detailed feedback
        details = (
            f"Length (8+): {'✔️' if length else '❌'}\n"
            f"Lowercase Letter: {'✔️' if lower else '❌'}\n"
            f"Uppercase Letter: {'✔️' if upper else '❌'}\n"
            f"Number: {'✔️' if digit else '❌'}\n"
            f"Special Character: {'✔️' if special else '❌'}"
        )

        # Display feedback box
        self.details_box.config(state="normal")
        self.details_box.delete("1.0", "end")
        self.details_box.insert("end", details)
        self.details_box.config(state="disabled")


# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    PasswordCheckerGUI(root)
    root.mainloop()