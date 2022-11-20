# Lecture 13: Max Gap Problem: Bucketing
# In this lecture, we will learn about the technique of Bucketing. Here we have been given an integer array ‘Arr[ N ]’ and we have to return the maximum difference between two consecutive elements when the array is in a sorted state.
#
#
# Approach:
#
# Brute Force - Sort the array and calculate the maximum difference between two consecutive elements.
# Time complexity: O(NlogN)
# Space complexity: O(1)
#
# Using Bucketization - Can you think of the minimum possible value of the answer? Let’s call it gap.
#
# gap = ceil((Max - Min)/(N - 1))
#
# Eg. 10 _ _ _ _  20 ; N=6
#
# In this case, the gap will be 2, i.e. when the elements are 12, 14, 16, 18 respectively.
#
# Similarly for,  10 _ _ _ _ 21 ; N=6
#
# The gap will be 3, i.e. when the elements are 12, 14, 16, 18 respectively.
#
# Since we know that, Answer >= gap. Thus, if somehow we are able to create buckets of size ‘gap’, then there will not be any need to calculate the difference between the elements which are lying in those particular buckets.
#
# And if we observe carefully, we will realise that our answer will be the maximum of the differences between the max & min elements from consecutive buckets.
#
# Time complexity: O(N)
# Space complexity: O(N)
#
# Summary of the steps:
# Find the minimum possible value of the answer ie gap = ceil((max-min)/(N-1))
#
# Create two temporary arrays maxArr[ N ] and minArr[ N ] for storing the max & min of each bucket.
#
# Calculate the bucket number of each element ie bucket = (Arr[ i ] - min)/gap and store the min & max of each bucket in minArr & maxArr.
#
# Note: In the above equation, 'gap' can not be zero (0/0 division), therefore take care of test cases containing all elements as equal.
#
# Iterate on maxArr & minArr to calculate the difference between the maximum & minimum elements from the consecutive buckets.