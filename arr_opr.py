# from collections import defaultdict
# Given
# an
# array
# of
# positive
# integers
# nums and a
# positive
# integer
# target,
# return the
# minimal
# length
# of
# a
# subarray
# whose
# sum is greater
# than or equal
# to
# target.
#
# If
# there is no
# such
# subarray,
# return 0
# instead.
#
# ar = [2,3,4,5,6]
# ar = [6,5,4,3,2]
# target = 10
#
#
# 10-6 = 4
#
# Input: target = 7, nums = [2, 3, 1, 2, 4, 3]: nums = [2, 5,6,8,12,15]
#
# Output: 2
# for i=0 to n-1:
#     key = ar[i]
#     find = target - key
#     min_no_of_idx = maxsize
#
# Example 1:
#
#     Input:    strs = ["eat","tea","tan","ate","nat","bat"]
#  eaat => aaet
#
#     Output:    [["bat"],["nat","tan"],["ate","eat","tea"]]
#
#     size of list  = m
#     size of each word = n
# O(m*nlogn)
# mp = defaultdict(list)
# for i =0 to n-1:
#     for j=i+1 to n-1:
#        if list[i] == list[j]:
#            mp[list[i]].append
# Tc = O(m*nlogn) + O(M**2)
#
# eat => q.push("e") => if q.front() > strs["a"] => q.pop_front() and push q.push("a")
#     aet