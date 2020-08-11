
#cabecera

import math
import os
import random
import re
import sys

def compareTriplets (a, b):

    rsult = [0,0]
    i = 0

    while i <  len (a) - 1:

        for element in a:
            if a[i] > b[i]:

                rsult[0] = rsult[0] + 1

            elif a[i] < b[i]:


                rsult[1] = rsult[1] + 1

            i += 1

    return rsult


#footer

if __name__ == '__main__':
    a = [17, 28, 30]
    b = [99, 16, 8]

    print (compareTriplets (a,b))


