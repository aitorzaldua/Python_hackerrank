import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    tip_total = (meal_cost * tip_percent) / 100
    print (tip_total)

    tax_total = (meal_cost * tax_percent) / 100
    print (tax_total)

    total_cost = round(meal_cost + tip_total + tax_total)
    return (total_cost)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print (solve(meal_cost, tip_percent, tax_percent))
