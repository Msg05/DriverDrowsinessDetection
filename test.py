import numpy as np

# Create a NumPy array
data = np.array([1, 2, 3, 4, 5])

# Perform operations
squared = data ** 2  # Element-wise square
sum_data = np.sum(data)  # Sum of all elements
mean_data = np.mean(data)  # Mean of the array
max_value = np.max(data)  # Maximum value in the array

# Print results
print("Original Array:", data)
print("Squared Array:", squared)
print("Sum:", sum_data)
print("Mean:", mean_data)
print("Max Value:", max_value)

