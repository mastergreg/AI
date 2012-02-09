#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : grids.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Thu 09 Feb 2012 01:38:45 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

lgrid=[]
blockChar = unichr(0x258A)
joinedColor = "0;32"
names = "Vasilis Gerakaris - Gregory Liras"

def revertMap(b):
    if b=="@" or b=="#":
        return b
    elif b>=0:
        return " "
    elif b<0:
        return "\033[41m \033[0m"
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
        if ( lgrid[x][y].startswith("\033")):
            lgrid[x][y] = "\033["+joinedColor+"m*\033[0m"
        else:
            lgrid[x][y]="\033["+color+"m*\033[0m"
    lgrid[sx][sy]="S"
    lgrid[fx][fy]="F"

def printpath():

    print "\033[47m"+(" "*(len(lgrid[0])+2))+"\033[0m"
    for i in lgrid:
        print "\033[47m \033[0m"+"".join(i)+"\033[47m \033[0m"
    print "\033[47m\033[1;34m"+(" "*(len(lgrid[0])+2-len(names)))+names+"\033[0m"

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
