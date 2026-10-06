import numpy as np

def calculate_statistics(seed):
    rng = np.random.default_rng(seed)

    data = rng.normal(size=1000)

    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)
    minimum = np.min(data)
    maximum = np.max(data)

    inside = (data >= mean - std) & (data <= mean + std)
    percentage = np.mean(inside) * 100

    print("Seed:", seed)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Percentage inside one standard deviation:", percentage, "%")
    
    return mean, median, std, minimum, maximum, percentage


print("Results for First Seed")
result1 = calculate_statistics(42)

print("\nResults for Second Seed")
result2 = calculate_statistics(123)

print("\nComparison")

print("Mean difference:", result2[0] - result1[0])
print("Median difference:", result2[1] - result1[1])
print("Standard deviation difference:", result2[2] - result1[2])
print("Minimum difference:", result2[3] - result1[3])
print("Maximum difference:", result2[4] - result1[4])
print("Percentage difference:", result2[5] - result1[5])