#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###-------------------Question no 2----------------------##
###-------------------Assignment 02----------------------##

def SelfDriving_MonitoringSensor(distanceRange,detectObjectIndex,position):
    result = [0,1]
    temp = result.copy()                         #storing value of result in temp
    for index in range(2,distanceRange):
        temp += [temp[index-1] + temp[index-2]]  # Generating Fibonacci sequence      
        if index >= detectObjectIndex and position == 'start':
            result += [temp[index]+1]
        elif index >= detectObjectIndex and position == 'end':
            result += [temp[index]-1]
        else:
            result += [temp[index]]
    return result
            
print(SelfDriving_MonitoringSensor(15,0,"none")) #Fibonacci sequence of 15 elements
print(SelfDriving_MonitoringSensor(15,7,"start")) #start adding 1 from 7th index
print(SelfDriving_MonitoringSensor(15,7,"end")) #start subtracting 1 from 7th index

