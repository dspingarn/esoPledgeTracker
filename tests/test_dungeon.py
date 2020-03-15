"""Unit tests for the dungeon module."""
import unittest
from eso_pledge_tracker.dungeon import Dungeon, PledgeMaster


class TestPledgeMasterEnum(unittest.TestCase):
    """Tests the PledgeMaster enum."""
    def test_pledge_master(self):
        pledge_master = PledgeMaster.MAJ
        self.assertEqual("Maj al-Ragath", pledge_master.value)
        self.assertEqual("MAJ", pledge_master.name)
        pledge_master_two = PledgeMaster('Maj al-Ragath')
        self.assertEqual(pledge_master, pledge_master_two)


class TestDungeon(unittest.TestCase):
    """Tests the creation of a Dungeon."""
    def test_dungeon(self):
        dun = Dungeon("name", "monster", "light", "medium", "heavy",
                      PledgeMaster.MAJ, 0)
        self.assertEqual("name", dun.name)
        self.assertEqual("monster", dun.monster_set)
        self.assertEqual("light", dun.dungeon_set_light)
        self.assertEqual("medium", dun.dungeon_set_medium)
        self.assertEqual("heavy", dun.dungeon_set_heavy)
        self.assertEqual(PledgeMaster.MAJ, dun.pledge_master)
        self.assertEqual(0, dun.cycle_index)


if __name__ == '__main__':
    unittest.main()
