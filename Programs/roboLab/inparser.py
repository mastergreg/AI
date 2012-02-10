#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : inparser.py
#
#* Purpose : Input parsing of state space
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Fri 10 Feb 2012 14:33:24 EET
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

def retbools(st):
    a=[]
    for i in st:
        #'X' marks obstacle, 'O' marks open space
        if i == 'X':
            a.append(-1)
        elif i=='O':
            a.append(0)
    return a

def parseInput(f):
    lines = int(f.readline().split()[0])
    robo1_initstate = tuple(map(int,f.readline().split()))
    robo2_initstate = tuple(map(int,f.readline().split()))
    target = tuple(map(int,f.readline().split()))
    text = map(retbools,f.readlines())
    return (target,robo1_initstate,robo2_initstate,text)
