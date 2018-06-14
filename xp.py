import numpy as np
import os
import logging
import re

logger = logging.getLogger(__name__)


class RegExError(Exception):
    pass


def read_csv(path):
    return np.genfromtxt(path, delimiter=',')


def verify_level(lvl):
    if re.match("20|[$1]?[0-9]$", lvl) is None:
        raise RegExError


def verify_input(lvls):
    try:
        spl = lvls.split(",")
        for lvl in spl:
            verify_level(lvl)
        return True
    except RegExError:
        print("\nERROR: Please enter levels in a comma separated string (ex: 11,3,5,8)\n")
        return False


def main():
    xp_list = read_csv(os.path.join("xp.csv"))

    running = True
    while running:
        lvls = input("Please enter levels as comma seperated list (ex: 2,3,4,5): ")
        if lvls in ["q", "quit", "exit", "0"]:
            running = False
            break

        if not verify_input(lvls):
            continue

        lvls = list(map(int, lvls.split(",")))
        lvls = [x - 1 for x in lvls] # index and level

        diff = xp_list[lvls]

        print("The combat difficulties are: ")

        diff_sum = np.sum(diff, axis=0)
        print(diff_sum)
        print("")

        print("Individual Player Difficulties: ")
        print(diff)
        running = False


if __name__ == "__main__":
    main()
