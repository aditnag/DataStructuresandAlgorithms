# Lecture 11: Processing Queries Efficiently
# In this lecture, we will learn how to process multiple queries for a 2d matrix efficiently.
#
# Here, we have been given a 2d matrix Arr[M][N] and we have to find the sum of the ‘Q’ sub-matrices defined by TL(i1, j1) & BR(i2, j2) cells.
#
# Approach:
#
# Brute Force - Calculate the sum of each submatrix individually to answer the query.
# Time complexity: O(Q*(M*N))
# Space complexity: O(1)
#
# Prefix Sum -  Think of applying the concept of Prefix sum in a 2D array.
# Arrays_L10(1)
# Since we now know how to define the Prefix sum for a 2D array, we can create a prefix sum matrix PS[ M ][ N ].
#
# For a submatrix: TL(i1, j1) and BR(i2, j2) -
#
# Arrays_L10(2)
# Required Sum = PS[i2][j2] - A1 - A2 + A3 where,
#
# A1 = PS[i1-1][j2]           ; i1>=1
# A2 = PS[i2][j1-1]          ;j1>=1
# A3 = PS[i1-1][j1-1]        ;i1>=1 & j1>=1
#
# Time complexity: O(Q+MN)
# Space complexity: O(MN)
#
# Note: Please check the boundary conditions to ensure that the array indices are non-negative.

class ProcessingQueriesEfficiently:
    def precomputation(self, mat, temp, n, m):
        for i in range(m):
            temp[]


    def main(self):
        print("Enter the row and column of the matrix")
        n, m = map(int, input().strip().split())

        print("Enter the number of Queries to be performed")
        q = int(input())

        # matrix input
        print("Enter the matrix elements")
        matrix = []
        for i in range(n):
            matrix.append([int(j) for j in input().split()])

