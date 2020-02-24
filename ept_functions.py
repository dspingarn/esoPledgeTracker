# functions for handling CLI arguments

from dungeon_data import DUNGEONS_MAJ, DUNGEONS_GLI, DUNGEONS_URG
import time


def _get_cycle_index(shift, list_length):
    # 02/12/2020 at 06:00:00 UTC, or 01:00:00 EST, because that's when this was first written
    cycle_start_timestamp = 1581487200
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
    for d in dungeon_list:
        print(
            "{}\nMonster Helm Set : {}\nLight Armor Set  : {}\nMedium Armor Set : {}\nHeavy Armor Set  : {}\n"
            .format(d.name, d.weapon_set_unique, d.weapon_set_light,
                    d.weapon_set_medium, d.weapon_set_heavy))


def handle_list(is_verbose):
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
    for d in dungeon_list:
        search_list = [
            d.name.lower(),
            d.weapon_set_unique.lower(),
            d.weapon_set_light.lower(),
            d.weapon_set_medium.lower(),
            d.weapon_set_heavy.lower()
        ]
        if [i for i in search_list if query.lower() in i]:
            res.append(d)
    return res


def _get_dungeon_index_in_list(dungeon_name, dungeon_list):
    for i in range(len(dungeon_list)):
        if dungeon_list[i].name == dungeon_name:
            return i
    return -1


def _print_next_results(results, dungeon_list, query, verbose):
    did_print = 0
    for r in results:
        index = _get_dungeon_index_in_list(r.name, dungeon_list)
        if index == 0:
            print("Query \"{}\" matched with {}, which is happening today.".
                  format(query, r.name))
            did_print = 1
        elif index != -1:
            print(
                "Query \"{}\" matched with the dungeon \"{}\", which will happen in {} days"
                .format(query, r.name, index))
            did_print = 1
        if verbose and index != -1:
            _print_list_verbose([r])
    return did_print


def handle_next(query, is_verbose):
    if len(query) < 3 or query.lower() == "the":
        print("Query not unique enough. Please use a different string.")
        return
    maj_results = _find_dungeons_that_match_query(query, DUNGEONS_MAJ)
    gli_results = _find_dungeons_that_match_query(query, DUNGEONS_GLI)
    urg_results = _find_dungeons_that_match_query(query, DUNGEONS_URG)
    did_print = 0
    if _print_next_results(maj_results, _get_dungeons_sorted(DUNGEONS_MAJ),
                           query, is_verbose) == 1:
        did_print = 1
    if _print_next_results(gli_results, _get_dungeons_sorted(DUNGEONS_GLI),
                           query, is_verbose) == 1:
        did_print = 1
    if _print_next_results(urg_results, _get_dungeons_sorted(DUNGEONS_URG),
                           query, is_verbose) == 1:
        did_print = 1
    if did_print == 0:
        print("Query \"{}\" returned no results.".format(query))


def handle_date(shift, is_verbose):
    reg_dungeon_index = _get_cycle_index(shift, len(DUNGEONS_MAJ))
    dlc_array_index = _get_cycle_index(shift, len(DUNGEONS_URG))

    if (shift == 0):
        message, tense = "Today's", "are"
    elif (shift > 0):
        message = "In {} days, the".format(
            shift) if shift != 1 else "Tomorrow's"
        tense = "will be"
    elif (shift < 0):
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
