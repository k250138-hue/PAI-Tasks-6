import numpy as np
arr=np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]])

mean=np.mean(arr,axis=1)

min=np.min(arr,axis=1)

max=np.max(arr,axis=1)

dev=np.std(arr,axis=1)

highest_avg=np.argmax(mean)+1

thre=8

result=np.where(arr>8,"True","False")

print("Orignal sensor readings:",arr)
print("Min readings:",min)
print("Max readings:",max)
print("Mean of readings:",mean)
print("Highest Average reading: ", highest_avg)
print("Detect readings above a selected threshold:",result)
