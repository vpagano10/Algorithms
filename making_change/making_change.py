#!/usr/bin/python

import sys


def making_change(amount, denominations):
    pass


# def greedy_change(change):
#     coins = (25, 10, 5, 1)
#     count = 0
#     for coin in coins:
#         while coin < change:
#             change -= coin
#             count += 1
#     return count
# print(greedy_change(22))


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
