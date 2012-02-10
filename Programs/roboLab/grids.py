#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : grids.py
#
#* Purpose : Functions related with grid modifying & output
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Fri 10 Feb 2012 04:17:27 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#* Created By : Vasilis Gerakaris <vgerak@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

lgrid=[]
blockChar = unichr(0x258A)
joinedColor = "0;32"
names = "Vasilis Gerakaris - Gregory Liras"

#Choose what will be printed depending on element in position
def revertMap(b):
    if b=="@" or b=="#":
        return b
    elif b>=0:
        return " "                  #unused space gets blankspace
    elif b<0:
        return "\033[41m \033[0m"   #obstacle gets red solid box
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
        if ( lgrid[x][y].startswith("\033")):       #if both robots use position, color with green
            lgrid[x][y] = "\033["+joinedColor+"m*\033[0m"
        else:                                       #else keep designated robot color
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
        grid[x][y]=i        #robot 1 marks its steps on the grid to
        i+=1                #be unusable (on same turn) by robot 2
    return grid
