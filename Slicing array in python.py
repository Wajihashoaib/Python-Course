#Slicicng array

#libraries#import numpy as np


A = np.array([ [1,4,6,7],
                     [7,3,8,10],
                     [8,3,4,9],
                     [9,1,6,11]])

#Access element '3' ----> in second row
A[1,1]

#Access element '6' ----> in last row
A[3,2]

#Access complete array
A[0:]

#Access first row verticaly
A[:,0]

#Third row with all columns
A[2,:]

#except first row and first column
A[1:,1:]

#Three rows of second and third column
A[0:3,1:3]

#second and third row of first second and third colum
A[1:3,0:3]