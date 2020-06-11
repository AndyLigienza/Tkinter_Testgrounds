import tkinter as tk
from tkinter import ttk #set of themable widgets

root = tk.Tk()
ttk.Label(root, text="Hello, World!", padding = (30, 10)).pack()

root.mainloop()