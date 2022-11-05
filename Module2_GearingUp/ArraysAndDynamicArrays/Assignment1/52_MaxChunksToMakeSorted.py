# You are given an integer array
# arr of length n that represents a permutation of the integers in the range[0,n−1].
#
# We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
#
# Print the largest number of chunks we can make to sort the array
#
# Input Format
#
# First line of input contains an integers n
# Next line of input contains n space separated integers
# a1, a2, a3...., an (0 <= a[i] <= n−1 ). All the numbers are unique
# Output Format
#
# Output a single integer the largest number of chunks we can split the given array.
# Sample Input 0
#
# 5
#
# 1 0 2 3 4
#
# Sample Output 0
#
# 2
#
# Explanation
#
# We can split them into two chunks, such as [1, 0], [2, 3, 4]. However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
#
# Example
# Input
# 5
# 1 0 2 3 4
# Output
# 4


# cook your dish here
import sys


class MaxChunksToBeSorted:
    def main(self):
        n = int(input())
        arr = list(map(int, input().strip().split()))[:n]
        pmax = -sys.maxsize
        chunk = 0
        for i in range(0, n):
            pmax = max(pmax, arr[i])
            if i == pmax:
                chunk += 1

        print(chunk)


obj = MaxChunksToBeSorted()
obj.main()
