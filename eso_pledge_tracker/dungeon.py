"""Template class for a Dungeon. Also defines a PledgeMaster enum."""
from enum import Enum


# note to self: enum can have multiple values
class PledgeMaster(Enum):
    """Enum for the three Undaunted PledgeMasters:
    Maj al-Ragath, Glirion the Redbeard, and Urgarlag Chief-Bane."""
    MAJ = 'Maj al-Ragath'
    GLIRION = 'Glirion the Redbeard'
    URGARLAG = 'Urgarlag Chief-bane'


class Dungeon:
    """A Dungeon has four different sets associated with it:
    the Monster Set (unique to the Dungeon), a Light Armor Set,
    a Medium Armor Set, and a Heavy Armor Set.
    In addition, each dungeon is associated with a PledgeMaster,
    and for ordering purposes an index has been assigned to each dungeon
    for their respective PledgeMaster's dungeon cycle."""
    name: str
    monster_set: str
    dungeon_set_light: str
    dungeon_set_medium: str
    dungeon_set_heavy: str
    pledge_master: PledgeMaster
    cycle_index: int

    def __init__(self, name, monster_set, dungeon_set_light,
                 dungeon_set_medium, dungeon_set_heavy, pledge_master,
                 cycle_index):
        self.name = name
        self.monster_set = monster_set
        self.dungeon_set_light = dungeon_set_light
        self.dungeon_set_medium = dungeon_set_medium
        self.dungeon_set_heavy = dungeon_set_heavy
        self.pledge_master = pledge_master
        self.cycle_index = cycle_index
