#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sun 25 Dec 2011 12:00:09 AM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import inparser
import astar
import sys

def main():
    f=open(sys.argv[1],"r")
    (r1,r2,field) = inparser.parseInput(f)
    f.close()
    astar.astar(r1,r2,field)


if __name__=="__main__":
    main()

