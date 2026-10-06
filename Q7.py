import numpy as np

# Create array containing valid values and NaN
data = np.array([10, 20, np.nan, 30, 40, np.nan, 50])

print("Original Array:")
print(data)

# Detect NaN values
nan_values = np.isnan(data)

print("\nNaN Detection:")
print(nan_values)

# Count NaN values
nan_count = np.sum(nan_values)

print("\nNumber of NaN values:", nan_count)

# Calculate statistics ignoring NaN
mean = np.nanmean(data)
minimum = np.nanmin(data)
maximum = np.nanmax(data)

print("\nMean ignoring NaN:", mean)
print("Minimum ignoring NaN:", minimum)
print("Maximum ignoring NaN:", maximum)

# Replace NaN values with mean
data[np.isnan(data)] = mean

print("\nArray after replacing NaN:")
print(data)

# Verify no NaN values remain
remaining_nan = np.isnan(data)

print("\nNaN Detection after replacement:")
print(remaining_nan)

print("\nNumber of NaN values after replacement:",
      np.sum(remaining_nan))