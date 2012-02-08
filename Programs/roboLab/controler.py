#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Wed  8 Feb 21:34:30 2012
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

from multiprocessing import Process,Queue
import sys

from inparser import parseInput
from astar import astar
from grids import flushgrid,printpath,designpath
#import psyco

#psyco.full()

def main():
    if len(sys.argv) == 1:
        print "Usage: ./controler.py <inputfile>"
        return -1
    f=open(sys.argv[1],"r")
    (target,r1,r2,field) = parseInput(f)
    f.close()
    q1=Queue()
    q2=Queue()
    p1 = Process(target=astar,args=(q1,r1,target,field,))
    p2 = Process(target=astar,args=(q2,r2,target,field,))
    p1.start()
    p2.start()
    finalists1 = q1.get()
    p1.join()
    finalists2 = q2.get()
    p2.join()
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()


if __name__=="__main__":
    main()

