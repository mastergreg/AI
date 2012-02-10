#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : heuristics.py
#
#* Purpose :
#
#* Creation Date : 09-02-2012
#
#* Last Modified : Fri 10 Feb 2012 04:17:27 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#* Created By : Vasilis Gerakaris <vgerak@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

def manhattanDist(point1,point2):
    return abs(point1[0][0]-point2[0])+abs(point1[0][1]-point2[1])

def squaredDist(point1,point2):
    return (point1[0][0]-point2[0])**2 + (point1[0][1]-point2[1])**2
