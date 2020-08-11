
import math
import os
import random
import re
import sys

def loop (number):
    for i in range (1,11):
        multiply = number * i
        # print (f'{number} x {i} = {multiply}')
        print (number, " x ", i, " = ", multiply)


if __name__ == '__main__':

    n = int(input('introduce un numero: '))
    loop (n)