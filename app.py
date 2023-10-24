from tkinter import *
#import xlsxwriter
import openpyxl
import os

root = Tk()
root.title("Match report")
root.config(bg="light blue")

class App:

    def __init__(self,main):
        team_labelframe = LabelFrame(main, text="Team goals", font=("Helvetica", 20), bg="light blue", bd=5)
        team_labelframe.pack(padx=10, pady=10)

        line_up_frame = LabelFrame(main, text="Line Ups", font=("Helvetica", 20), bg="light blue", bd=5)
        line_up_frame.pack(padx=10, pady=10)

        button_frame = Frame(main, bg="light blue")
        button_frame.pack(padx=10, pady=10)

        self.red_label = Label(team_labelframe, text="Red Team", font=("Helvetica", 18), bg="Red", fg="white")
        self.red_label.grid(row=0, column=0, padx=10, pady=10)

        self.yellow_label = Label(team_labelframe, text="Yellow Team", font=("Helvetica", 18), bg="Yellow", fg="Black")
        self.yellow_label.grid(row=0, column=1, padx=10, pady=10)

        self.red_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER, bd=5)
        self.red_goal_entry.grid(row=1, column=0, padx=10, pady=10)

        self.yellow_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER, bd=5)
        self.yellow_goal_entry.grid(row=1, column=1, padx=10, pady=10)

        self.player_name_label = Label(line_up_frame, text="Player Name: ", font=("Helvetica", 24), bg="light blue")
        self.player_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.player_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.player_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_player_button = Button(line_up_frame, font=("Helvetica", 16), text="Add player", bg="light grey", command=self.add_player)
        self.add_player_button.grid(row=0, column=3, padx=10, pady=10)

        self.add_button = Button(button_frame, text="Add to spreadsheet", font=("Helvetica", 16), bg="light grey", bd=3, command=self.add)
        self.add_button.grid(row=2, column=0, ipadx=150, padx=10, pady=10)

        self.open_excel_file = Button(button_frame, text="Open spreadsheet", font=("Helvetica", 16), bg="light grey", bd=3, command=self.open_file)
        self.open_excel_file.grid(row=2, column=1, ipadx=150, padx=10, pady=10)

    def add(self):
        try:
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            sheet['A1'] = 'Red Team'
            sheet['B1'] = 'Yellow team'
            sheet['A2'] = self.red_goal_entry.get()
            sheet['B2'] = self.yellow_goal_entry.get()

            workbook.save('C:\\Users\\ijhus\\OneDrive\\Desktop\\hello.xlsx')

            self.red_goal_entry.delete(0,END)
            self.yellow_goal_entry.delete(0,END)
        except:
            print("error could not write as file is open in excel")

    def open_file(self):
        os.system('start "excel" "C:\\Users\\ijhus\\OneDrive\\Desktop\\hello.xlsx"')

    def add_player(self):
        pass

a = App(root)

root.mainloop()