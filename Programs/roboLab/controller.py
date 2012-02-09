#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose : 1st assignment in Artificial Intelligence
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Thu  9 Feb 2012 19:00:43 EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys

from inparser import parseInput
from astar import astar
import heuristics
from grids import flushgrid,printpath,designpath,modifygrid
#import psyco

#psyco.full()

def main():
    if len(sys.argv) < 3:
        print "Usage: %s <inputfile> <mode (A/N)>" %sys.argv[0]
        return -1
    f=open(sys.argv[1],"r")
    (target,r1,r2,field) = parseInput(f)
    f.close()
    if sys.argv[2] == "A":
        print "Using Manhattan Distance as admissible heuristic"
        heuristic = heuristics.manhattanDist
    elif sys.argv[2] == "N":
        print "Using Square Distances as non-admissible heuristic"
        heuristic = heuristics.squaredDist
    else:
        print "Wrong mode, choose A for admissible heuristic or N for non-admissible"
        return -1
    finalists1 = astar(r1,target,field,heuristic)
    field = modifygrid(finalists1,field)
    finalists2 = astar(r2,target,field,heuristic)
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()
    print "Max length in steps:", max(len(finalists1),len(finalists2))
    print "finalists 1 len: ", len(finalists1)
    print "finalists 2 len: ", len(finalists2)

if __name__=="__main__":
    main()
