# Template for a Dungeon or Monster Set
from abc import ABC


# abstract class
class Set(ABC):
    name: str
    bonus: dict

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus


# the dictionary looks like {1: "bonus_one", 2: "bonus_two"}
class MonsterSet(Set):
    def __init__(self, name, bonus_one, bonus_two):
        bonus_list = [bonus_one, bonus_two]
        bonus_dict = {i: b for i, b in enumerate(bonus_list, 1)}
        super(MonsterSet, self).__init__(name, bonus_dict)


class DungeonSet(Set):
    def __init__(self, name, bonus_two, bonus_three, bonus_four, bonus_five):
        bonus_list = [bonus_two, bonus_three, bonus_four, bonus_five]
        bonus_dict = {i: b for i, b in enumerate(bonus_list, 2)}
        super(DungeonSet, self).__init__(name, bonus_dict)
