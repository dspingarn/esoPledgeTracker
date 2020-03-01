# template class for a Dungeon


class Dungeon:

    name: str
    weapon_set_unique: str
    weapon_set_light: str
    weapon_set_medium: str
    weapon_set_heavy: str

    def __init__(self, name, weapon_set_unique, weapon_set_light,
                 weapon_set_medium, weapon_set_heavy):
        self.name = name
        self.weapon_set_unique = weapon_set_unique
        self.weapon_set_light = weapon_set_light
        self.weapon_set_medium = weapon_set_medium
        self.weapon_set_heavy = weapon_set_heavy
