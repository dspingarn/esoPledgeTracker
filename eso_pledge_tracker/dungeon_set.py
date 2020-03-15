"""Template for a Dungeon or Monster Set. Also defines the SetType enum."""
from abc import ABC
from enum import Enum


class SetType(Enum):
    """An enum to differentiate the types of Sets. MonsterSets are not weight-unique, whereas
    Light, Medium, and Heavy armor Sets are DungeonSets,
    and we differentiate between them by weight for sorting purposes."""
    Monster = "Monster"
    Light = "Light"
    Medium = "Medium"
    Heavy = "Heavy"


class Set(ABC):
    """Abstract class for a generic Set.
    The bonus field is a dict that may look like {1: "bonus_one", 2: "bonus_two"}, for example."""
    name: str
    bonus: dict
    set_type: SetType

    def __init__(self, name, bonus, set_type):
        self.name = name
        self.bonus = bonus
        self.set_type = set_type

    #pylint: disable=unused-argument
    def __new__(cls, *args):
        if cls is Set:
            raise TypeError("Set may not be instantiated.")
        return object.__new__(cls)


class MonsterSet(Set):
    """A MonsterSet is a Set with two bonus effects, indexing at 1,
    as equipping only one item still gives a bonus."""
    def __init__(self, name, bonus_one, bonus_two):
        bonus_list = [bonus_one, bonus_two]
        bonus_dict = {i: b for i, b in enumerate(bonus_list, 1)}
        super(MonsterSet, self).__init__(name, bonus_dict, SetType.Monster)


class DungeonSet(Set):
    """A DungeonSet is a Set with a weight (Light, Medium, or Heavy) up to four bonus effects
    (indexing at 2, because equipping one item does not grant the set bonus).
    Raises a ValueError exception if the DungeonSet is not Light, Medium, or Heavy."""
    def __init__(self, name, weight, bonus_two, bonus_three, bonus_four,
                 bonus_five):
        if weight == "Monster":
            raise ValueError(('Dungeons can either be Light, Medium, or Heavy'
                              ' but not Monster.'))
        bonus_list = [bonus_two, bonus_three, bonus_four, bonus_five]
        bonus_dict = {i: b for i, b in enumerate(bonus_list, 2)}
        super(DungeonSet, self).__init__(name, bonus_dict, SetType(weight))
