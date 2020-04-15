#!/usr/bin/python

import argparse


# Kind of works but doesn not restrict the min value to come before the max value
def find_max_profit(prices):
    # get maximum in list
    max_price = prices[1]
    curr_max = max_price
    for price in prices:
        if price > curr_max:
            curr_max = price
    # get min_price in list, but must come before the max_price
    min_price = prices[0]
    curr_min = min_price
    while prices.index(curr_min) < prices.index(curr_max):
        for price in prices:
            if price < curr_min:
                curr_min = price
    # subtract min_price from max_price
    result = curr_max - curr_min
    return result


# ATTEMPT 2
# def find_max_profit(prices):
    # if less than 1 return -1 or something to indicate nothing available
    # variable to find profit (subtract min for max) set min then max is min+1 by indexing prices array
    # for items in the range of the prices array length
    # make a new variable that checks the item + 1
    # while that new variable is less than the prices array length
    # make another profit checking variable that subs the new var index - item index
    # if the new profit checker is now bigger than first max profit check, set it
    # increase then item+1 variable by 1 to continue moving through the array
    # return the reuslts for the max profit
    # pass


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
