#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : inparser.py
#
#* Purpose :
#
#* Creation Date : 24-12-2011
#
#* Last Modified : Wed  8 Feb 20:45:40 2012
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

def retbools(st):
    a=[]
    for i in st:
        if i == 'X':
            a.append(-1)
        elif i=='O':
            a.append(0)
    return a


def parseInput(f):
    lines = int(f.readline().split()[0])
    target = tuple(map(int,f.readline().split()))
    robo1_initstate = tuple(map(int,f.readline().split()))
    robo2_initstate = tuple(map(int,f.readline().split()))
    text = map(retbools,f.readlines())

    return (target,robo1_initstate,robo2_initstate,text)
