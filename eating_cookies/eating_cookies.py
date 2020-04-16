#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# look at fibonacci sequence example using the cache but with a dict in the cache param
# the cache here is the base case, and it dynamically increases
def eating_cookies(n, cache={0: 1, 1: 1, 2: 2}):
    if n in cache:
        return cache[n]
    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]


# def cache_fib(n, cache=None):
#     if cache is None:
#         cache = {}
#     if n < 2:
#         return 1
#     if n in cache:
#         return cache[n]
#     else:
#         answer = cache_fib(n - 1, cache) + cache_fib(n - 2, cache)
#         cache[n] = answer
#         return answer

# ->

# def cache_fib(n, cache={0: 0, 1: 1}):
#     if n in cache:
#         return cache[n]
#     cache[n] = cache_fib(n - 1) + cache_fib(n - 2)
#     return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
