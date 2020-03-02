# ESO Pledge Tracker

### \* Up to date as of Patch 25 (Harrowstorm) \*

A simple CLI program to find out what the Undaunted Pledges are without logging into ESO.  
For some reason, ESO doesn't have any APIs (as far as I can tell) that lets me get that information automatically so we're literally hard-coding the sequence of dungeons on rotation for each NPC quest giver.  
Therefore, every time a new dungeon is added, this will have to be updated. Joy.

Do add-ons already exist in-game to get this information? Probably, yeah. But the point is to _not_ log into the game to know this info. Because I'm lazy.

## Requirements

- Python 3

## Running This Project
Assuming you're in the project root:

`python eso_pledge_tracker/ept.py [-h] [-d <days>] [-l] [-v] [-n <query>] [--version] [--debug]`

# Running the Tests
This project uses unittest, so feel free to run with whatever arguments you like.  
NOTE: Due to python issues (unless I goofed somewhere) you need to add eso_pledge_tracker and tests to your PYTHONPATH. I do this with a shell script (PYTHONPATH = ...)

`python -m unittest`

## Command Line Arguments

| Argument | Description |
| --- | --- |
| `-d <days>` | Print the dungeons for `days` before or after today's date<br>If no arguments are specified, or no flags are specified, default to this function and assume the current date |
| `-n <query>` | Searches for any dungeons containing `query` or with an item set with `query` in it, case-insensitive, and prints when the dungeon is happening next<br>If multiple words are required for the query, be sure to surround them with quotation marks |
| `-l, --list`     | List all of the undaunted pledges, starting with the current dungeon |
| `-v, --verbose`  | Make the output more verbose (i.e. list the dungeon sets for each dungeon) |
| `-h, --help`     | Show the help message and exit |
| `--version`      | Show program's version number and exit |
| `--debug`        | Print the argument parser's argv values for debugging purposes |

## File Structure

```
esoPledgeTracker/
    eso_pledge_tracker/
        dungeon_data.py
        dungeon_set_data.py
        dungeon_set.py
        dungeon.py
        ept_functions.py
        ept.py
    tests/
        __init__.py
        test_dungeon_set.py
        test_dungeon.py
        test_ept_functions.py
        test_parser.py
    ...
```
