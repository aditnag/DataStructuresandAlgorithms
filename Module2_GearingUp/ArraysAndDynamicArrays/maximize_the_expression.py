# Maximize the Expression
# In this lecture, we will look at another problem based on the pre-computation technique. Here, we have been given an array ‘Arr[N]’ and we have to maximise ‘s’
# s = p*Arri + q*Arrj + r*Arrk where p, q, r ∈ Z and i < j < k
#
# Approach:
#
# Brute force - Run three nested loops to find the sum of all possible combinations and hence the maximum value of ‘s’.
# Time Complexity: O(N^3)
# Space Complexity: O(1)
#
# How about choosing the first three largest elements to calculate ‘s’?
# No, it may not work since we are not dealing with positive numbers alone. Let us see an example -
# Arr[5] = { 1, 2, 3, 4, -5}, p = 1, q = 2, r = -3
# According to the above approach,
# s = 1(2) + 2(3) + (-3)(4) = -4, which is not the correct answer.
#
# What if we know all the three maximum terms separately?
# Let a = p*Arri, b = q*Arrj and c = r*Arrk. If we can fix the second term (b) and find the maximum possible value of a & c corresponding to that b. And if we repeat the process for all the possible values of b then we can easily find the maximum value of ‘s’.
#
# For implementing this, we can create a prefix max(PMAX) and a suffix max(SMAX) array for the first and the third term respectively. We can then iterate on the array for the second term to find the answer.
#
# ans = max (ans, PMAX[j-1]+q*Arr[j]+SMAX[j+1])
#
# Time complexity: O(N)
# Space complexity: O(N)
import sys


class MTE:
    def main(self):
        print("Enter the size of the array")
        n = int(input())
        print("Enter the array elements")
        ar = list(map(int, input().strip().split()))[:n]
        print("Enter the value of the co-efficients p,q and r")
        p, q, r = map(int, input().strip().split())

        # Finding prefix max
        pmax = ar.copy()
        pmax[0] = p * ar[0]
        for i in range(1, n):
            pmax[i] = max(pmax[i - 1], p * ar[i])

        # Finding suffix max
        smax = ar.copy()
        smax[n - 1] = r * ar[n - 1]
        for i in range(n - 2, -1, -1):
            smax[i] = max(smax[i + 1], r * ar[i])

        # Finally sliding the middle element from idx = 2 to n-2
        ans = -sys.maxsize
        for i in range(1, n - 1):
            ans = max(ans, pmax[i - 1] + q * ar[i] + smax[i + 1])

        return ans


obj = MTE()
print(obj.main())
