# Lecture 14: Array Rearrangement
# In this lecture, we will discuss a problem based on Array rearrangement. Here we have been given a permutation array ‘Arr[N]’ and we have to rearrange it such that - if Arr[ i ] = j, then Arr[ j ] = i.
# Input: Arr[4] = { 1, 3, 0, 2 }
# Output: Arr[4] = { 2, 0, 3, 1 }
#
# Approach:
#
# Using a temporary array - When we try to place the elements at their new indices at that time we may lose the old elements present at those indices. Therefore we can use a temporary array to store the elements at their desired position.
# Time complexity: O(N)
# Space complexity: O(N)
#
# Can we do it without using any auxiliary array?
#
# The problem while replacing the old value with the new value is that the previous elements are being overwritten. But can not we do it in a cycle?
# Yes, we can!
# Cycles
# But as evident from the figure, there may not necessarily be a single cycle. It can contain multiple cycles and thus we would need to track if an element has already been modified in some other cycle or not.
#
# For this, we can make use of the fact that 0<=Arr[ i ]<=N-1, therefore we can add 1 to the elements and multiply them by -1.
# ie. If element at index ‘i’ has been visited then, Arr[ i ] -> - ( Arr[ i ] + 1 )
#
# Time complexity: O(N)
# Space complexity: O(1)

class ArrayRearrangement:
    def main(self):
        print("Enter the length of the array")
        n = int(input())
        print("Enter the array elements")
        ar = list(map(int, input().strip().split()))[:n]
        for i in range(n):
            if ar[i] >= 0:
                index = ar[i]
                value = i
                while index != i:
                    temp = ar[index]
                    ar[index] = -(value + 1)
                    value = index
                    index = temp
                ar[index] = -(value + 1)

        for i in range(n):
            ar[i] = (-1 * ar[i]) - 1

        for ele in ar:
            print(ele, end=" ")


obj = ArrayRearrangement()
obj.main()
