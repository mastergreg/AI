#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : grids.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 24 Dec 2011 09:31:53 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

def revertMap(b):
    if b=="@" or b=="#":
        return b
    elif b:
        return "o"
    elif not b:
        return "x"
    else:
        return b

def printgrid((cx,cy),(fx,fy),grid):
    lgrid=[]
    for i in grid:
        lgrid.append(list(i))
    lgrid[cx][cy]="@"
    lgrid[fx][fy]="#"
    for i in lgrid:
        print "".join(map(revertMap,i))
    print "----"
