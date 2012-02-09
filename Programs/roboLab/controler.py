#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose : 1st assignment in Artificial Intelligence
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Thu 09 Feb 2012 06:51:57 PM EET
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
    if len(sys.argv) == 1:
        print "Usage: %s <inputfile>" %sys.argv[0]
        return -1
    f=open(sys.argv[1],"r")
    (target,r1,r2,field) = parseInput(f)
    f.close()
    finalists1 = astar(r1,target,field,heuristics.manhattanDist)
    field = modifygrid(finalists1,field)
    finalists2 = astar(r2,target,field,heuristics.manhattanDist)
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()

if __name__=="__main__":
    main()
