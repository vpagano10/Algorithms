#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=None):
    if cache is None:
        cache = [0] * (amount + 1)
        cache[0] = 1
    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            difference = higher_amount - coin
            cache[higher_amount] += cache[difference]
    return cache[amount]


# def greedy_change(change):
#     coins = (25, 10, 5, 1)
#     count = 0
#     for coin in coins:
#         while coin < change:
#             change -= coin
#             count += 1
#     return count
# print(greedy_change(22))


# To get optimal number of coins
# def change_matrix(coin_set, change_amount):
#     matrix = [[0 for m in range(change_amount+1)]
#               for m in range(len(coin_set)+1)]
#     for i in range(change_amount+1):
#         matrix[0][i] = i
#     return matrix
# def change_making(coins, change):
#     matrix = change_matrix(coins, change)
#     for c in range(1, len(coins)+1):
#         for r in range(1, change+1):
#             if coins[c-1] == r:
#                 matrix[c][r] = 1
#             elif coins[c-1] > r:
#                 matrix[c][r] = matrix[c-1][r]
#             else:
#                 matrix[c][r] = min(matrix[c-1][r], 1+matrix[c][r-coins[c-1]])
#     return matrix[-1][-1]
# print(change_making([1, 5, 10, 25], 32))


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
