# Sliding Window Technique
# The Sliding Window Technique helps in reducing the time complexity of a solution by converting nested loops into a single loop. In the lecture, we will take a glimpse at different types of problems that can be solved using the Sliding window technique.
#
# Given an integer array ‘Arr[N]’. Print the individual sum of all the subarrays of length ‘k’.
#
# Approach:
#
# Brute Force - Create two nested loops to find all the subarrays of size ‘k’ and print their sum.
# Time complexity: O(kN)
# Space complexity: O(1)
#
# Sliding Window Technique - In this technique, we first calculate the sum of a window (subarray of size ‘k’) and then slide the window by one unit each, to find the sum of the remaining subarrays respectively.
# Sliding Window Technique
# Time complexity: O(N)
# Space complexity: O(1)


