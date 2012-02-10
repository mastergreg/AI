#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose : 1st assignment in Artificial Intelligence
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Fri 10 Feb 2012 10:33:06 EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import sys

from inparser import parseInput
from astar import astar
import heuristics
from grids import flushgrid,printpath,designpath,modifygrid

def main():
    if len(sys.argv) < 3:
        print "Usage: %s <inputfile> <mode (A/N)>" %sys.argv[0]
        return -1
    f=open(sys.argv[1],"r")
    (target,r1,r2,field) = parseInput(f)
    f.close()
    modeCheck = sys.argv[2]
    while modeCheck != "A" and modeCheck != "N" and modeCheck != "a" and modeCheck != "n":
        print "Wrong mode, choose A for admissible heuristic or N for non-admissible"
        modeCheck = raw_input('Enter A or N --->')
    if modeCheck == "A" or modeCheck == 'a':
        print "Using Manhattan Distance as admissible heuristic"
        heuristic = heuristics.manhattanDist
    else:
        print "Using Square Distances as non-admissible heuristic"
        heuristic = heuristics.squaredDist
    print "\n======= Robot 2 plays 'nice' ======="
    finalists1 = astar(r1,target,field,heuristic)
    field = modifygrid(finalists1,field)
    finalists2 = astar(r2,target,field,heuristic)
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()
    max1 = max(len(finalists1),len(finalists2))
    print "Max length in steps:", max1-1
    print "\t Robot 1 took:\t\t", len(finalists1)-1, " steps"
    print "\t Robot 2 (nice) took:\t", len(finalists2)-1, " steps"
    flushgrid(field)
    print "\n======= Robot 1 plays 'nice' ======="
    finalists2 = astar(r2,target,field,heuristic)
    field = modifygrid(finalists2,field)
    finalists1 = astar(r1,target,field,heuristic)
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()
    max2 = max(len(finalists1),len(finalists2))
    print "Max length in steps:", max2-1
    print "\t Robot 1 (nice) took:\t", len(finalists1)-1, " steps"
    print "\t Robot 2 took:\t\t", len(finalists2)-1, " steps"
    print "\n ===== RESULT ====="
    if max1 < max2:
        print "1st strategy (Robot 2 plays nice) is optimal"
    elif max2 < max1:
        print "2nd strategy (Robot 1 plays nice) is optimal"
    else:
        print "Both strategies yield same result"


if __name__=="__main__":
    main()
