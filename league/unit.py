import pygame
from team import Team
from ability import Ability

class Unit:
    def __init__(self, base_health: int, base_damage: int, base_armor: int, base_range: int, team: Team, enemy_team: Team) -> None:
        self._base_health = base_health
        self._base_damage = base_damage
        self._base_armor = base_armor
        self._base_range = base_range
        self._team = team
        self._enemy_team = enemy_team

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
        return self._base_damage

    def get_health(self) -> int:
        return self._base_health

    def get_armor(self) -> int:
        return self._base_armor

    def get_range(self) -> int:
        return self._base_range
