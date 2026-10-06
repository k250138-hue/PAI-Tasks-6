import numpy as np

rng=np.random.default_rng()
arr=rng.integers(1,50,size=(10,4))


mean= np.mean(arr,axis=0)
dev=np.std(arr,axis=0)

standarize_dev= (arr-mean) / dev

new_mean=np.mean(standarize_dev,axis=0)
new_dev=np.std(standarize_dev,axis=0)

print("Original Data:")
print(arr)

print("\nMean of each feature:")
print(mean)

print("\nStandard deviation of each feature:")
print(dev)

print("\nStandardized Data:")
print(standarize_dev)

print("\nMean after standardization:")
print(new_mean)

print("\nStandard deviation after standardization:")
print(new_dev)