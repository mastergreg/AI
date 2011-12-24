#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : inparser.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 24 Dec 2011 10:09:02 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

def retbools(st):
    a=[]
    for i in st:
        if i == 'X':
            a.append(False)
        elif i=='O':
            a.append(True)
    return a


def parseInput(f):
    lines = int(f.readline())
    robo1_initstate = map(int,f.readline().split())
    robo2_initstate = map(int,f.readline().split())
    #text = map(lambda x:x.split(),f.readlines())
    text = map(retbools,f.readlines())
    
    return (robo1_initstate,robo2_initstate,text)

