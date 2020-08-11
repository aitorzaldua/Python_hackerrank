import math
import os
import random
import re
import sys

def dicAndMaps (cases):
    phoneBook = {}
    keyList = []
    for i in range (cases):

        names = input ('introduce un nombre: ')
        phones = input ('introduce el telefono: ')
        phoneBook.update ({names:phones})


    for i in range (cases):
        key = input ('introduce los check: ')
        keyList.append(key)

    for i in keyList:
        if i in phoneBook:
            print ("{}={}".format(i, phoneBook[i]))
        else:
            print ('Not found')




if __name__ == '__main__':

    n = int(input('introduce el numero de ejemplos: '))
    dicAndMaps(n)


