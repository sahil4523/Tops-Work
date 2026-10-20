import tkinter as tk

root = tk.Tk()
root.title("Login Form")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
user = tk.Entry(root)
user.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
password = tk.Entry(root, show="*")
password.grid(row=1, column=1)

msg = tk.Label(root, text="")
msg.grid(row=3, column=0, columnspan=2)

def login():
    if user.get() != "" and password.get() != "":
        msg.config(text="Login Successful")
    else:
        msg.config(text="Please fill all fields")

tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()