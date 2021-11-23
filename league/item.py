from .stats import Stats

class Item:
    def __init__(self, name: str, level: int, stat_buff: Stats):
        self.name = name
        if level < 1:
            raise ValueError("Level can't be negative.")
        self.level = level
        self.stat_buff = stat_buff

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name
    
    def get_level(self) -> int:
        return self.level

    def set_level(self, level: int) -> None:
        if level < 1:
            raise ValueError("Level can't be negative.")
        self.level = level

    def get_cost(self) -> int:
        return self.level * 100

    def get_stat_buff(self) -> Stats:
        return self.stat_buff

    def set_stat_buff(self, stats: Stats) -> None:
        self.stat_buff = stats
