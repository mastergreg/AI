#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : grids.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Wed  8 Feb 2012 23:17:17 EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

lgrid=[]

def revertMap(b):
    if b=="@" or b=="#":
        return b
    elif b>=0:
        return "-"
    elif b<0:
        return "\033[0;31mx\033[0m"
    else:
        return b

def flushgrid(grid):
    global lgrid
    lgrid = []
    for i in grid:
        lgrid.append(map(revertMap,list(i)))

def designpath(color,(sx,sy),(fx,fy),finalists):
    global lgrid
    for (x,y) in finalists:
        lgrid[x][y]="\033["+color+"m*\033[0m"
    lgrid[sx][sy]="S"
    lgrid[fx][fy]="F"

def printpath():
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

def modifygrid(finalists,grid):
    i=1
    for (x,y) in finalists:
        grid[x][y]=i
        i+=1
    return grid
