#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : controler.py
#
#* Purpose : 1st assignment in Artificial Intelligence
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 11 Feb 2012 04:15:04 AM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#* Created By : Vasilis Gerakaris <vgerak@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/


from inparser import parseUser
from astar import astar
from grids import flushgrid,printpath,designpath,modifygrid
from sys import argv

def main():
    (target,r1,r2,initialfield,heuristic) = parseUser()
    field = map(list,initialfield)
    print "\nLEGEND:"
    print "\033[1;34m Robot1 path \n\033[1;33m Robot2 path \n\033[0;32m Joined path \033[0m"
    print "\n \033[0;34m ======= Robot 2 plays 'nice' ======= \033[0m"
    (finalists1,nodes) = astar(r1,target,field,heuristic,1)
    total = nodes
    field = modifygrid(finalists1,field)
    (finalists2,nodes) = astar(r2,target,field,heuristic,2)
    total += nodes
    flushgrid(field)
    designpath("1;34",r1,target,finalists1)
    designpath("1;33",r2,target,finalists2)
    printpath()
    max1 = max(len(finalists1),len(finalists2))
    print "Max length in steps:", max1-1
    print "\t Robot 1 took:\t\t", len(finalists1)-1, " steps"
    print "\t Robot 2 (nice) took:\t", len(finalists2)-1, " steps"
    flushgrid(field)
    print "\n \033[0;34m ======= Robot 1 plays 'nice' ======= \033[0m"
    field = map(list,initialfield)
    (finalists2,nodes) = astar(r2,target,field,heuristic,2)
    total += nodes
    field = modifygrid(finalists2,field)
    (finalists1,nodes) = astar(r1,target,field,heuristic,1)
    total += nodes
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
    print "Total nodes considered:", total


if __name__=="__main__":
    main()
