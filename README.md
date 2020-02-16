# ESO Pledge Tracker

A simple CLI program to find out what the undaunted pledges are without logging into ESO.  
For some reason, ESO doesn't have any APIs (as far as I can tell) that lets me get that information automatically so we're literally hard-coding the sequence of dungeons on rotation for each NPC quest giver.  
Therefore, every time a new dungeon is added, this will have to be updated. Joy.

Do add-ons already exist in-game to get this information? Probably yeah. But the point is to _not_ log into the game to know this info. Because I'm lazy.

## Requirements

- Python

## Command Line Arguments

| Argument                      | Description                                                                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-d, --date_shift [NUM_DAYS]` | Print the dungeons for `[NUM_DAYS]` before or after today's date <br> If no arguments are specified, or no flags are specified, assume the current date |
| `-l, --list`                  | List all of the undaunted pledges                                                                                                                       |
| `-v, --verbose`               | Make the output more verbose (i.e. list the dungeon sets for each dungeon)                                                                              |
| `-h, --help`                  | Show the help message and exit                                                                                                                          |
| `--version`                   | Show program's version number and exit                                                                                                                  |
