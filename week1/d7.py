import numpy as np

mat=np.arange(1,10).reshape(3,3)

print(f"Matrix:\n{mat}")
print(f"Shape: {mat.shape}")
print(f"Size: {mat.size}")
print(f"Dimension: {mat.ndim}")

# task 2

arr=np.random.normal(loc=5,scale=10,size=100)
print(f"Mean: {arr.mean()}")
print(f"Standard deviation: {arr.std()}")