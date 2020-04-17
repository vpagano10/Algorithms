#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # variable results is an array
    game_results = []
    # variable options that holds the available options
    available_moves = ("rock", "paper", "scissors")
    # internal helper function that takes in original param and an array to collect the results that are then passed to results

    def rps_helper(n, result_collector):
        if n == 0:
            game_results.append(result_collector)
            return
        else:
            for move in range(len(available_moves)):
                move = available_moves[move]
                rps_helper(n-1, result_collector + [move])

    rps_helper(n, [])
    return game_results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
