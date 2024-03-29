#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : astar.py
#
#* Purpose : Main body of A* algorithm
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 11 Feb 2012 04:18:25 AM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#* Created By : Vasilis Gerakaris <vgerak@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/


def nextNodes((a,b)):
    return [((a-1,b),(a,b)),((a,b-1),(a,b)),((a+1,b),(a,b)),((a,b+1),(a,b))]

def astar(startpoint,finishpoint,grid,heuristic,robotID=1):
    ancestors={}
    #ancestors is a dictionary which stores the ancestors of each point
    #this will be used in the end to rebuild the path
    passedlist=[]
    passedlist.append(startpoint)
    #passedlist contains nodes that have been processed already
    starque=[]
    #num of rows
    sizex=len(grid)
    #num of columns
    sizey=len(grid[0])
    currentCost = 0
    current = startpoint

    while(current!=finishpoint):
        #until you find the end
        possible = map(lambda x:(heuristic(x,finishpoint)+currentCost+1,currentCost+1,x),nextNodes(current))
        #find the next possible list
        for (h,c,((x,y),father)) in possible:
            if x >= 0 and y >= 0 and x < sizex and y < sizey and grid[x][y] != -1:
                #check what is in possible list, make sure its sane
                if(x,y) not in passedlist:
                    passedlist.append((x,y))
                    #if I havend passed this so far
                    #then store it and insert the coordinates in ancestors dictionary
                    ancestors[(x,y)]=father
                    starque.append((h,c,(x,y)))
                #if I have passed this already then I can reach this with a lower cost
                #so i don't need to save x,y

        ind = starque.index(min(starque))
        (h,c,(x,y)) = starque.pop(ind)
        #Conflict detection for all steps
        while(grid[x][y] == c + 1 ):
            print "Conflict in [%d,%d] on step %d , Robot #%d recalculating.." %(x,y,c,robotID)
            starque.append((h+1,c+1,(x,y)))
            ind = starque.index(min(starque))
            #Consideration of alternative paths
            print "Robot #%d trying.." %(robotID),starque[ind][2][0],starque[ind][2][1]
            (h,c,(x,y)) = starque.pop(ind)


        #find index of touple with the lowest heuristic+cost
        nxt = (h,c,(x,y))
        #remove if from the queue and store it in nxt
        #nxt = (minh,c,((x,y),father))
        current = nxt[2]
        currentCost = nxt[1]
        #current cost is the cost so far that is stored in nxt
    print "Found it after %d expanded nodes" %len(passedlist)

    finalists=[]
    i =finishpoint
    finalists.append(i)
    #starting from the end build the path list
    #following the directions in the ancestors dictionary
    while i !=startpoint:
        i = ancestors[i]
        finalists.append(i)
    #reverse the path so it starts from the beginning
    finalists.reverse()
    #put it in the queue
    return (finalists, len(passedlist))
