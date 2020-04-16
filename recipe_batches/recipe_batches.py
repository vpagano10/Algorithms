#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = {}
    ingredient_check = 0
    total_possible_batches = 0
    if len(recipe) == len(ingredients):
        for i in recipe:
            batches[i] = ingredients[i] // recipe[i]
        print(batches)
        for i in batches:
            if batches[i] > 0:
                ingredient_check += 1
            if ingredient_check == len(recipe):
                min_batches = []
                for i in batches.values():
                    min_batches.append(i)
                print(min(min_batches))
                total_possible_batches = min(min_batches)
    return total_possible_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 10}
#     ingredients = {'milk': 198, 'butter': 52, 'flour': 10}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
