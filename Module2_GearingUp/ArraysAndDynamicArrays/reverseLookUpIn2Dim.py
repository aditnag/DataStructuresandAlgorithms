# Reverse Lookup in 2-Dimenssions
# In this lecture, we will solve a problem based on reverse lookup in a 2D array. We have a 2d matrix Arr[M][N] and we have to find the sum of all the submatrices.
#
# How to define a submatrix uniquely?
# We can define a unique submatrix by using the indices of either -
#
# Top Left (TL) & Bottom Right (BR) cell
# Bottom Left (BL) & Top Right (TR) cell
#
# Approach:
# Brute Force - Create nested loops to iterate through every possible TL & BR valid cell combination to find all the submatrices and calculate their total sum respectively.
# Time complexity: O((M^3)*(N^3))
# Space complexity: O(1)
#
# Using Reverse Lookup - Can we use the approach followed in the previous question to find out the contribution of each array element to the total sum?
# Reverse Lookup in a 2D Array
# An element Arr[ i ][ j ] will be a part of all those submatrices who have -
#
# 0<=TLi<=i & 0<=TLj<=j
# i<=BRi<=M-1 & j<=BRj<=N-1
# Therefore, by the Rule of Products, Arr[ i ][ j ] appears = (i+1)*(j+1)*(M-i)*(N-j)
#
# Total sum = Σi(Σj(Arr[i][j]*(i+1)*(j+1)*(M-i)*(N-j)))     [from i=0 to M-1 & j=0 to N-1]
#
# Time complexity: O(MN)
# Space complexity: O(1)
#
# Note: The above method involves integer multiplication and the product may be out of the valid integer range. Therefore we may have to calculate the modulus of the product each time by some large prime number say, 10^9 + 7.