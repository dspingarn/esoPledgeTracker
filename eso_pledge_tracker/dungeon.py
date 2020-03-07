"""template class for a Dungeon"""


class Dungeon:
    """A Dungeon has four different sets associated with it"""
    name: str
    monster_set: str
    dungeon_set_light: str
    dungeon_set_medium: str
    dungeon_set_heavy: str

    def __init__(self, name, monster_set, dungeon_set_light,
                 dungeon_set_medium, dungeon_set_heavy):
        self.name = name
        self.monster_set = monster_set
        self.dungeon_set_light = dungeon_set_light
        self.dungeon_set_medium = dungeon_set_medium
        self.dungeon_set_heavy = dungeon_set_heavy
