"""Tests the creation of a Dungeon object"""
import unittest
from eso_pledge_tracker import dungeon


class TestDungeon(unittest.TestCase):
    def test_dungeon(self):
        dun = dungeon.Dungeon("name", "monster", "light", "medium", "heavy")
        self.assertEqual("name", dun.name)
        self.assertEqual("monster", dun.monster_set)
        self.assertEqual("light", dun.dungeon_set_light)
        self.assertEqual("medium", dun.dungeon_set_medium)
        self.assertEqual("heavy", dun.dungeon_set_heavy)


if __name__ == '__main__':
    unittest.main()
