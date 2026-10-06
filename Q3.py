import numpy as np

arr=np.arange(0,256).reshape(-1,4)

min=np.min(arr)

max=np.max(arr)

mean=np.mean(arr)

mask=arr>128

thr_image=np.where(mask,255,0)

print("Orignal Image:",arr)
print("Min Intensity:",min)
print("Max Intensity:",max)
print("Mean of Image:",mean)
print("Binary Mask:", mask)
print("Above Threshold Image:",thr_image)