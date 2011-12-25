#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : inparser.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sun 25 Dec 2011 11:27:14 AM EET
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
    target = tuple(map(int,f.readline().split()))
    robo1_initstate = tuple(map(int,f.readline().split()))
    robo2_initstate = tuple(map(int,f.readline().split()))
    text = map(retbools,f.readlines())
    
    return (target,robo1_initstate,robo2_initstate,text)

