from eso_pledge_tracker.dungeon_set import MonsterSet, DungeonSet

import unittest


# obligatory
class TestTruth(unittest.TestCase):
    def test(self):
        assert True


class DungeonSetCreationTest(unittest.TestCase):
    def test_dungeon_set(self):
        dungeon_set = DungeonSet("weapon set", "second", "third", "fourth",
                                 "fifth")
        self.assertEqual(dungeon_set.name, "weapon set")
        self.assertEqual(dungeon_set.bonus.get(1), None)
        self.assertEqual(dungeon_set.bonus.get(2), "second")
        self.assertEqual(dungeon_set.bonus.get(3), "third")
        self.assertEqual(dungeon_set.bonus.get(4), "fourth")
        self.assertEqual(dungeon_set.bonus.get(5), "fifth")

    def test_bonus(self):
        monster_set = MonsterSet("monster set", "first", "second")
        self.assertEqual(monster_set.name, "monster set")
        self.assertEqual(monster_set.bonus.get(1), "first")
        self.assertEqual(monster_set.bonus.get(2), "second")
        self.assertEqual(monster_set.bonus.get(3), None)


if __name__ == '__main__':
    unittest.main()