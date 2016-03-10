# -*-coding:utf-8 -*-
__author__ = "philipchang"
__date__   = "2016-01-22"

import sys
import math
import pandas as pd
import numpy as np
import random

print "let we go to the python world"

#print pd.DataFrame();

N = 5
ind = np.arange(N)
print ind

series_obj = pd.Series([4,7,-5,3], index=['a','b','c','d'])
print series_obj


def jugdescore(x):
    
    if x > 100 :
        print "other invalid score"
    elif x > 89 :
        print "A"
    elif x > 79 :
        print "B"
    elif x > 69 :
        print "C"
    elif x > -1 :
        print "D"
    else:
        print "other invalid score"
        
for i in xrange(0,0):
    score = raw_input()
    if score.isdigit() :
        jugdescore(int(score))
    else:
        print "invalid argument, please input the interge num"
            
def myabs(x):
    if x > 0:
        return x
    else:
        return -x

#'''
x = random.randint(0,25)
print "please input a number between [0,25]"
#while 1 :
for count in range(0,10):
    digit = input()
    if digit == x :
        print "bingo!"
        break
    elif digit > x :
        print "too large, please try it again"
    else :
        print "too small, please try it again"
#  '''      
print "end"
        




