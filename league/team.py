
class Team:
    def __init__(self, nexus, Minions: list[minion], towers: list[towers], heroes: list[hero]) -> None:
        self.nexus = nexus
        self.Minions = Minions
        self.towers = towers
        self.heroes = heroes
    def spawn_minions(self):
        pass
    def get_minions(self):
       pass
    def get_towers(self):
        pass
    def get_nexus(self):
        return self.nexus
    def get_all(self):
        return self.Minions, self.towers, self.heroes, self.nexus
    def create_blue_team(self, heroes: list[hero]):
        pass
    def create_red_team(self, heroes: list[hero]):
        pass
