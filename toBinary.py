import math
import os
import random
import re
import sys

def toBinary(number):
    binaryN = (''.join(str(1 & int(number) >> i) for i in range(64)[::-1]) + '0')
    print (binaryN)
    counterMax = 0
    counterOnes = 1
    for i in range (len(binaryN)-1):
        if binaryN[i] == "1" and binaryN[i+1]== "1":
            # print (i,binaryN[i] )
            counterOnes = int(binaryN[i]) + int(binaryN[i+1]) + 1
        else:
            if counterOnes > counterMax:
                    counterMax = counterOnes
                    counterOnes = 1


    print (counterMax)



if __name__ == '__main__':
    n = int(input("numero:  "))

toBinary(n)