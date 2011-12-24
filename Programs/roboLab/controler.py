#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 24 Dec 2011 08:52:57 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import inparser
import astar

def main():
    (r1,r2,field) = inparser.parseInput()
    print r1,r2
    astar.astar(r1,r2,field)


if __name__=="__main__":
    main()

