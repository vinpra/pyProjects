#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:14:34 2020

@author: praveen
"""


def comaparetimes(t1, t2):
    
    (ho1,mn1) = t1.split(":")
    (ho2,mn2) = t2.split(":")
    
    t1m = int(ho1)*60 + int(mn1)
    t2m = int(ho2)*60 + int(mn2)
    
    if t1m > t2m :
        return 1 # greater than
    elif t1m == t2m :
        return 0 # equal
    else:
        return -1 # less than
    
def timediffinmin(t1,t2):
    mins = 0
    
    (ho1,mn1) = t1.split(":")
    (ho2,mn2) = t2.split(":")
    
    t1m = int(ho1)*60 + int(mn1)
    t2m = int(ho2)*60 + int(mn2)
    
    mins = t2m-t1m
    print("mins :" + str(mins) )
    return mins
    
def mergeschedules(ps1, ps2):
    p1 = 0
    p2 = 0 # init pointers
    booked_arr = []
    
    while p1<len(ps1) or p2<len(ps2) :
        
        if (p1 < len(ps1)) and (comaparetimes(ps1[p1][0], ps2[p2][0]) == -1):
            booked_arr.append(ps1[p1])
            if p1 < len(ps1):
               p1 = p1+1
              
        else:
            booked_arr.append(ps2[p2])
            if p2 < len(ps2):
                p2=p2+1
        
    print(booked_arr)
            
    i = 0
    
    while i<len(booked_arr)-1 :
        end1 = booked_arr[i][1]
        start2 = booked_arr[i+1][0]
        
        if comaparetimes(end1,start2) == 1 or comaparetimes(end1,start2) == 0:
           end2 = booked_arr[i+1][1]
           if comaparetimes(end1,end2) == 0 or comaparetimes(end1,end2) == 1:
               booked_arr.pop(i+1)
               i=i-1
           else:
               booked_arr[i][1] = end2
               booked_arr.pop(i+1)
               i=i-1
        i=i+1
          

    
    return booked_arr

def getmeetingschedules(ps1, ps2, time):
    
    # first get the merged array
    merged_arr = mergeschedules(ps1, ps2)
    avail_blocks = []
    i = 0
    
    while i < len(merged_arr)-1 :
        start1 = merged_arr[i][1]
        end1 = merged_arr[i+1][0]
        if timediffinmin(start1, end1) > time :
            avail_blocks.append([start1,end1])
        
        i=i+1
    return avail_blocks
                

ar1 = [["9:00", "10:00"], ["11:00", "11:30"], ["14:00", "15:00"]]

ar2 = [["9:30", "10:00"], ["11:30", "12:30"], ["16:00", "17:00"],]


print (getmeetingschedules(ar1,ar2,30))



