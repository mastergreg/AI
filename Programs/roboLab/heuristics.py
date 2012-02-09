#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : heuristics.py
#
#* Purpose :
#
#* Creation Date : 09-02-2012
#
#* Last Modified : Thu 09 Feb 2012 06:49:17 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

def manhattanDist(point1,point2):
    return abs(point1[0][0]-point2[0])+abs(point1[0][1]-point2[1])


def squaredDist(point1,point2):
    return (point1[0][0]-point2[0])**2 + (point1[0][1]-point2[1])**2
