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

import sys


class SlidingWindowTechnique:
    # def subArraySum(self):
    #     print("Enter the size of the array and the value of the window size")
    #     n, k = map(int, input().strip().split())
    #     ar = list(map(int, input().strip().split()))[:n]
    #     print(f"Sum of the sub-array of size {k} is:")
    #     sum = 0
    #     for i in range(k):
    #         sum += ar[i]
    #
    #     for i in range(k, n):
    #         print(sum)
    #         sum += ar[i]
    #         sum -= ar[i - k]
    #
    #     return sum
    #
    # def frequency(self):
    #     print("Enter the size of the array and the value of the window size")
    #     n, k = map(int, input().strip().split())
    #     ar = list(map(int, input().strip().split()))[:n]
    #     print(f"Enter the element whose frequency you want to find in each array of the window size {k}")
    #     x = int(input())
    #
    #     frq = 0
    #     for i in range(k):
    #         if ar[i] == x:
    #             frq += 1
    #
    #     for i in range(k, n):
    #         print(frq)
    #         if ar[i] == x:
    #             frq += 1
    #         if ar[i - k] == x:
    #             frq -= 1
    #     return frq

    # To find the minimum number of swaps to bring all the elements <= k together
    def swaps(self):
        print("Enter the size of the array and the value of K")
        n, k = map(int, input().strip().split())
        print("Enter the array elements")
        ar = list(map(int, input().strip().split()))[:n]

        countLegalElements = 0
        for i in range(n):
            if ar[i] <= k:
                countLegalElements += 1

        ans = sys.maxsize
        max_count = 0
        for i in range(countLegalElements):
            if ar[i] <= k:
                max_count += 1

        for i in range(countLegalElements, n):
            ans = min(ans, countLegalElements - max_count)
            if ar[i] <= k:
                max_count += 1
            if ar[i-countLegalElements] == k:
                max_count -= 1

        return ans


obj = SlidingWindowTechnique()
# print(obj.subArraySum())
# print(obj.frequency())
print(obj.swaps())
