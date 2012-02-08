#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : astar.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Wed  8 Feb 21:27:58 2012
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
    ancestors={}
    #ancestors is a dictionary which stores the ancestors of each point
    #this will be used in the end to rebuild the path
    passedlist=[]
    passedlist.append(startpoint)
    #passedlist contains nodes that have been processed already
    starque=[]
    sizex=len(grid)
    #num of rows
    sizey=len(grid[0])
    #num of columns
    possible = map(lambda x:(manthatanDist(x,finishpoint)+1,1,x),nextNodes(startpoint))
    #each point has these characteristics
    #(heuristic,cost,((x,y),father))
    for (h,c,((x,y),father)) in possible:
        #checking for bounds and then checking if grid[x][y]==True
        #now should be grid[x][y]==0 ??
        if x >= 0 and y >= 0 and x < sizey and y < sizex and grid[x][y]:
            passedlist.append((x,y))
            ancestors[(x,y)]=father
            starque.append((h,c,(x,y)))
    ind = starque.index(min(starque))
    #find index of touple with the lowest heuristic+cost
    nxt = starque.pop(ind)
    #remove if from the queue
    #and store it in nxt
    #nxt = (minh,c,((x,y),father))
    current = nxt[2]
    currentCost = nxt[1]
    #current cost is the cost so far that is stored in nxt

    while(current!=finishpoint):
        #untill you find the end
        possible = map(lambda x:(manthatanDist(x,finishpoint)+currentCost+1,currentCost+1,x),nextNodes(current))
        #find the next possible list
        for (h,c,((x,y),father)) in possible:
            if x >= 0 and y >= 0 and x < sizex and y < sizey and grid[x][y]:
                #check what is in possible list, make sure its sane
                #starque = putinlist(starque,(h,c,(x,y)))
                if(x,y) not in passedlist:
                    passedlist.append((x,y))
                    #if i havend passed this so far
                    #then store it and insert the coordinates in ancestors dictionary
                    ancestors[(x,y)]=father
                    starque.append((h,c,(x,y)))
                #if i have passed this already then i can reach this with a lower cost
                #so i don't need to save x,y

        ind = starque.index(min(starque))
        #find index of touple with the lowest heuristic+cost
        nxt = starque.pop(ind)
        #remove if from the queue
        #and store it in nxt
        #nxt = (minh,c,((x,y),father))
        current = nxt[2]
        currentCost = nxt[1]
        #current cost is the cost so far that is stored in nxt
    print "Found it after %d iterations" %len(passedlist)

    finalists=[]
    i =finishpoint
    finalists.append(i)
    #starting from the end build the path list
    #following the directions in the ancestors dictionary
    while i !=startpoint:
        i = ancestors[i]
        finalists.append(i)
    finalists.reverse()
    #reverse the path so it starts from the beginning
    q.put(finalists)
    #put it in the queue
