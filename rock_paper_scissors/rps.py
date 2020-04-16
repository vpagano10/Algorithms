#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # variable results is an array
    game_results = []
    # variable options that holds the available options
    available_moves = ("rock", "paper", "scissors")
    # internal helper function that takes in original param and an array to collect the results that are then passed to results

    def rps_helper(n, result_collector):
        # if there are results...
        if result_collector >= 1:
            # for each option, set it to a variable
            for move in result_collector:
                result_collector.append(move)
                # recurse the helper func, adding the option into the helper array
                rps_helper(n, result_collector)
                # call helper function then return results
        # else, no entries, add new empty array into results
        else:
            game_results = result_collector
        return game_results
    return game_results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
