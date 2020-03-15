"""Unit tests for the dungeon_set module."""
import unittest
from eso_pledge_tracker.dungeon_set import MonsterSet, DungeonSet, SetType, Set


class SetCreationTests(unittest.TestCase):
    """Tests the creation of a DungeonSet and a MonsterSet object."""
    def test_dungeon_set(self):
        dungeon_set = DungeonSet("set name", "Light", "second", "third",
                                 "fourth", "fifth")
        self.assertEqual("set name", dungeon_set.name)
        self.assertEqual(SetType.Light, dungeon_set.set_type)
        self.assertIsNone(dungeon_set.bonus.get(1))
        self.assertEqual("second", dungeon_set.bonus.get(2))
        self.assertEqual("third", dungeon_set.bonus.get(3))
        self.assertEqual("fourth", dungeon_set.bonus.get(4))
        self.assertEqual("fifth", dungeon_set.bonus.get(5))

    def test_monster_set(self):
        monster_set = MonsterSet("monster set", "first", "second")
        self.assertEqual("monster set", monster_set.name)
        self.assertEqual(SetType.Monster, monster_set.set_type)
        self.assertEqual("first", monster_set.bonus.get(1))
        self.assertEqual("second", monster_set.bonus.get(2))
        self.assertIsNone(monster_set.bonus.get(3))

    def test_abstract_set(self):
        """Raises TypeError because the Set class cannot be instantiated."""
        with self.assertRaises(TypeError):
            Set("name", "bonus", SetType.Monster)


class SetTypeTest(unittest.TestCase):
    """Tests the SetType enum."""
    def test_monster_type_for_dungeon(self):
        """Raises ValueError because "monster" is not a valid type for a DungeonSet."""
        with self.assertRaises(ValueError):
            DungeonSet("bad", "monster", "two", "three", "four", "five")

    def test_capitalization_required_for_dungeon(self):
        """Raises ValueError because we expect the types to be capital letters."""
        with self.assertRaises(ValueError):
            DungeonSet("bad", "light", "two", "three", "four", "five")

    def test_bad_type_for_dungeon(self):
        """Raises ValueError because "bad" is not a valid SetType."""
        with self.assertRaises(ValueError):
            DungeonSet("bad", "foo", "two", "three", "four", "five")

    def test_happy_enum(self):
        set_type = SetType("Light")
        self.assertEqual(SetType.Light, set_type)
        set_type = SetType("Medium")
        self.assertEqual(SetType.Medium, set_type)
        set_type = SetType("Heavy")
        self.assertEqual(SetType.Heavy, set_type)
        set_type = SetType("Monster")
        self.assertEqual(SetType.Monster, set_type)


if __name__ == '__main__':
    unittest.main()
