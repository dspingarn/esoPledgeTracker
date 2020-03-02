import unittest
from eso_pledge_tracker.dungeon_set import MonsterSet, DungeonSet


class DungeonSetCreationTest(unittest.TestCase):
    def test_dungeon_set(self):
        dungeon_set = DungeonSet("weapon set", "second", "third", "fourth",
                                 "fifth")
        self.assertEqual("weapon set", dungeon_set.name)
        self.assertIsNone(dungeon_set.bonus.get(1))
        self.assertEqual("second", dungeon_set.bonus.get(2))
        self.assertEqual("third", dungeon_set.bonus.get(3))
        self.assertEqual("fourth", dungeon_set.bonus.get(4))
        self.assertEqual("fifth", dungeon_set.bonus.get(5))

    def test_bonus(self):
        monster_set = MonsterSet("monster set", "first", "second")
        self.assertEqual("monster set", monster_set.name)
        self.assertEqual("first", monster_set.bonus.get(1))
        self.assertEqual("second", monster_set.bonus.get(2))
        self.assertIsNone(monster_set.bonus.get(3))


if __name__ == '__main__':
    unittest.main()
