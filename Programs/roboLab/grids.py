#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : grids.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sun 25 Dec 2011 10:00:01 AM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

lgrid=[]

def revertMap(b):
    if b=="@" or b=="#":
        return b
    elif b:
        return "-"
    elif not b:
        return "\033[0;31mx\033[0m"
    else:
        return b

def flushgrid(grid):
    global lgrid
    lgrid = []
    for i in grid:
        lgrid.append(map(revertMap,list(i)))

def printpath((sx,sy),(fx,fy),finalists):
    global lgrid
    for (x,y) in finalists:
        lgrid[x][y]="\033[1;34m*\033[0m"
    lgrid[sx][sy]="S"
    lgrid[fx][fy]="F"
    for i in lgrid:
        print "".join(i)



def printgrid((cx,cy),(fx,fy),grid):
    global lgrid
    if not lgrid:
        for i in grid:
            lgrid.append(map(revertMap,i))
    lgrid[cx][cy]="@"
    lgrid[fx][fy]="#"
    for i in lgrid:
        print "".join(i)
    print "----"
