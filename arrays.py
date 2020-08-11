#mensaje borrar

import math
import os
import random
import re
import sys

def arrayMethod (arrNew):

    arrNew.reverse()
    print (' '.join(map(str,arrNew)))


if __name__ == '__main__':

    arr = [1, 2, 3, 4]

    arrayMethod (arr)