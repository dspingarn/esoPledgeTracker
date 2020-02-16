import argparse
import dungeon_data
from ept_functions import handle_list, handle_date

parser = argparse.ArgumentParser(
    prog="ESO Pledge Tracker",
    description=
    "A simple CLI program to print information about Undaunted Pledges in ESO")

# optional arguments have a dash in the argument name
parser.add_argument(
    "-d",
    "--date_shift",
    type=int,
    help=
    "Print the dungeons for `[NUM_DAYS]` before or after today's date (e.g. -1 is yesterday, 1 is tomorrow). If no arguments are specified when running the script, default to the current date",
    default=0,
    metavar="[NUM_DAYS]")
parser.add_argument(
    "-l",
    "--list",
    help=
    "List all of the undaunted pledges (and their dungeon sets with verbose).",
    action="store_true")
parser.add_argument("-v",
                    "--verbose",
                    help="Make the output more verbose",
                    action="store_true")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

# if --help or --version are chosen, they will take precedence over --list and --date_shift and the program will terminate after handling them
args = parser.parse_args()
print(vars(args))

if args.list == False:
    handle_date(args.verbose, args.date_shift)

else:
    handle_list(args.verbose)
