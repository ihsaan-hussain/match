class Players:
    def __init__(self):
        self.players = []
    
    def add_player(self, name, team, goals, assists):
        self.player_dictionary = {
            'name': None,
            'team': None,
            'goals': None,
            'assists': None
        }

        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

        self.player_dictionary['name'] = self.name
        self.player_dictionary['team'] = self.team
        self.player_dictionary['goals'] = self.goals
        self.player_dictionary['assists'] = self.assists

        self.players.append(self.player_dictionary)

    def list_players(self):
        for player in self.players:
            print(f'\n{player}')

x = Players()
for i in range(14):
    x.add_player('Ihsaan', 'Yellow', 10, 5)
x.list_players()