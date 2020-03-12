"""Functions for handling CLI arguments"""

import time
from .dungeon_data import DUNGEONS_MAJ, DUNGEONS_GLI, DUNGEONS_URG


def _get_cycle_index(shift, list_length):
    # 02/24/2020 at 06:00:00 UTC, or 01:00:00 EST, corresponding to patch 25 (Harrowstorm)
    cycle_start_timestamp = 1582524000
    current_timestamp = time.time()
    elapsed_time = current_timestamp - cycle_start_timestamp
    seconds_per_day = 86400
    elapsed_days = int(elapsed_time / seconds_per_day) + shift
    return elapsed_days % list_length


def _get_dungeons_sorted(dungeon_list):
    sorted_list = []
    dungeons_length = len(dungeon_list)
    current_index = _get_cycle_index(0, dungeons_length)
    for i in range(dungeons_length):
        sorted_list.append(dungeon_list[(i + current_index) % dungeons_length])
    return sorted_list


def _print_list_verbose(dungeon_list):
    for dungeon in dungeon_list:
        print(
            ("{}\nMonster Helm Set : {}\nLight Armor Set  : {}\n"
             "Medium Armor Set : {}\nHeavy Armor Set  : {}\n").format(
                 dungeon.name, dungeon.monster_set, dungeon.dungeon_set_light,
                 dungeon.dungeon_set_medium, dungeon.dungeon_set_heavy))


def handle_list(is_verbose):
    """Handle -l argument to list the dungeon cycles"""
    dungeons_maj_sorted = _get_dungeons_sorted(DUNGEONS_MAJ)
    print("The dungeon cycle for Maj al-Ragath is:\n")
    if is_verbose:
        _print_list_verbose(dungeons_maj_sorted)
    else:
        print(', '.join([d.name for d in dungeons_maj_sorted]))
    dungeons_gli_sorted = _get_dungeons_sorted(DUNGEONS_GLI)
    print("\nThe dungeon cycle for Glirion the Redbeard is:\n")
    if is_verbose:
        _print_list_verbose(dungeons_gli_sorted)
    else:
        print(', '.join([d.name for d in dungeons_gli_sorted]))
    dungeons_urg_sorted = _get_dungeons_sorted(DUNGEONS_URG)
    print("\nThe dungeon cycle for Urgarlag Chief-bane is:\n")
    if is_verbose:
        _print_list_verbose(dungeons_urg_sorted)
    else:
        print(', '.join([d.name for d in dungeons_urg_sorted]))


def _find_dungeons_that_match_query(query, dungeon_list):
    search_list = []
    res = []
    for dungeon in dungeon_list:
        search_list = [
            dungeon.name.lower(),
            dungeon.monster_set.lower(),
            dungeon.dungeon_set_light.lower(),
            dungeon.dungeon_set_medium.lower(),
            dungeon.dungeon_set_heavy.lower()
        ]
        if [i for i in search_list if query.lower() in i]:
            res.append(dungeon)
    return res


def _get_dungeon_index_in_list(dungeon_name, dungeon_list):
    for i, item in enumerate(dungeon_list):
        if item.name == dungeon_name:
            return i
    return -1


def _print_next_results(results, dungeon_list, query, verbose):
    did_print = 0
    for result in results:
        index = _get_dungeon_index_in_list(result.name, dungeon_list)
        if index == 0:
            print("Query \"{}\" matched with {}, which is happening today.".
                  format(query, result.name))
            did_print = 1
        elif index != -1:
            print(
                "Query \"{}\" matched with {}, which will happen in {} days.".
                format(query, result.name, index))
            did_print = 1
        if verbose and index != -1:
            _print_list_verbose([result])
    return did_print


def handle_next(query, is_verbose):
    """Handle -n argument to search for next occurence of a dungeon matching a given string"""
    if len(query) < 3 or query.lower() == "the":
        print("Query not unique enough. Please use a different string.")
        return
    maj_results = _find_dungeons_that_match_query(query, DUNGEONS_MAJ)
    gli_results = _find_dungeons_that_match_query(query, DUNGEONS_GLI)
    urg_results = _find_dungeons_that_match_query(query, DUNGEONS_URG)
    did_print = 0
    if _print_next_results(maj_results, _get_dungeons_sorted(DUNGEONS_MAJ),
                           query, is_verbose):
        did_print = 1
    if _print_next_results(gli_results, _get_dungeons_sorted(DUNGEONS_GLI),
                           query, is_verbose):
        did_print = 1
    if _print_next_results(urg_results, _get_dungeons_sorted(DUNGEONS_URG),
                           query, is_verbose):
        did_print = 1
    if did_print == 0:
        print("Query \"{}\" returned no results.".format(query))


def handle_date(shift, is_verbose):
    """Handle -d argument to get the dungeons for a given date"""
    reg_dungeon_index = _get_cycle_index(shift, len(DUNGEONS_MAJ))
    dlc_array_index = _get_cycle_index(shift, len(DUNGEONS_URG))

    if shift == 0:
        message, tense = "Today's", "are"
    elif shift > 0:
        message = "In {} days, the".format(
            shift) if shift != 1 else "Tomorrow's"
        tense = "will be"
    elif shift < 0:
        message = "{} days ago, the".format(
            (shift * -1)) if shift != -1 else "Yesterday's"
        tense = "were"

    if is_verbose:
        print("{} Undaunted Pledges {}:\n".format(message, tense))
        dungeon_selection = [
            DUNGEONS_MAJ[reg_dungeon_index], DUNGEONS_GLI[reg_dungeon_index],
            DUNGEONS_URG[dlc_array_index]
        ]
        _print_list_verbose(dungeon_selection)

    else:
        print("{} Undaunted Pledges {}: {}, {}, and {}".format(
            message, tense, DUNGEONS_MAJ[reg_dungeon_index].name,
            DUNGEONS_GLI[reg_dungeon_index].name,
            DUNGEONS_URG[dlc_array_index].name))
