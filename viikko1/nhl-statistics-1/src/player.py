class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def get_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.get_points()}"
