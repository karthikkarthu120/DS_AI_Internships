import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])

result = a + b
print("Result of adding array a and b:")
print(result)

#Vectorized vs Loop
print("Vectorized vs Loop")
arr = np.random.rand(1000000)
print(arr)

#vectorized
print("Vectorized operation:")
squared = arr * 2
print(squared)

#zero dimensions
zero_dim = np.zeros((4,2))
print("Zero dimension array:")
print(zero_dim)

#one dimension
one_dim = np.array([1,2,3,4,5])
print("One dimension array:")
print(one_dim)

#two dimension
two_dim = np.array([[1,2,3],[4,5,6]])
print("Two dimension array:")
print(two_dim)

#three dimension
three_dim = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Three dimension array:")
print(three_dim)

#reshaping arrays
print("Reshaping arrays: ")
arr = np.arange(12)
reshaped = arr.reshape(3,4)
print(reshaped)

#vertical stacking
print("Vertical Stacking")
a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)

#Horizontal Stacking
print("Horizontal Stacking")
hstacked = np.hstack((a, b))
print(hstacked)

#Statistical functions
print("Statistical functions:")
data = np.array([[10, 20, 30],
                 [40, 50, 60]])
print(np.mean(data))
print(np.mean(data, axis=0))

#linear Algebra
print("Linear Algebra")
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
print(np.dot(A, B))







