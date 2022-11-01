# Histogram Problem
# In this lecture, we will discuss the Rainwater collection problem. Here, we have been given an integer array ‘Arr[N]’ containing the heights of 'N' pillars. We have to find the total height of the water column trapped between the pillars after the rainfall.
#
# Approach:
#
# Which pillars will hold water on their tops?
# Histogram
# It can be seen in the above illustration, only the pillars with a larger pillar in their left and right neighbourhood can hold water.
#
# Will the boundary pillars hold water?
# No, since there is no supporting pillar on the other side.
# Solution - If we know the largest left and right neighbours for each pillar then we can find the amount of water that it can hold on its top.
# Amount of water on the top of pillar 'i' = max(0, (min(largest left neighbour, largest right neighbour) - height of pillar i))
#
# Implementation - Can you think of how to apply a pre-computation technique that was taught in the previous lecture?
# For pre-processing, we can calculate the prefix and suffix max for each pillar and use it to find the amount of water they will hold on their top.
#
# Time complexity: O(N)
# Space complexity: O(N)

import sys


class Histogram:
    def main(self):
        print("Enter the total number of buildings")
        n = int(input())
        print(f"Enter the heights of the {n} buildings")
        ar = list(map(int, input().strip().split()))[:n]

        pmax = ar.copy()
        for i in range(1, n):
            pmax[i] = max(pmax[i - 1], ar[i])

        smax = ar.copy()
        for i in range(n - 2, -1, -1):
            smax[i] = max(smax[i + 1], ar[i])

        # Quantity of water stored over ith building
        amount = 0
        for i in range(1, n - 1):
            deciding_height = min(pmax[i - 1], smax[i + 1])
            if deciding_height > ar[i]:
                amount += deciding_height - ar[i]

        print(f"Total quantity of water stored = {amount}")


obj = Histogram()
obj.main()
