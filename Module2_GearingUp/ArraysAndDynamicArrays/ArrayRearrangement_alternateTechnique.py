# Lecture 15: Array Rearrangement: Alternate Technique
# In this lecture, we will tackle the previous question on array rearrangement with an alternate approach.
#
# The problem that we were facing earlier was to preserve the old value while placing the new value at its position.
#
# So, can we think of a number that can represent both the old and the new value together?
# Hint: Use the fact that 0<=Arr[ i ]<=N-1
#
# Let the modified element be x such that x = N * new_value + old_value. We would be able to extract both the new & the old value from x as -
#
# old_value = x%N
# new_value = x/N
#
# Once we have modified all the elements then we can divide them by N to find out the new values at each array index.
# Time complexity: O(N)
# Space complexity: O(1)
#
# Note:
#
# Can we do it the other way around ie. x = N*old_value + new_value.
# We can not! since for any untouched element, x/N = 0 (Arr[i]<N-1), therefore we will not be able to extract the old value.
# In the above method, we are multiplying N with the new_value, which may lead to integer overflow if N is larger than 10^4. Therefore, it may not work in every case.

class ArrayRearrangementAT:
    def main(self):
        print("Enter the length of the array")
        n = int(input())

        print("Enter the array elements")
        ar = list(map(int, input().strip().split()))[:n]

        """"
        To do: if ar[i] = j then ar[j] = i. 
        For this the elements should be permutation of n (size of the array) and less than n
        """
        for i in range(n):
            old_value = ar[i] % n
            ar[old_value] = n * i + ar[old_value]

        # new arrangement
        for i in range(n):
            ar[i] = ar[i] // n

        print("New arrangement:")
        for elements in ar:
            print(elements, end=" ")


obj = ArrayRearrangementAT()
obj.main()
