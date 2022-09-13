#Sum of array elements without using Sum function

import numpy as np

x= np.array([10,2,4,8,9,12,22,89,14])

temp = 0

#loop for accessing element from
for i in range(len(x)):
    temp = temp+x[i]
    #sum of elements


print(temp)