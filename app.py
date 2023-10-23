from tkinter import *
#import xlsxwriter
import openpyxl
import os

root = Tk()
root.title("Match report")

class App:

    def __init__(self,main):
        team_labelframe = LabelFrame(main, text="Team goals", font=("Helvetica", 20))
        team_labelframe.pack(padx=10, pady=10)

        self.red_label = Label(team_labelframe, text="Red Team", font=("Helvetica", 18))
        self.red_label.grid(row=0, column=0, padx=10, pady=10)

        self.yellow_label = Label(team_labelframe, text="Yellow Team", font=("Helvetica", 18))
        self.yellow_label.grid(row=0, column=1, padx=10, pady=10)

        self.red_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER)
        self.red_goal_entry.grid(row=1, column=0, padx=10, pady=10)

        self.yellow_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER)
        self.yellow_goal_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = Button(team_labelframe, text="Add to spreadsheet", font=("Helvetica", 16), command=self.add)
        self.add_button.grid(row=2, column=0, ipadx=150, padx=10, pady=10, columnspan=3)

        self.open_excel_file = Button(team_labelframe, text="Open spreadsheet", font=("Helvetica", 16), command=self.open_file)
        self.open_excel_file.grid(row=3, column=0, ipadx=150, padx=10, pady=10, columnspan=3)

    def add(self):
        try:
            workbook = openpyxl.Workbook()
            # Get the active sheet
            sheet = workbook.active
            # Write data to cells
            sheet['A1'] = 'Red Team'
            sheet['B1'] = 'Yellow team'
            sheet['A2'] = self.red_goal_entry.get()
            sheet['B2'] = self.yellow_goal_entry.get()

            workbook.save('C:\\Users\\ijhus\\OneDrive\\Desktop\\hello.xlsx')

            self.red_goal_entry.delete(0,END)
            self.yellow_goal_entry.delete(0,END)
        except:
            print("error could not write")

    def open_file(self):
        os.system('start "excel" "C:\\Users\\ijhus\\OneDrive\\Desktop\\hello.xlsx"')

a = App(root)

root.mainloop()