#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # variable results is an array
    # variable options that holds the available options
    # internal helper function that takes in original param and an array to collect the results that are then passed to results
    #   if no entries just add the new empty array into results and get out of function
    #   else for each option, set it to a variable and iterate through each one
    #   recurse the helper function, adding the option intot the helper array
    # call helper function then return results
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
