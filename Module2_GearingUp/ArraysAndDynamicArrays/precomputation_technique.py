# Pre-computation Techniques
# In this lecture, we will learn the applications of pre-computation techniques like prefix sum, prefix max, suffix max etc. Pre-processing helps in efficiently answering multiple queries and is used with linear data structures like arrays and vectors.
#
# In the given problem, there is an integer array ‘Arr[N]’ and we have to print the individual sum of ‘Q’ subarrays whose first index - ‘l’ and the last index - ‘r’ is given.
#
# Approach:
#
# Brute force - Create two nested loops to print the sum of different subarrays respectively.
# Time Complexity: O(Q*N)
# Space Complexity: O(1)
#
# Prefix sum - We can pre-compute the prefix sum of the array and store it in an array PS[N].
# PS[ i ] = Arr[ i ] + PS[ i - 1 ];
#
#  We can then print the sum of subarray(l, r) within O(1) time complexity.
#
# Sum of Subarray(l, r) = PS[ r ] - PS[ l - 1 ]  (l>=1)
#                                     = PS[ r ]                     (l==0)
#
# Time Complexity: O(N+Q)
#
# Space Complexity: O(N)
#
# Note: It can also be solved in O(1) space complexity if we use the original array to store the prefix sum.

class PrefixOperation:
    def main(self):
        print("Enter the length of the array")
        n = int(input())
        print("Enter the array elements")
        ar = list(map(int, input().strip().split()))[:n]
        print("The array is:")
        print(ar)
        print("Enter the number of queries")
        q = int(input())
        while q:
            # prefix sum
            opr = ar.copy()
            l, r = map(int, input().strip().split())
            for i in range(1, n):
                opr[i] += opr[i - 1]
            if l == 0: # To handle index out of bound exception
                ps = opr[r]
            else:
                ps = opr[r] - opr[l - 1]
            print(f"The prefix sum for elements between {l} and {r} = {ps}")
            q -= 1


obj = PrefixOperation()
obj.main()
