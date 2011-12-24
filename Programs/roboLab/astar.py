#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : astar.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 24 Dec 2011 10:25:08 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import grids

def manthatanDist(point1,point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

def nextNodes((a,b)):
    return [(a-1,b),(a,b-1),(a+1,b),(a,b+1)]


def astar(startpoint,finishpoint,grid):
    starque=[]
    sizex=len(grid)
    sizey=len(grid[0])
    #map(lambda x:heappush(starque,x),nextNodes(startpoint))
    #no need to use heaps
    grids.printgrid(startpoint,finishpoint,grid)
    possible = map(lambda x:(manthatanDist(x,finishpoint)+1,1,x),nextNodes(startpoint))
    #each point has these characteristics
    #(heuristic,cost,(x,y))
    for (h,c,(x,y)) in possible:
        #if x<sizex and y<sizey:
        if x < sizey and y < sizex and grid[x][y]:
            starque.append((h,c,(x,y)))
    ind = starque.index(min(starque))
    nxt = starque.pop(ind)
    current = nxt[2]
    currentCost = nxt[1]
    grids.printgrid(current,finishpoint,grid)
    print nxt
    dummy = raw_input("How does it look?? ")

    while(current!=tuple(finishpoint)):
        possible = map(lambda x:(manthatanDist(x,finishpoint)+currentCost+1,currentCost+1,x),nextNodes(current))
        #each point has these characteristics
        #(heuristic,cost,(x,y))
        for (h,c,(x,y)) in possible:
            if x < sizex and y < sizey and grid[x][y]:
                starque.append((h,c,(x,y)))
        ind = starque.index(min(starque))
        nxt = starque.pop(ind)
        current = nxt[2]
        currentCost = nxt[1]
        grids.printgrid(current,finishpoint,grid)
        print nxt
        dummy = raw_input("How does it look?? ")


    

