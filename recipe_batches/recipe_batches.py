#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # set a batches dictionary
    # set a variable for maximum batches to a high integer
    # for i in recipe
    # try batches at i = ingredients at i divided by recipe at i
    # catch maximum batches is 0
    # nested for i in values() of batches
    # if i greater than the maximum maximum is i then return
    pass


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
