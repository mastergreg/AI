#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose : 1st assignment in Artificial Intelligence
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Wed  8 Feb 2012 22:34:56 EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys

from inparser import parseInput
from astar import astar
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
    finalists1 = astar(r1,target,field)
    #field = modifygrid(finalists1,field)
    finalists2 = astar(r2,target,field)
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()


if __name__=="__main__":
    main()
