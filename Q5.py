import numpy as np

A_Mat = np.arange(1, 5).reshape(2, 2)

B_Mat = np.array([[4, 5],
                  [6, 7]])

print("Matrix A:")
print(A_Mat)

print("\nMatrix B:")
print(B_Mat)


print("\n--- Addition ---")
print("Shape of A:", A_Mat.shape)
print("Shape of B:", B_Mat.shape)
add = A_Mat + B_Mat
print("A + B:")
print(add)


print("\n--- Subtraction ---")
print("Shape of A:", A_Mat.shape)
print("Shape of B:", B_Mat.shape)
sub = A_Mat - B_Mat
print("A - B:")
print(sub)


print("\n--- Element-wise Multiplication ---")
print("Shape of A:", A_Mat.shape)
print("Shape of B:", B_Mat.shape)
ele_wise_mul = A_Mat * B_Mat
print("A * B:")
print(ele_wise_mul)


print("\n--- Matrix Multiplication ---")
print("Shape of A:", A_Mat.shape)
print("Shape of B:", B_Mat.shape)
Mat_mul = A_Mat @ B_Mat
print("A @ B:")
print(Mat_mul)


print("\n--- Transpose ---")
print("Shape of A:", A_Mat.shape)
trans_A = np.transpose(A_Mat)
print("Transpose of A:")
print(trans_A)

print("Shape of B:", B_Mat.shape)
trans_B = np.transpose(B_Mat)
print("Transpose of B:")
print(trans_B)


print("\n--- Determinant ---")
print("Shape of A:", A_Mat.shape)
det_A = np.linalg.det(A_Mat)
print("Determinant of A:", det_A)

print("Shape of B:", B_Mat.shape)
det_B = np.linalg.det(B_Mat)
print("Determinant of B:", det_B)


print("\n--- Inverse ---")
print("Shape of A:", A_Mat.shape)
inv_A = np.linalg.inv(A_Mat)
print("Inverse of A:")
print(inv_A)

print("Shape of B:", B_Mat.shape)
inv_B = np.linalg.inv(B_Mat)
print("Inverse of B:")
print(inv_B)

# | Operation                       | Dimension requirement           |
# | ------------------------------- | ------------------------------- |
# | Addition                        | Same shape                      |
# | Subtraction                     | Same shape                      |
# | Element-wise multiplication `*` | Compatible/broadcastable shapes |
# | Matrix multiplication `@`       | Columns of A = Rows of B        |
# | Transpose                       | No special requirement          |
# | Determinant                     | Square matrix                   |
# | Inverse                         | Square matrix + determinant ≠ 0 |
