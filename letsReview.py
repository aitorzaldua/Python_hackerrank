import math
import os
import random
import re
import sys

class Separator:
    def __init__(self, Ty):
        self.numberCases = Ty
        self.classString = ""
        self.listOfClassString = []
        self.evenList = []
        self.oddList = []
        self.indexList = 0
        self.joinDigitsEven = ""
        self.joinDigitsOdd = ""



    def printString(self):

        for i in self.classString:
            self.listOfClassString.append (i)

        for j in self.listOfClassString:

            if self.listOfClassString.index(j) % 2 == 0:
                self.evenList.append (j)
            else:
                self.oddList.append (j)

        self.joinDigitsEven = ''.join(map(str,self.evenList))
        self.joinDigitsOdd = ''.join(map(str,self.oddList))

        print (self.joinDigitsEven, self.joinDigitsOdd)

        self.classString = ""
        self.listOfClassString = []
        self.evenList = []
        self.oddList = []




    def testCase (self):

        while  self.indexList <  self.numberCases:
            self.classString = input('Introduce el string: ')
            self.printString()
            self.indexList += 1




if __name__ == '__main__':
    T = int(input ('number of test case: '))

    p = Separator (T)

    p.testCase()




