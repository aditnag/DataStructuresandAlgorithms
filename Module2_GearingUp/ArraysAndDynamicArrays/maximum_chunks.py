# Maximum Chunks
# Here we have been given a permutation array ‘Arr[N]’ - containing all the elements from 0 to N-1. We have to split the array into the maximum number of chunks (contiguous subarrays) such that after sorting all the chunks individually, we get a sorted array.
#
# Input: Arr[5] = { 1, 2, 0, 3, 4 }
# Output: 3
#
# We can divide the array into three chunks - [ 1 0 2  3  4 ]. After sorting each chunk individually we get a sorted array - [ 0, 1, 2, 3, 4 ]
#
# Approach:
#
# What will be the minimum number of chunks?
# One, if we consider the whole array as a chunk then sorting the chunk can yield us a sorted array. [ 5 4 3 2 1 ] => [ 1 2 3 4 5 ]
#
# Observation - Every chunk from index i to j should be a permutation of numbers from i to j.
# Eg.       [  1 2 0  3 4 ]
# Index:    0 1  2  3 4
#
# Implementation -
# Brute Force - Create two nested loops to check each subarray starting from 'i', if it can be chunked or not. If it can be chunked then we can increase the count of the answer variable and move our iterator after that chunk.
# Time complexity: O(N^2)
# Space complexity: O(1)
#
# Prefix Max - From the above observation, we can also infer that the chunks are divided at the index where the prefix max is equal to the array index. Since a chunk from the index, i to j is basically a permutation of numbers from i to j.
# Eg.              [ 1  2 0  3  4 ]
# Index:           0 1  2  3  4
# Prefix Max:   1  2 2  3  4
# Time complexity: O(N)
# Space complexity: O(1) - we can use the input array for calculating prefix max.
