from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("420x420")
window.title("CCT)
window.config(background="#e0f9ff")
window.mainloop()

             
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Chapter = StringVar()
chapter_entry = ttk.Entry(mainframe, width=7, textvariable=chapter)
chapter_entry.grid(column=2, row=1, sticky=(W, E))
