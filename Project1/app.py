import tkinter as tk
from tkinter import ttk #set of themable widgets

def greet():
    print("Hello, World!")

root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="both", expand=True) # algoritm Pack that embeds the widget

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left")
root.mainloop()