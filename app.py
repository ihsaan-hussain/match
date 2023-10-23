from tkinter import *
import sqlite3

root = Tk()
root.title('Stat Reports')
root.geometry("900x500")

class app:

    def __init__(self, app):
        
        title_frame = Frame(app, bg="light blue")
        title_frame.pack(padx=10, pady=10)

        title = Label(app, text="Stat Reports", font=("Ariel", 48, 'bold'))
        title.pack()

d = app(root)

root.mainloop()