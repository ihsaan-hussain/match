# Import libraries
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# App object
class MatchReportApp:
    def __init__(self, root):
        # Initialize the window
        self.root = root
        self.root.title("Football Match Report Generator")
        # create all the widgets for the GUI
        self.create_widgets()

    def create_widgets(self):
        # Team 1 (RED)
        ttk.Label(self.root, text="Team 1 Name:").grid(column=0, row=0, sticky=tk.W)
        self.team1_name = ttk.Entry(self.root)
        self.team1_name.grid(column=1, row=0, sticky=tk.W)
        self.team1_name.insert(0, 'Red')
        self.team1_name.config(state=tk.DISABLED)

        ttk.Label(self.root, text="Red Team Score:").grid(column=0, row=1, sticky=tk.W)
        self.team1_score = ttk.Entry(self.root)
        self.team1_score.grid(column=1, row=1, sticky=tk.W)

        ttk.Label(self.root, text="Red Possession (%):").grid(column=0, row=2, sticky=tk.W)
        self.team1_possession = ttk.Entry(self.root)
        self.team1_possession.grid(column=1, row=2, sticky=tk.W)

        ttk.Label(self.root, text="Red Team Lineup (comma-separated):").grid(column=0, row=3, sticky=tk.W)
        self.team1_lineup = ttk.Entry(self.root)
        self.team1_lineup.grid(column=1, row=3, sticky=tk.W)

        ttk.Label(self.root, text="Red Team Goals (comma-separated):").grid(column=0, row=4, sticky=tk.W)
        self.team1_goals = ttk.Entry(self.root)
        self.team1_goals.grid(column=1, row=4, sticky=tk.W)

        ttk.Label(self.root, text="Red Team Assists (comma-separated):").grid(column=0, row=5, sticky=tk.W)
        self.team1_assists = ttk.Entry(self.root)
        self.team1_assists.grid(column=1, row=5, sticky=tk.W)

        # Team 2 (YELLOW)
        ttk.Label(self.root, text="Team 2 Name:").grid(column=0, row=6, sticky=tk.W)
        self.team2_name = ttk.Entry(self.root)
        self.team2_name.grid(column=1, row=6, sticky=tk.W)
        self.team2_name.insert(0, 'Yellow')
        self.team2_name.config(state=tk.DISABLED)

        ttk.Label(self.root, text="Yellow Score:").grid(column=0, row=7, sticky=tk.W)
        self.team2_score = ttk.Entry(self.root)
        self.team2_score.grid(column=1, row=7, sticky=tk.W)

        ttk.Label(self.root, text="Yellow Possession (%):").grid(column=0, row=8, sticky=tk.W)
        self.team2_possession = ttk.Entry(self.root)
        self.team2_possession.grid(column=1, row=8, sticky=tk.W)

        ttk.Label(self.root, text="Yellow Lineup (comma-separated):").grid(column=0, row=9, sticky=tk.W)
        self.team2_lineup = ttk.Entry(self.root)
        self.team2_lineup.grid(column=1, row=9, sticky=tk.W)

        ttk.Label(self.root, text="Yellow Goals (comma-separated):").grid(column=0, row=10, sticky=tk.W)
        self.team2_goals = ttk.Entry(self.root)
        self.team2_goals.grid(column=1, row=10, sticky=tk.W)

        ttk.Label(self.root, text="Yellow Assists (comma-separated):").grid(column=0, row=11, sticky=tk.W)
        self.team2_assists = ttk.Entry(self.root)
        self.team2_assists.grid(column=1, row=11, sticky=tk.W)

        # Man of the Match
        ttk.Label(self.root, text="Man of the Match:").grid(column=0, row=12, sticky=tk.W)
        self.man_of_the_match = ttk.Entry(self.root)
        self.man_of_the_match.grid(column=1, row=12, sticky=tk.W)

        # Generate Report Button
        self.generate_button = ttk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.generate_button.grid(column=0, row=13, columnspan=2, pady=10)

    # Create the Excel file
    def generate_report(self):
        # Gather the information in all the inputs
        team1_name = self.team1_name.get()
        team2_name = self.team2_name.get()
        team1_score = int(self.team1_score.get())
        team2_score = int(self.team2_score.get())
        team1_possession = self.team1_possession.get()
        team2_possession = self.team2_possession.get()
        man_of_the_match = self.man_of_the_match.get()

        team1_lineup = self.team1_lineup.get().split(',')
        team1_goals = self.team1_goals.get().split(',')
        team1_assists = self.team1_assists.get().split(',')

        team2_lineup = self.team2_lineup.get().split(',')
        team2_goals = self.team2_goals.get().split(',')
        team2_assists = self.team2_assists.get().split(',')

        # Organise the data so that red players stats and yellow players stats are given to the correct players
        team1_data = [{'Player': player.strip(), 'Goals': int(goal.strip()), 'Assists': int(assist.strip())} for player, goal, assist in zip(team1_lineup, team1_goals, team1_assists)]
        team2_data = [{'Player': player.strip(), 'Goals': int(goal.strip()), 'Assists': int(assist.strip())} for player, goal, assist in zip(team2_lineup, team2_goals, team2_assists)]
        
        # Try means to run the code normally
        try:
            # Create a 'pandas' dataframe
            team1_df = pd.DataFrame(team1_data)
            team2_df = pd.DataFrame(team2_data)

            # write to Excel file
            writer = pd.ExcelWriter('football_match_report.xlsx', engine='openpyxl')

            team1_df.to_excel(writer, sheet_name=f'{team1_name}_Data', index=False)
            team2_df.to_excel(writer, sheet_name=f'{team2_name}_Data', index=False)

            summary_data = {
                'Team': [team1_name, team2_name],
                'Score': [team1_score, team2_score],
                'Possession (%)': [team1_possession, team2_possession]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Match_Summary', index=False)

            motm_df = pd.DataFrame({'Man of the Match': [man_of_the_match]})
            motm_df.to_excel(writer, sheet_name='Man_of_the_Match', index=False)

            writer._save()
            messagebox.showinfo("Success", "Football match report has been successfully generated and saved as 'football_match_report.xlsx'.")
        # If there is an error in the process of saving then an error message will pop up on the screen
        except:
            messagebox.showerror("Permission Denied", "PermissionError: [Errno 13] Permission denied: 'football_match_report.xlsx'")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatchReportApp(root)
    root.mainloop()