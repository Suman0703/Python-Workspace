# Aggregation means one class uses another class, but both can exist independently.

class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, players):
        self.players = players   # aggregation

    def show_players(self):
        for p in self.players:
            print(p.name)

p1 = Player("Ram")
p2 = Player("Sita")

t = Team([p1, p2])
t.show_players()

