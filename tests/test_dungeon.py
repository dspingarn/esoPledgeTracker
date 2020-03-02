import unittest
from eso_pledge_tracker import dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon(self):
        dun = dungeon.Dungeon("name", "unique", "light", "medium", "heavy")
        self.assertEqual("name", dun.name)
        self.assertEqual("unique", dun.weapon_set_unique)
        self.assertEqual("light", dun.weapon_set_light)
        self.assertEqual("medium", dun.weapon_set_medium)
        self.assertEqual("heavy", dun.weapon_set_heavy)


if __name__ == '__main__':
    unittest.main()
