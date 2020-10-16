import tkinter as tk
from tkinter import ttk #set of themable widgets

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

root = tk.Tk() # main window declaration
root.title("Greeter")

root.columnconfigure(0, weight=1)

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20,10,20,0)) #padding (left, top, right, bottom)
input_frame.grid(row=0, column=0, sticky="EW")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0, padx=(0,10))

name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

buttons = ttk.Frame(root, padding=(20,10)) # padding (lef/right, top/bottom)
buttons.grid(row=1, column=0, sticky="EW")

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW") # algoritm Pack that embeds the widget

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW") # fill value can be x,y or both

root.mainloop() #main window initialization