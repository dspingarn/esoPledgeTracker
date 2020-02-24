import argparse
from ept_functions import handle_list, handle_next, handle_date

parser = argparse.ArgumentParser(
    prog="ESO Pledge Tracker",
    description=
    "A simple CLI program to print information about Undaunted Pledges in ESO")

# optional arguments have a dash in the argument name
parser.add_argument(
    "-d",
    "--date",
    type=int,
    help=
    "The default command if none are specified. Print the dungeons for <days> before or after today's date (e.g. -1 is yesterday, 1 is tomorrow). If no arguments are specified, default to the current date",
    default=0,
    metavar="<days>")
parser.add_argument(
    "-l",
    "--list",
    help=
    "List all of the undaunted pledges (and their dungeon sets with verbose), starting with the current dungeon for each cycle",
    action="store_true")
parser.add_argument("-v",
                    "--verbose",
                    help="Make the output more verbose",
                    action="store_true")
parser.add_argument(
    "-n",
    "--next",
    help="Get the next time a dungeon or dungeon set is available",
    metavar="<query>")
# added for the fun of it, version numbers are currently meaningless
parser.add_argument("--version", action="version", version="%(prog)s 1.1")
parser.add_argument(
    "--debug",
    action="store_true",
    help="Print the argument parser's argv values for debugging purposes")

# if --help or --version are chosen, they will take precedence over all else and the program will terminate after handling them
args = parser.parse_args()
if (args.debug):
    print(vars(args))

if args.list:
    handle_list(args.verbose)
elif args.next:
    handle_next(args.next, args.verbose)
else:
    handle_date(args.date, args.verbose)
