from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import openpyxl
import xlsxwriter
import os

root = Tk()
root.title("Match report")
#root.geometry("1200x700+0+0")
root.config(bg="light blue")

class App:

    def __init__(self,main):

        topframe = Frame(main,bd=10,bg="light blue",relief=GROOVE)
        topframe.pack(side=TOP,fill=X)

        scoresframe = Frame(main,bd=10,bg="light blue",relief=GROOVE)
        scoresframe.pack(side=TOP,fill=X)

        scorelabelframe = LabelFrame(scoresframe, text="Match Score", bd=5, font=("Helvetica", 20, 'bold'), bg="light blue")
        scorelabelframe.pack(padx=10,pady=10,fill=X)

        player_frame = Frame(main,bd=10,relief=GROOVE,bg="light blue")
        player_frame.pack(side=LEFT,fill=Y)

        extrainfo_frame = Frame(main,bd=10,relief=GROOVE,bg="light blue")
        extrainfo_frame.pack(side=RIGHT,fill=Y)

        players_frame = LabelFrame(player_frame, text="Players name/info", bd=5, font=("Helvetica", 20, 'bold'), bg="light blue")
        players_frame.pack(padx=10,pady=10,fill=X)

        extrainfos_frame = LabelFrame(extrainfo_frame, text="Extra info", bd=5, font=("Helvetica", 20, 'bold'),bg="light blue")
        extrainfos_frame.pack(padx=10,pady=10,fill=X)

        buttonlabelframe = LabelFrame(scoresframe, text="Buttons", bd=5, font=("Helvetica", 20, 'bold'),bg="light blue")
        buttonlabelframe.pack(padx=10,pady=10,fill=X)        

        self.title = Label(topframe,text="Match Report", font=("Helvetica", 28, 'bold'),bg="light blue")
        self.title.pack(padx=10,pady=10)

        self.red_score_label = Label(scorelabelframe,bg="red",fg="white",text="Red Team", font=("Helvetica", 20, 'bold'))
        self.red_score_label.grid(row=0, column=0, padx=10, pady=10)

        self.red_score_entry = Entry(scorelabelframe,font=("Helvetica", 20, 'bold'), bd=5, width=5, justify=CENTER)
        self.red_score_entry.grid(row=0,column=1, padx=10, pady=10)

        self.yellow_score_label = Label(scorelabelframe,bg="yellow",text="Yellow Team", font=("Helvetica", 20, 'bold'))
        self.yellow_score_label.grid(row=0, column=2, padx=10, pady=10)

        self.yellow_score_entry = Entry(scorelabelframe,font=("Helvetica", 20, 'bold'), bd=5, width=5, justify=CENTER)
        self.yellow_score_entry.grid(row=0,column=3, padx=10, pady=10)

        self.save_score = Button(scorelabelframe,text="Save score",bg="light grey",font=("Helvetica",20,'bold'),bd=5,width=20,command=self.savescore)
        self.save_score.grid(row=0,column=4,padx=10,pady=10)

        self.current_file_label = Label(scorelabelframe, bg="light blue", font=("Helvetica", 15, 'bold'), text="Current file: ")
        self.current_file_label.grid(row=0, column=5, padx=10, pady=10)

        self.current_entry = Entry(scorelabelframe, bd=5, font=("Helvetica", 20, 'bold'))
        self.current_entry.grid(row=0,column=6,padx=10,pady=10)

        self.selected = StringVar()
        self.team_pick = ttk.Combobox(players_frame, textvariable=self.selected)
        self.team_pick['values'] = ['Red Team', 'Yellow Team']
        self.team_pick['state'] = 'readonly'
        self.team_pick.set('Red Team')
        self.team_pick.grid(row=0,column=0,padx=10,pady=10)

        self.player_name_label = Label(players_frame, text="Player Name:", font=("Helvetica", 20, 'bold'), bg="light blue")
        self.player_name_label.grid(row=1,column=0,padx=10,pady=10)

        self.player_entry = Entry(players_frame, bd=5, font=("Helvetica", 20, 'bold'), width=20)
        self.player_entry.grid(row=1,column=1,padx=10,pady=10)

        self.player_goals_label = Label(players_frame, text="Player goals:", font=("Helvetica", 20, 'bold'), bg="light blue")
        self.player_goals_label.grid(row=2,column=0,padx=10,pady=10)

        self.player_goals_entry = Entry(players_frame, bd=5, font=("Helvetica", 20, 'bold'), width=20, justify=CENTER)
        self.player_goals_entry.grid(row=2,column=1,padx=10,pady=10)

        self.player_assists_label = Label(players_frame, text="Player assists:", font=("Helvetica", 20, 'bold'), bg="light blue")
        self.player_assists_label.grid(row=3,column=0,padx=10,pady=10)

        self.player_assists_entry = Entry(players_frame, bd=5, font=("Helvetica", 20, 'bold'), width=20, justify=CENTER)
        self.player_assists_entry.grid(row=3,column=1,padx=10,pady=10)

        self.add_player = Button(players_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Add Player", width=25,command=self.addplayer)
        self.add_player.grid(row=4,column=0,padx=10,pady=10)

        self.clear_fields = Button(players_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Clear Fields", width=25,command=self.clearplayers)
        self.clear_fields.grid(row=4,column=1,padx=10,pady=10)

        self.filler_label = Label(player_frame, text="                                                                                                                                  ", bg="light blue", fg="light blue", font=("Helvetica", 15, 'bold'))
        self.filler_label.pack(padx=10,pady=10)

        self.motm_label = Label(extrainfos_frame, bd=5, bg="light blue", font=("Helvetica",20,'bold'), text="MOTM: ")
        self.motm_label.grid(row=0,column=0,padx=10,pady=10)

        self.motm_entry = Entry(extrainfos_frame, bd=5, font=("Helvetica", 20, 'bold'), width=20)
        self.motm_entry.grid(row=0,column=1,padx=10,pady=10)

        self.topscorer_label = Label(extrainfos_frame, bd=5, bg="light blue", font=("Helvetica",20,'bold'), text="Top Scorer: ")
        self.topscorer_label.grid(row=1,column=0,padx=10,pady=10)

        self.topscorer_entry = Entry(extrainfos_frame, bd=5, font=("Helvetica", 20, 'bold'), width=20)
        self.topscorer_entry.grid(row=1,column=1,padx=10,pady=10)

        self.possesion_label = Label(extrainfos_frame, bd=5, bg="light blue", font=("Helvetica",20,'bold'), text="Posession Red:")
        self.possesion_label.grid(row=2,column=0,padx=10,pady=10)

        self.possesion_entry = Entry(extrainfos_frame, bd=5, font=("Helvetica", 20, 'bold'), width=5, justify=CENTER)
        self.possesion_entry.grid(row=2,column=1,padx=10,pady=10)

        self.possesion2_label = Label(extrainfos_frame, bd=5, bg="light blue", font=("Helvetica",20,'bold'), text="Posession Yellow:")
        self.possesion2_label.grid(row=3,column=0,padx=10,pady=10)

        self.possesion2_entry = Entry(extrainfos_frame, bd=5, font=("Helvetica", 20, 'bold'), width=5, justify=CENTER)
        self.possesion2_entry.grid(row=3,column=1,padx=10,pady=10)

        self.add_info = Button(extrainfos_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Add Extra Info", width=25,command=self.addinfo)
        self.add_info.grid(row=4,column=0,padx=10,pady=10)

        self.clear_fields = Button(extrainfos_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Clear Fields", width=25,command=self.clearinfo)
        self.clear_fields.grid(row=4,column=1,padx=10,pady=10)

        self.create_spreadsheet = Button(buttonlabelframe, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Create Spreadsheet", width=25,command=self.createspreadsheet)
        self.create_spreadsheet.grid(row=0,column=0,padx=30,pady=10)

        self.open_spreadsheet = Button(buttonlabelframe, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Open Spreadsheet", width=25,command=self.openspreadsheet)
        self.open_spreadsheet.grid(row=0,column=1,padx=30,pady=10)

        self.add_spreadsheet = Button(buttonlabelframe, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Save to Spreadsheet", width=25,command=self.addspreadsheet)
        self.add_spreadsheet.grid(row=0,column=2,padx=30,pady=10)

        self.see_players = Button(buttonlabelframe, bd=5, bg="light grey", font=("Helvetica",15,'bold'),text="See added players", width=25,command=self.seeplayers)
        self.see_players.grid(row=0, column=3, padx=30, pady=10)

    def seeplayers(self):
        pass

    def addspreadsheet(self):
        pass

    def openspreadsheet(self):
        pass

    def createspreadsheet(self):
        self.file = filedialog.asksaveasfile(title="Open a File", filetype=(("xlsx files", ".*xlsx"),("All Files", "*.")))

    def addinfo(self):
        pass

    def clearinfo(self):
        self.motm_entry.delete(0,END)
        self.topscorer_entry.delete(0,END)
        self.possesion_entry.delete(0,END)
        self.possesion2_entry.delete(0,END)

    def clearplayers(self):
        self.player_entry.delete(0,END)
        self.player_goals_entry.delete(0,END)
        self.player_assists_entry.delete(0,END)

    def addplayer(self):
        pass

    def savescore(self):
        pass 

    def get(self, x):
        x = self.fileinput.get()
        self.newwin.destroy()

a = App(root)

root.mainloop()    	