from tkinter import *
from tkinter import ttk
import openpyxl
import os

root = Tk()
root.title("Match report")
#root.geometry("1200x700+0+0")
root.config(bg="light blue")

class App:

    def __init__(self,main):

    	player_frame = Frame(main,bd=10,relief=RIDGE,bg="light blue")
    	player_frame.pack(side=LEFT)

    	extrainfo_frame = Frame(main,bd=10,relief=RIDGE,bg="light blue")
    	extrainfo_frame.pack(side=RIGHT)

    	players_frame = LabelFrame(player_frame, text="Players name/info", bd=5, font=("Helvetica", 20, 'bold'), bg="light blue")
    	players_frame.pack(padx=10,pady=10,fill=X)

    	extrainfos_frame = LabelFrame(extrainfo_frame, text="Extra info", bd=5, font=("Helvetica", 20, 'bold'),bg="light blue")
    	extrainfos_frame.pack(padx=10,pady=10,fill=X)

    	self.selected = StringVar()
    	self.team_pick = ttk.Combobox(players_frame, textvariable=self.selected)
    	self.team_pick['values'] = ['Red Team', 'Yellow Team']
    	self.team_pick['state'] = 'readonly'
    	self.team_pick.set('Red Team')
    	self.team_pick.grid(row=0,column=0,padx=20,pady=21)

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

    	self.add_player = Button(players_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Add Player", width=25)
    	self.add_player.grid(row=4,column=0,padx=10,pady=10)

    	self.clear_fields = Button(players_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Clear Fields", width=25)
    	self.clear_fields.grid(row=4,column=1,padx=10,pady=10)

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

    	self.add_info = Button(extrainfos_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Add Extra Info", width=25)
    	self.add_info.grid(row=4,column=0,padx=10,pady=10)

    	self.clear_fields = Button(extrainfos_frame, bd=5, bg="light grey", font=("Helvetica",15,'bold'), text="Clear Fields", width=25)
    	self.clear_fields.grid(row=4,column=1,padx=10,pady=10)

a = App(root)

root.mainloop()    	