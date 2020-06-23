import tkinter as tk
from tkinter import ttk #set of themable widgets

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk() # main window declaration
root.title("Greeter")

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20,10,20,0)) #padding (left, top, right, bottom)
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

buttons = ttk.Frame(root, padding=(20,10)) # padding (lef/right, top/bottom)
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True) # algoritm Pack that embeds the widget

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True) # fill value can be x,y or both

root.mainloop() #main window initialization