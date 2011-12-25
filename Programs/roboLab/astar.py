#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : astar.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sun 25 Dec 2011 11:32:36 AM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

from multiprocessing import Queue

def manthatanDist(point1,point2):
    return abs(point1[0][0]-point2[0])+abs(point1[0][1]-point2[1])

def nextNodes((a,b)):
    return [((a-1,b),(a,b)),((a,b-1),(a,b)),((a+1,b),(a,b)),((a,b+1),(a,b))]

def putinlist(starque,(h,c,xy)):
    if not starque:
        starque.append((h,c,xy))
        return starque

    for i in range(len(starque)):
        (sh,sc,sxy) = starque[i]
        if sxy == xy:
            starque.pop(i)
            (sh,sc,sxy) = min((sh,sc,sxy),(h,c,xy))
            starque.append((sh,sc,sxy))
            return starque
            


def astar(q,startpoint,finishpoint,grid):
    ansestors={}
    passedlist=[]
    passedlist.append(startpoint)
    starque=[]
    sizex=len(grid)
    sizey=len(grid[0])
    possible = map(lambda x:(manthatanDist(x,finishpoint)+1,1,x),nextNodes(startpoint))
    #each point has these characteristics
    #(heuristic,cost,((x,y),father))
    for (h,c,((x,y),father)) in possible:
        if x >= 0 and y >= 0 and x < sizey and y < sizex and grid[x][y]:
            passedlist.append((x,y))
            ansestors[(x,y)]=father
            starque.append((h,c,(x,y)))
    ind = starque.index(min(starque))
    nxt = starque.pop(ind)
    current = nxt[2]
    currentCost = nxt[1]

    while(current!=finishpoint):
        possible = map(lambda x:(manthatanDist(x,finishpoint)+currentCost+1,currentCost+1,x),nextNodes(current))
        for (h,c,((x,y),father)) in possible:
            if x >= 0 and y >= 0 and x < sizex and y < sizey and grid[x][y]:
                #starque = putinlist(starque,(h,c,(x,y)))
                if(x,y) not in passedlist:
                    passedlist.append((x,y))
                    ansestors[(x,y)]=father
                    starque.append((h,c,(x,y)))
        ind = starque.index(min(starque))
        nxt = starque.pop(ind)
        current = nxt[2]
        currentCost = nxt[1]
    print "Found it after %d iterations" %len(passedlist)

    finalists=[]
    i =finishpoint
    finalists.append(i)
    while i !=startpoint:
        i = ansestors[i]
        finalists.append(i)
    finalists.reverse()
    q.put(finalists)
