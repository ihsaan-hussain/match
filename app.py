from tkinter import *
#import xlsxwriter
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo
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

        global red_player_list
        red_player_list = []
        global yellow_player_list
        yellow_player_list = []

        self.red_label = Label(team_labelframe, text="Red Team", font=("Helvetica", 18), bg="Red", fg="white")
        self.red_label.grid(row=0, column=0, padx=10, pady=10)

        self.yellow_label = Label(team_labelframe, text="Yellow Team", font=("Helvetica", 18), bg="Yellow", fg="Black")
        self.yellow_label.grid(row=0, column=1, padx=10, pady=10)

        self.red_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER, bd=5)
        self.red_goal_entry.grid(row=1, column=0, padx=10, pady=10)

        self.yellow_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER, bd=5)
        self.yellow_goal_entry.grid(row=1, column=1, padx=10, pady=10)

        self.red_player_name_label = Label(line_up_frame, text="Player Name: ", font=("Helvetica", 24), bg="red", fg="white")
        self.red_player_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.red_player_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.red_player_entry.grid(row=0, column=1, padx=10, pady=10)

        self.yellow_player_name_label = Label(line_up_frame, text="Player Name: ", font=("Helvetica", 24), bg="yellow", fg="black")
        self.yellow_player_name_label.grid(row=0, column=2, padx=10, pady=10)

        self.yellow_player_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.yellow_player_entry.grid(row=0, column=3, padx=10, pady=10)

        self.add_players_button = Button(line_up_frame, font=("Helvetica", 20), text="Add players", bg="light grey", command=self.add_player)
        self.add_players_button.grid(row=0, column=4, padx=10, pady=10)

        self.player_text = Text(line_up_frame, font=("Helvetica", 16), height=10, width=20)
        self.player_text.grid(row=1, column=1, padx=10, pady=10)

        self.player_text2 = Text(line_up_frame, font=("Helvetica", 16), height=10, width=20)
        self.player_text2.grid(row=1, column=3, padx=10, pady=10)

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
        self.player_text.delete(0.0,END)
        self.player_text2.delete(0.0,END)
        self.red_player = self.red_player_entry.get()
        self.yellow_player = self.yellow_player_entry.get()
        red_player_list.append(self.red_player)
        yellow_player_list.append(self.yellow_player)

        for self.x in red_player_list:
            self.player_text.insert(END, self.x + "\n")


        for self.x in yellow_player_list:
            self.player_text2.insert(END, self.x + "\n")

        

a = App(root)

root.mainloop()