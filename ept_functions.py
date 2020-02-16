# functions for handling CLI arguments

import dungeon_data
import time


def handle_list(isVerbose):
    print("The dungeon cycle for Maj al-Ragath is:\n")
    if isVerbose:
        for d in dungeon_data.DUNGEONS_MAJ:
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))
    else:
        print(', '.join(dungeon_data.PLEDGES_LIGHT_MAJ))
    print("\nThe dungeon cycle for Glirion the Redbeard is:\n")
    if isVerbose:
        for d in dungeon_data.DUNGEONS_GLI:
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))
    else:
        print(', '.join(dungeon_data.PLEDGES_LIGHT_GLI))
    print("\nThe dungeon cycle for Urgarlag Chief-bane is:\n")
    if isVerbose:
        for d in dungeon_data.DUNGEONS_URG:
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))
    else:
        print(', '.join(dungeon_data.PLEDGES_LIGHT_URG))


def handle_date(isVerbose, shift):
    # 02/12/2020 at 06:00:00 UTC, or 01:00:00 EST, because that's when this was first written
    CYCLE_START_TIMESTAMP = 1581487200

    def getCycleIndex():
        CURRENT_TIMESTAMP = time.time()
        ELAPSED_TIME = CURRENT_TIMESTAMP - CYCLE_START_TIMESTAMP
        SECONDS_PER_DAY = 86400
        ELAPSED_DAYS = int(ELAPSED_TIME / SECONDS_PER_DAY)
        return ELAPSED_DAYS

    REG_DUNGEON_INDEX = (getCycleIndex() + shift) % len(
        dungeon_data.PLEDGES_LIGHT_MAJ)
    DLC_ARRAY_INDEX = (getCycleIndex() + shift) % len(
        dungeon_data.PLEDGES_LIGHT_URG)

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
            dungeon_data.DUNGEONS_MAJ[REG_DUNGEON_INDEX],
            dungeon_data.DUNGEONS_GLI[REG_DUNGEON_INDEX],
            dungeon_data.DUNGEONS_URG[DLC_ARRAY_INDEX]
        ]
        for d in DUNGEONS:
            print(
                "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
                .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                        d.weapon_set_medium, d.weapon_set_heavy))

    else:
        print("{} Undaunted Pledges {}: {}, {}, and {},".format(
            MESSAGE, TENSE, dungeon_data.PLEDGES_LIGHT_MAJ[REG_DUNGEON_INDEX],
            dungeon_data.PLEDGES_LIGHT_GLI[REG_DUNGEON_INDEX],
            dungeon_data.PLEDGES_LIGHT_URG[DLC_ARRAY_INDEX]))
