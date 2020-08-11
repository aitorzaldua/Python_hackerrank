import math
import os
import random
import re
import sys

def conditionalSt (N):
    if (N % 2) != 0:
        print ('Weird')
    else:
        if 2 <= N <= 5:
            print ('Not Weird')
        elif 6 <= N <= 20:
           print ('Weird')
        else:
           print ('Not Weird')






if __name__ == '__main__':
    conditionalSt(3)
    conditionalSt(24)



