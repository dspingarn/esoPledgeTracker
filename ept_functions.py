# functions for handling CLI arguments

from dungeon_data import DUNGEONS_MAJ, DUNGEONS_GLI, DUNGEONS_URG
import time


def __get_cycle_index():
    # 02/12/2020 at 06:00:00 UTC, or 01:00:00 EST, because that's when this was first written
    CYCLE_START_TIMESTAMP = 1581487200
    CURRENT_TIMESTAMP = time.time()
    ELAPSED_TIME = CURRENT_TIMESTAMP - CYCLE_START_TIMESTAMP
    SECONDS_PER_DAY = 86400
    ELAPSED_DAYS = int(ELAPSED_TIME / SECONDS_PER_DAY)
    return ELAPSED_DAYS


def __get_full_dungeon_list(dungeons):
    DUNGEON_LIST = []
    DUNGEONS_LENGTH = len(dungeons)
    CURRENT_INDEX = __get_cycle_index() % DUNGEONS_LENGTH
    for i in range(DUNGEONS_LENGTH):
        DUNGEON_LIST.append(dungeons[(i + CURRENT_INDEX) % DUNGEONS_LENGTH])
    return DUNGEON_LIST


def __get_dungeon_names(dungeons):
    DUNGEON_LIST = []
    DUNGEONS_LENGTH = len(dungeons)
    CURRENT_INDEX = __get_cycle_index() % DUNGEONS_LENGTH
    for i in range(DUNGEONS_LENGTH):
        DUNGEON_LIST.append(dungeons[(i + CURRENT_INDEX) %
                                     DUNGEONS_LENGTH].name)
    return DUNGEON_LIST


def handle_list(isVerbose):
    print("The dungeon cycle for Maj al-Ragath is:\n")
    if isVerbose:
        for d in __get_full_dungeon_list(DUNGEONS_MAJ):
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))
    else:
        print(', '.join(__get_dungeon_names(DUNGEONS_MAJ)))
    print("\nThe dungeon cycle for Glirion the Redbeard is:\n")
    if isVerbose:
        for d in __get_full_dungeon_list(DUNGEONS_GLI):
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))
    else:
        print(', '.join(__get_dungeon_names(DUNGEONS_GLI)))
    print("\nThe dungeon cycle for Urgarlag Chief-bane is:\n")
    if isVerbose:
        for d in __get_full_dungeon_list(DUNGEONS_URG):
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))
    else:
        print(', '.join(__get_dungeon_names(DUNGEONS_URG)))


def handle_date(isVerbose, shift):
    REG_DUNGEON_INDEX = (__get_cycle_index() + shift) % len(DUNGEONS_MAJ)
    DLC_ARRAY_INDEX = (__get_cycle_index() + shift) % len(DUNGEONS_URG)

    if (shift == 0):
        MESSAGE, TENSE = "Today's", "are"
    elif (shift > 0):
        MESSAGE = "In {} days, the".format(
            shift) if shift != 1 else "Tomorrow's"
        TENSE = "will be"
    elif (shift < 0):
        MESSAGE = "{} days ago, the".format(
            (shift * -1)) if shift != -1 else "Yesterday's"
        TENSE = "were"

    if isVerbose:
        print("{} Undaunted Pledges {}:\n".format(MESSAGE, TENSE))
        DUNGEONS = [
            DUNGEONS_MAJ[REG_DUNGEON_INDEX], DUNGEONS_GLI[REG_DUNGEON_INDEX],
            DUNGEONS_URG[DLC_ARRAY_INDEX]
        ]
        for d in DUNGEONS:
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))

    else:
        print("{} Undaunted Pledges {}: {}, {}, and {}".format(
            MESSAGE, TENSE, DUNGEONS_MAJ[REG_DUNGEON_INDEX].name,
            DUNGEONS_GLI[REG_DUNGEON_INDEX].name,
            DUNGEONS_URG[DLC_ARRAY_INDEX].name))
