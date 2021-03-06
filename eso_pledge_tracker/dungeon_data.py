"""Reads in all of the Dungeon, DungeonSet, and MonsterSet data
from the .csv files in the data directory. This populates the
DUNGEONS lists for each pledge master, as well as the MONTER_SETS and
DUNGEON_SETS dicts."""

import csv
from .dungeon import Dungeon, PledgeMaster
from .dungeon_set import DungeonSet, MonsterSet, SetType

DUNGEONS_MAJ = []
DUNGEONS_GLI = []
DUNGEONS_URG = []
MONSTER_SETS = {}
DUNGEON_SETS = {}

with open('data/dungeon_set_relation.csv', newline='') as csvfile:
    DUNGEON_READER = csv.reader(csvfile, delimiter=',')
    # skip the header
    next(DUNGEON_READER)
    for row in DUNGEON_READER:
        (name, pledge_master, cycle_index, monster_set, dungeon_set_light,
         dungeon_set_medium, dungeon_set_heavy) = row
        read_dungeon = Dungeon(name, monster_set, dungeon_set_light,
                               dungeon_set_medium, dungeon_set_heavy,
                               PledgeMaster(pledge_master), cycle_index)
        if read_dungeon.pledge_master == PledgeMaster.MAJ:
            DUNGEONS_MAJ.append(read_dungeon)
        elif read_dungeon.pledge_master == PledgeMaster.GLIRION:
            DUNGEONS_GLI.append(read_dungeon)
        elif read_dungeon.pledge_master == PledgeMaster.URGARLAG:
            DUNGEONS_URG.append(read_dungeon)
        else:
            print("Read in {} but couldn't classify it.\n".format(row))
            raise Exception

with open('data/monster_set.csv', newline='') as csvfile:
    MONSTER_READER = csv.reader(csvfile, delimiter=',')
    next(MONSTER_READER)
    for row in MONSTER_READER:
        (name, effect_one, effect_two) = row
        read_monster_set = MonsterSet(name, effect_one, effect_two)
        MONSTER_SETS[name] = read_monster_set

with open('data/dungeon_set.csv', newline='') as csvfile:
    DUNGEON_SET_READER = csv.reader(csvfile, delimiter=',')
    next(DUNGEON_SET_READER)
    for row in DUNGEON_SET_READER:
        (name, effect_two, effect_three, effect_four, effect_five,
         armor_class) = row
        read_dungeon_set = DungeonSet(name, armor_class, effect_two,
                                      effect_three, effect_four, effect_five)
        DUNGEON_SETS[name] = read_dungeon_set


def get_set_by_name(dungeon, dungeon_name):
    """Find the Dungeon or Monster Set associated with this Dungeon and a set name."""
    if dungeon_name == dungeon.monster_set:
        return MONSTER_SETS[dungeon_name]
    return DUNGEON_SETS[dungeon_name]


def get_set_by_type(dungeon, set_type):
    """Find the Set associated with this Dungeon for a given SetType."""
    if set_type == SetType.Monster:
        return MONSTER_SETS[dungeon.monster_set]
    switch = {
        SetType.Light: dungeon.dungeon_set_light,
        SetType.Medium: dungeon.dungeon_set_medium,
        SetType.Heavy: dungeon.dungeon_set_heavy,
    }
    return DUNGEON_SETS[switch.get(set_type)]
