#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : inparser.py
#
#* Purpose : Input parsing of state space
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 11 Feb 2012 03:29:42 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#* Created By : Vasilis Gerakaris <vgerak@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import heuristics
from sys import argv,exit
def fieldTranslate(st):
    a=[]
    for i in st:
        #'X' marks obstacle, 'O' marks open space
        if i == 'X':
            a.append(-1)
        elif i=='O':
            a.append(0)
        else:
            print "Wrong input format"
            exit(-1)
    return a

def parseInput(f):
    lines = int(f.readline().split()[0])
    robo1_initstate = tuple(map(int,f.readline().split()))
    robo2_initstate = tuple(map(int,f.readline().split()))
    target = tuple(map(int,f.readline().split()))
    text = map(fieldTranslate,map(lambda x:x.strip(),f.readlines()))
    return (target,robo1_initstate,robo2_initstate,text)

def parseUser():
    if len(argv) < 3:
        print "Usage: %s <inputfile> <mode (A/N)>" %argv[0]
        exit(-1)
    modeCheck = argv[2]
    while modeCheck != "A" and modeCheck != "N" and modeCheck != "a" and modeCheck != "n":
        print "Wrong mode, choose A for admissible heuristic or N for non-admissible"
        modeCheck = raw_input('Enter A or N --->')
    if modeCheck == "A" or modeCheck == 'a':
        print "Using Manhattan Distance as admissible heuristic"
        heuristic = heuristics.manhattanDist
    else:
        print "Using Square Distances as non-admissible heuristic"
        heuristic = heuristics.squaredDist
    try:
        f=open(argv[1],"r")
    except IOError:
        print "The file you have entered does not exist"
        exit(-1)
    (target,r1,r2,initialfield) = parseInput(f)
    f.close()
    return (target,r1,r2,initialfield,heuristic)
