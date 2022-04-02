'''
Docs for Tkinter module: https://docs.python.org/3/library/tk.html
'''
import tkinter as tk

window = tk.Tk()

window.title("Tkinter Template")
window.geometry('500x500')

usernameLabel = tk.Label(text="Username", background="yellow", foreground="black")
usernameLabel.pack()
username = tk.Entry()
username.pack()

passwordLabel = tk.Label(text="Password", background="yellow", foreground="black")
passwordLabel.pack()
password = tk.Entry()
password.pack()

window.mainloop()