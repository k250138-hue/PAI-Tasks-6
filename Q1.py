import numpy as np

marks = np.array([
    [78, 85, 69, 90, 74],
    [55, 62, 70, 68, 60],
    [88, 91, 84, 79, 95],
    [45, 52, 48, 50, 42],
    [67, 73, 71, 65, 69],
    [92, 89, 94, 90, 96],
    [50, 55, 60, 58, 52],
    [35, 40, 45, 38, 42],
    [81, 76, 85, 88, 79],
    [63, 68, 59, 72, 66]
])

total = np.sum(marks, axis=1)
average = np.mean(marks, axis=1)
subject_average = np.mean(marks, axis=0)

highest = np.argmax(average) + 1

count = np.sum(average >= 50)

status = np.where(average >= 50, "Pass", "Fail")

print("Student Total:", total)
print("Student Average:", average)
print("Subject Average:", subject_average)
print("Highest Average: Student", highest)
print("Students with average >= 50:", count)
print("Result:", status)