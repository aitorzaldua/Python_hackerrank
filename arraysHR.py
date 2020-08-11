#Dale la vuelta a un array

import math
import os
import random
import re
import sys

def arrayMethod (arrayToChange):
    print(" ".join(map(str, arr[::-1])))


if __name__ == '__main__':

    arr = [1, 2, 3, 4]

    arrayMethod (arr)