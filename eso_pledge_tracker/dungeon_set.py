"""Template for a Dungeon or Monster Set"""
from abc import ABC


class Set(ABC):
    """Abstract class for a generic set"""
    name: str
    bonus: dict

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus


class MonsterSet(Set):
    """A MonsterSet is a Set with two bonus effects"""

    # the dictionary looks like {1: "bonus_one", 2: "bonus_two"}
    def __init__(self, name, bonus_one, bonus_two):
        bonus_list = [bonus_one, bonus_two]
        bonus_dict = {i: b for i, b in enumerate(bonus_list, 1)}
        super(MonsterSet, self).__init__(name, bonus_dict)


class DungeonSet(Set):
    """A DungeonSet is a Set with four bonus effects and a weight (light, medium, heavy)"""
    def __init__(self, name, weight, bonus_two, bonus_three, bonus_four,
                 bonus_five):
        self.weight = weight
        bonus_list = [bonus_two, bonus_three, bonus_four, bonus_five]
        bonus_dict = {i: b for i, b in enumerate(bonus_list, 2)}
        super(DungeonSet, self).__init__(name, bonus_dict)
