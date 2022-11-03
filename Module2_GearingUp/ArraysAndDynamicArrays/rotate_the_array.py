# Rotate the Array
# In this lecture, we will learn how to rotate an array by ‘k’ units clockwise using different methods.
#
# Input: Arr[6] = { 1, 2, 3, 4, 5, 6 }, k = 3
# O: Arr[6] = { 4, 5, 6, 1, 2, 3 }
#
#
# Approach:
#
# Brute Force - Rotate the array clockwise by 1 unit and repeat the steps ‘k’ times.
# Time complexity: O(kN)
# Space complexity: O(1)
#
# Using a temporary array - We can create a temporary array and store the elements at their new position after rotation.
# Using Array Reversal
#
#
# Changed positions
# Time complexity: O(N)
# Space complexity: O(N)
#
# 3.  Using Array Reversal -
#
# Input: Arr[5] = { 1 7 3 4 5 }, k = 3
#
# Output: Arr[5] = [ 3 4 5 1 7 ]
#
# [ 1 7 3 4 5 ] → [ 3 4 5 1 7 ]
#
# We can divide the array into two subarrays of length N-k and k. Now, if we carefully look at the reverse of the two subarrays -
#
# reverse of [ 1 7 ] → [ 7 1 ]
#
# reverse of [ 3 4 5 ] → [ 5 4 3 ]
#
# Combining the above two reversed sub-arrays, we get → [ 7 1 5 4 3 ]
#
# And on reversing the above array, we get → [ 3 4 5 1 7 ], which is the desired output.
#
# Note: The above method is based on the logic that an array if reversed twice yields the same array.
#
#
# Time complexity: O(N)
# Space complexity: O(1)


