
class Team:
    def __init__(self, nexus, minions: Unit, towers: Unit, heroes: list[heroes] -> None:
        self.nexus = nexus
        self.minions = minions
        self.towers = towers
        self.heroes = heroes
    def spawn_minions(self):
        pass
    def get_minions(self):
       return self.minions
    def get_towers(self):
        return self.towers
    def get_nexus(self):
        return self.nexus
    def get_all(self):
        return self.Minions, self.towers, self.heroes, self.nexus
    def create_blue_team(self, heroes: list[hero]):
        pass
    def create_red_team(self, heroes: list[hero]):
        pass
