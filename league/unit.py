import pygame
from team import Team
from ability import Ability

class Unit:
    def __init__(self, base_health: int, base_damage: int, base_armor: int, base_range: int, team: Team, enemy_team: Team) -> None:
        self.base_health = base_health
        self.base_damage = base_damage
        self.base_armor = base_armor
        self.base_range = base_range
        self.team = team
        self.enemy_team = enemy_team

    def apply_debuff(self, debuff: Ability):
        "Take an Ability object and stores the debuff"
        pass

    def implement_debuffs(self):
        "Applies the debuffs onto the unit"
        pass

    def update(self):
        "Updates the player debuffs when the duration of debuff is over"
        pass

    def get_damage(self) -> int:
        self.base_damage

    def get_health(self) -> int:
        self.base_health

    def get_armor(self) -> int:
        self.base_armor

    def get_range(self) -> int:
        self.base_range
