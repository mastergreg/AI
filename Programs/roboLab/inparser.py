#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : inparser.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Sat 24 Dec 2011 08:09:34 PM EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

from sys import stdin

def retbools(st):
    a=[]
    for i in st:
        if i == 'X':
            a.append(True)
        elif i=='O':
            a.append(False)
    return a


def parseInput():
    lines = int(stdin.readline())
    robo1_initstate = map(int,stdin.readline().split())
    robo2_initstate = map(int,stdin.readline().split())
    #text = map(lambda x:x.split(),stdin.readlines())
    text = map(retbools,stdin.readlines())
    
    return (robo1_initstate,robo2_initstate,text)

print parseInput()
    

