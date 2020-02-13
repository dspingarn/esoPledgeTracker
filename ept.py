import argparse, time

parser = argparse.ArgumentParser(
    description="prints the undaunted pledges for the day")

# optional because it has a dash in the argument name
parser.add_argument(
    "-d",
    type=int,
    help=
    "Use -d N where N is a number of days before or after today (-1 is yesterday, 1 is tomorrow, etc.). If no arguments are specified when running the script, then we assume -d 0 (i.e. today).",
    default=0,
    metavar='N')
parser.add_argument(
    "-p",
    help=
    "Does absolutely nothing at all. I'll implement this in a future update.")

args = parser.parse_args()

if (args.d != 0):
    print("Days argument was {}".format(args.d))
    SHIFT = args.d

if (args.p != None):
    print("Useless argument -p was {}".format(args.p))

if (args.d == 0):
    print("Getting pledges for today.")
    SHIFT = 0

pledges_MAJ = [
    "Fungal Grotto I", "Banished Cells II", "Darkshade Caverns I",
    "Elden Hollow II", "Wayrest Sewers I", "Spindleclutch II",
    "Banished Cells I", "Fungal Grotto II", "Spindleclutch I",
    "Darkshade Caverns II", "Elden Hollow I", "Wayrest Sewers II"
]

pledges_GLI = [
    "Selene's Web", "City of Ash II", "Crypt of Hearts I", "Volenfell",
    "Blessed Crucible", "Direfrost Keep", "Vaults of Madness",
    "Crypts of Hearts II", "City of Ash I", "Tempest Island",
    "Blackheart Haven", "Arx Corinium"
]

pledges_URG = [
    "Fang Lair", "Scalecaller Peak", "Moon Hunter Peak", "March of Sacrifices",
    "Depths of Malatar", "Frostvault", "Moongrave Fane", "Lair of Maarselok",
    "Imperial City Prison", "Ruins of Mazzatun", "White-Gold Tower",
    "Cradle of Shadows", "Bloodroot Forge", "Falkreath Hold"
]

# 02/12/2020 at 06:00:00 UTC, or 01:00:00 EST, because that's when this was first written
CYCLE_START_TIMESTAMP = 1581487200


def getCycleIndex():
    CURRENT_TIMESTAMP = time.time()
    ELAPSED_TIME = CURRENT_TIMESTAMP - CYCLE_START_TIMESTAMP
    SECONDS_PER_DAY = 86400
    ELAPSED_DAYS = int(ELAPSED_TIME / SECONDS_PER_DAY)
    return ELAPSED_DAYS


REG_DUNGEON_INDEX = (getCycleIndex() + SHIFT) % len(pledges_MAJ)
DLC_ARRAY_INDEX = (getCycleIndex() + SHIFT) % len(pledges_URG)

print("Today's undaunted pledges are {}, {}, and {}.".format(
    pledges_MAJ[REG_DUNGEON_INDEX], pledges_GLI[REG_DUNGEON_INDEX],
    pledges_URG[DLC_ARRAY_INDEX]))
