#Average of array elements without using function

import numpy as np

x= np.array([10,2,4,8,9,12,22,89,14])

temp = 0

#loop for accessing element from
temp =0
for i in range(len(x)):
    temp = temp + x[i]

avg = temp/len(x)
print(avg)

