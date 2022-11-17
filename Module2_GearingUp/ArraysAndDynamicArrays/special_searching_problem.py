# Lecture 12: A Special Searching Problem
# In this lecture, we will discuss a special type of searching problem. Here, we have been given a 2d matrix Arr[M][N] with sorted rows & columns along with a key ‘k’. We have to return the coordinates of the key if it is present in the matrix otherwise return (-1, -1).
#
#
# Approach:
#
# Brute Force - Traverse the matrix to search for the key ‘k’ and return its coordinates if present otherwise returns (-1,-1).
# Time complexity: O(MN)
# Space complexity: O(1)
#
# Binary Search - Since the rows are sorted, therefore we can think of applying binary search while searching in each row.
# Time complexity: O(MlogN)
# Space complexity: O(1)
#
# The above time complexity could have been achieved even if only the rows were sorted but here the columns are also sorted too. Can we use this fact to optimise it further?
#
# Can we somehow curtail the search space by traversing the matrix in a clever way?
# This approach involves observing the elements of the matrix and smartly traversing it to find the key. We can start traversing either from the Top Right(TR) or the Bottom Left(BL) cell of the matrix and move accordingly, comparing the key with the matrix elements.
# Special Search
# Time complexity: O(M+N)
# Space complexity: O(1)
#
# Note: We can not start the traversal from Top Left(TL) or Bottom Right(BR) cell because their neighbouring elements are either greater or smaller to them, therefore we do not get any clue on which direction we should move next.

class SpecialSearchingProblem:
    def main(self):
        print("Enter the rows and columns")
        m, n = map(int, input().strip().split())

        print("Enter the matrix elements such that each row is sorted in asc and each column is sorted in asc order!")
        matrix = []
        for i in range(m):
            matrix.append([int(j) for j in input().split()])

        print("Enter the key to be searched")
        key = int(input())

        i = 0
        j = n - 1
        while i < m and j >= 0:
            if key == matrix[i][j]:
                print(f"{key} is present")
                break
            elif key > matrix[i][j]:
                i += 1
            else:
                j -= 1


obj = SpecialSearchingProblem()

obj.main()
