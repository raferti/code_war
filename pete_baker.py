"""

Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths. Can you help him to find out,
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available
ingredients (also an object) and returns the maximum number of cakes Pete
can bake (integer). For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}

"""


# solution 1
def cakes(recipe, available):
    count_cakes = []
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        else:
            count = available[ingredient] // recipe[ingredient]
            if count < 0:
                return 0
            else:
                count_cakes.append(count)
    return min(count_cakes)



# solution 2
def cakes_two(recipe, available):
    return min(available.get(k, 0) // recipe[k] for k in recipe)
