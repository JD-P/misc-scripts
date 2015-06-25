# Binary search a tuple/array of integers according to a list of numbers given 
# on the command line.

import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "csv_list",
        default=(0,1,2,3,4,5,6,7,8,9,10),
        help="A comma seperated list of values.")
    parser.add_argument(
        "search_target",
        default=7,
        help="The integer to search for in the given list.")
    arguments = parser.parse_args()
    restrictions = re.compile("[^[0-9,]+")
    if restrictions.search(arguments.csv_list):
        print("ERROR: Comma seperated list given incorrectly on cmd line.")
        return False
    else:
        parsed_ints = arguments.csv_list.split(",")
        while '' in parsed_ints:
            integers.remove('')
        integers = list()
        for int_string in parsed_ints:
            integers.append(int(int_string))
        target = int(arguments.search_target)
        integers.sort()
        print(binary_search(target, integers))
        return True
            
def binary_search(integer, integers):
    """Takes a target search integer to pull from an array of given integers. 
    If target integer is not in array returns False."""
    while 1:
        mid = len(integers) / 2
        if len(integers) == 1:
            if integer == integers[0]:
                return integer
            else:
                return False
        elif isinstance(mid, float):
            middle = integers[round(mid)]
            if integer == middle:
                return integer
            elif integer > middle:
                integers = integers[round(mid) + 1:]
            else:
                integers = integers[:round(mid) - 1]
        else: 
            middle = integers[mid] + .5
            if integer == integers[middle - (middle % 1)]:
                return integer
            elif integer == integers[round(middle)]:
                return integer
            elif integer > middle:
                integers = integers[round(middle) + 1:]
            else:
                integers = integers[:middle - (middle % 1) - 1]

if __name__ == '__main__':            
    main()
