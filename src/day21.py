from util import *
from collections import *
import copy

day = 21


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    potential_ingredients = defaultdict(set)
    all_ingredients = set()
    all_allergens = set()
    rules = []

    for line in data:
        ingredients, allergens = line.split(" (")
        ingredients = ingredients.split(" ")
        allergens = allergens[:-1].split("contains ")[1].split(", ")
        all_ingredients = all_ingredients.union(ingredients)
        all_allergens = all_allergens.union(allergens)
        rules.append((ingredients, allergens))

    for al in all_allergens:
        potential_ingredients[al] = all_ingredients

    change = True
    while change:
        change = False
        for ingredients, allergens in rules:
            for allergen in allergens:
                existing = potential_ingredients[allergen]
                new = existing.intersection(ingredients)
                if new != existing:
                    change = True
                    potential_ingredients[allergen] = new

    no_allergens = []
    for el in all_ingredients:
        if all(el not in x for x in potential_ingredients.values()):
            no_allergens.append(el)

    ans = 0
    for rule in rules:
        for el in no_allergens:
            if el in rule[0]:
                ans += 1
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    potential_ingredients = defaultdict(set)
    all_ingredients = set()
    all_allergens = set()
    rules = []

    for line in data:
        ingredients, allergens = line.split(" (")
        ingredients = ingredients.split(" ")
        allergens = allergens[:-1].split("contains ")[1].split(", ")
        all_ingredients = all_ingredients.union(ingredients)
        all_allergens = all_allergens.union(allergens)
        rules.append((ingredients, allergens))

    for al in all_allergens:
        potential_ingredients[al] = all_ingredients

    change = True
    while change:
        change = False
        for ingredients, allergens in rules:
            for allergen in allergens:
                existing = potential_ingredients[allergen]
                new = existing.intersection(ingredients)
                if new != existing:
                    change = True
                    potential_ingredients[allergen] = new

    change = True
    while change:
        change = False
        for al, ings in potential_ingredients.items():
            if len(ings) == 1:
                ingredient = list(ings)[0]
                for ings2 in potential_ingredients.values():
                    if ings != ings2 and ingredient in ings2:
                        ings2.remove(ingredient)
                        change = True

    items = sorted(potential_ingredients.items(), key=lambda x: x[0])
    ans = []
    for it in items:
        ans.append(list(it[1])[0])
    ans = ",".join(ans)
    print(ans)
    return ans


# task1()
task2()
