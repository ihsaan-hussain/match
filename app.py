from tkinter import *
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import PatternFill
import os

root = Tk()
root.title("Match report")
root.config(bg="light blue")

class App:

    def __init__(self,main):
        #Frames
        team_labelframe = LabelFrame(main, text="Team goals", font=("Helvetica", 20), bg="light blue", bd=5)
        team_labelframe.pack(padx=10, pady=10)
        line_up_frame = LabelFrame(main, text="Line Ups/info", font=("Helvetica", 20), bg="light blue", bd=5)
        line_up_frame.pack(padx=10, pady=10)
        button_frame = Frame(main, bg="light blue")
        button_frame.pack(padx=10, pady=10)

        #Lists
        global red_player_list
        red_player_list = []
        global yellow_player_list
        yellow_player_list = []

        #Team goals
        self.red_label = Label(team_labelframe, text="Red Team", font=("Helvetica", 18), bg="Red", fg="white")
        self.red_label.grid(row=0, column=0, padx=10, pady=10)
        self.yellow_label = Label(team_labelframe, text="Yellow Team", font=("Helvetica", 18), bg="Yellow", fg="Black")
        self.yellow_label.grid(row=0, column=1, padx=10, pady=10)
        self.red_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER, bd=5)
        self.red_goal_entry.grid(row=1, column=0, padx=10, pady=10)
        self.yellow_goal_entry = Entry(team_labelframe, font=("Helvetica", 20), justify=CENTER, bd=5)
        self.yellow_goal_entry.grid(row=1, column=1, padx=10, pady=10)

        # Red player name and entry
        self.red_player_name_label = Label(line_up_frame, text="Player Name: ", font=("Helvetica", 24), bg="red", fg="white")
        self.red_player_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.red_player_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.red_player_entry.grid(row=0, column=1, padx=10, pady=10)

        # Yellow player name and entry
        self.yellow_player_name_label = Label(line_up_frame, text="Player Name: ", font=("Helvetica", 24), bg="yellow", fg="black")
        self.yellow_player_name_label.grid(row=0, column=2, padx=10, pady=10)
        self.yellow_player_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.yellow_player_entry.grid(row=0, column=3, padx=10, pady=10)

        # Buttons
        self.add_players_button = Button(line_up_frame, font=("Helvetica", 20), text="Add players", bg="light grey", command=self.add_player)
        self.add_players_button.grid(row=0, column=4, padx=10, pady=10)
        self.add_button = Button(button_frame, text="Add to spreadsheet", font=("Helvetica", 16), bg="light grey", bd=3, command=self.add)
        self.add_button.grid(row=2, column=0, ipadx=150, padx=10, pady=10)
        self.open_excel_file = Button(button_frame, text="Open spreadsheet", font=("Helvetica", 16), bg="light grey", bd=3, command=self.open_file)
        self.open_excel_file.grid(row=2, column=1, ipadx=150, padx=10, pady=10)

        # Text box
        self.player_text = Text(line_up_frame, font=("Helvetica", 16), height=10, width=30)
        self.player_text.grid(row=4, column=1, padx=10, pady=10)
        self.player_text2 = Text(line_up_frame, font=("Helvetica", 16), height=10, width=30)
        self.player_text2.grid(row=4, column=3, padx=10, pady=10)

        # Player Goals and Assists (red)
        self.goals_label = Label(line_up_frame, text="Player goals: ", font=("Helvetica", 24), bg="red", fg="white")
        self.goals_label.grid(row=1, column=0)
        self.assists_label = Label(line_up_frame, text="Player assists: ", font=("Helvetica", 24), bg="red", fg="white")
        self.assists_label.grid(row=2, column=0)
        self.goals_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.goals_entry.grid(row=1, column=1, padx=10, pady=10)
        self.assists_entry = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.assists_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Player Goals and Assists (yellow)
        self.goals_label = Label(line_up_frame, text="Player goals: ", font=("Helvetica", 24), bg="yellow", fg="black")
        self.goals_label.grid(row=1, column=2)
        self.assists_label = Label(line_up_frame, text="Player assists: ", font=("Helvetica", 24), bg="yellow", fg="black")
        self.assists_label.grid(row=2, column=2)
        self.goals_entry2 = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.goals_entry2.grid(row=1, column=3, padx=10, pady=10)
        self.assists_entry2 = Entry(line_up_frame, font=("Helvetica", 24), bd=5)
        self.assists_entry2.grid(row=2, column=3, padx=10, pady=10)

    def add(self):
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        sheet['A1'] = 'Red Team'
        sheet['B1'] = 'Yellow team'
        sheet['A2'] = self.red_goal_entry.get()
        sheet['B2'] = self.yellow_goal_entry.get()
        sheet['B3'] = '\n'


        for row in red_player_list:
            sheet.append(row)

        for row in yellow_player_list:
            sheet.append(row)

        workbook.save('C:\\Users\\ijhus\\OneDrive\\Desktop\\hello.xlsx')

        self.red_goal_entry.delete(0,END)
        self.yellow_goal_entry.delete(0,END)

    def open_file(self):
        os.system('start "excel" "C:\\Users\\ijhus\\OneDrive\\Desktop\\hello.xlsx"')

    def add_player(self):
        self.player_text.delete(0.0,END)
        self.player_text2.delete(0.0,END)

        self.red_player = self.red_player_entry.get()
        self.yellow_player = self.yellow_player_entry.get()

        self.red_player_goals = self.goals_entry.get()
        self.red_player_assists = self.assists_entry.get()

        self.yellow_player_goals = self.goals_entry2.get()
        self.yellow_player_assists = self.assists_entry2.get()

        self.red_player_info = []
        self.red_player_info.append(self.red_player)
        self.red_player_info.append(f'Goals: {str(self.red_player_goals)}')
        self.red_player_info.append(f'Assists: {str(self.red_player_assists)}') 

        self.yellow_player_info = []
        self.yellow_player_info.append(self.yellow_player)
        self.yellow_player_info.append(f'Goals: {str(self.yellow_player_goals)}')
        self.yellow_player_info.append(f'Assists: {str(self.yellow_player_assists)}')         

        red_player_list.append(self.red_player_info)
        yellow_player_list.append(self.yellow_player_info)

        for self.x in red_player_list:
            self.player_text.insert(END, str(self.x) + "\n")

        for self.x in yellow_player_list:
            self.player_text2.insert(END, str(self.x) + "\n")

        self.red_player_entry.delete(0,END)
        self.yellow_player_entry.delete(0,END)
        self.goals_entry.delete(0,END)
        self.goals_entry2.delete(0,END)

a = App(root)

root.mainloop()