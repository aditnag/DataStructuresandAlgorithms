import pandas as pd
import numpy as np

data_info = {'first': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
             'second': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data_info)
print(df)
# To add new column third
df['third'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(df)
# To add new column fourth
df['fourth'] = df['first'] + df['third']
print(df)

# Deleting cols and rows using drop
df.drop(
    labels=["fourth", 'third'],
    axis=1,
    inplace=True
)
print(df)

df.drop(
    labels=["a", 'b'],
    axis=0,
    inplace=True
)
print(df)

ndArray = np.array([1, 2, 3, 4], ndmin=6)
print(ndArray)
print('Dimensions of array:', ndArray.ndim)

inputArray = np.array([[35, 53, 63], [72, 12, 22], [43, 84, 56]])
new_col = np.array([[20, 30, 40]])
# delete 2nd column
arr = np.delete(inputArray, 1, axis=1)
# insert new_col to array
arr = np.insert(arr, 1, new_col, axis=1)
print(arr)

# arr = np.array([[8, 3, 2],
#                 [3, 6, 5],
#                 [6, 1, 4]])
# # sort the array using np.sort
# arr = np.sort(arr.view('i1,i1,i1'),
#               order=['f1'],
#               axis=0).view(np.int)

print("**************************************************")
"""
How will you sort the array based on the Nth column?
"""
# Create an example 2D NumPy array
arr = np.array([[3, 6, 9],
                [1, 4, 7],
                [2, 5, 8]])

# Get the indices that would sort the second column (index 1)
sorted_indices = np.argsort(arr[:,1])

# Use the sorted indices to rearrange the rows of the array
sorted_arr = arr[sorted_indices]

# Print the sorted 2D array
print(sorted_arr)

print("**************************************************")

# Create a NumPy array
arr = np.array([1, 3, 6, 8, 11, 14, 18])

# Define the target value
target_value = 7

# Calculate the absolute differences
differences = np.abs(arr - target_value)

# Find the index of the minimum difference
nearest_index = np.argmin(differences)

# Get the nearest value
nearest_value = arr[nearest_index]

print("Original Array:", arr)
print("Target Value:", target_value)
print("Nearest Value:", nearest_value)
