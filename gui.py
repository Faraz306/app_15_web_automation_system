import tkinter as tk
from main import WebAutomation
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Yamaan Faraz's Web Automation system.")
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, sticky="w")
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w")

        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full name:").grid(row=0, column=0, sticky="w")
        self.fullname_entry = tk.Entry(self.form_frame)
        self.fullname_entry.grid(row=0, column=1, sticky="w")
        tk.Label(self.form_frame, text="Email:").grid(row=1, column=0, sticky="w")
        self.Email_entry = tk.Entry(self.form_frame)
        self.Email_entry.grid(row=1, column=1, sticky="w")
        tk.Label(self.form_frame, text="Current Address:").grid(row=2, column=0, sticky="w")
        self.current_address_entry = tk.Entry(self.form_frame)
        self.current_address_entry.grid(row=2, column=1, sticky="w")
        tk.Label(self.form_frame, text="Permanent Address:").grid(row=3, column=0, sticky="w")
        self.permanent_address_entry = tk.Entry(self.form_frame)
        self.permanent_address_entry.grid(row=3, column=1, sticky="w")

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)
        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, sticky="w", padx=5)
        tk.Button(self.button_frame, text="Close browser", command=self.close).grid(row=0, column=1, sticky="ew", padx=5)

    def submit_data(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        fullname = self.fullname_entry.get()
        email = self.Email_entry.get()
        current_address = self.current_address_entry.get()
        permanent_address = self.permanent_address_entry.get()
        self.automate_web = WebAutomation()
        self.automate_web.login(username, password)
        self.automate_web.text_box(fullname, email, current_address, permanent_address)
    def close(self):
        self.root.destroy()
        tk.messagebox.showinfo("Success !", "Successfully closed the browser :)")



root = tk.Tk()
app = App(root)
root.mainloop()
