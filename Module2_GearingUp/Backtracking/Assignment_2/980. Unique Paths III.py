from typing import List


class Solution:
    @staticmethod
    def isSafe(i, j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] >= 0

    def cp(self, i, j, grid, isvisited, remain):
        if grid[i][j] == 2 and remain == 1:
            return 1
        isvisited[i][j] = 1
        targetsum = 0
        remain -= 1
        if self.isSafe(i, j + 1, grid) and (isvisited[i][j + 1]) == 0:
            targetsum += self.cp(i, j + 1, grid, isvisited, remain)
        if self.isSafe(i, j - 1, grid) and isvisited[i][j - 1] == 0:
            targetsum += self.cp(i, j - 1, grid, isvisited, remain)
        if self.isSafe(i + 1, j, grid) and isvisited[i + 1][j] == 0:
            targetsum += self.cp(i + 1, j, grid, isvisited, remain)
        if self.isSafe(i - 1, j, grid) and isvisited[i - 1][j] == 0:
            targetsum += self.cp(i - 1, j, grid, isvisited, remain)
        isvisited[i][j] = 0
        return targetsum

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        itr, jtr = 0, 0
        non_obstacles = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    itr, jtr = (i, j)
                if grid[i][j] >= 0:
                    non_obstacles += 1
        isvisited = [[0] * len(grid[0]) for _ in range(len(grid))]
        return self.cp(itr, jtr, grid, isvisited, non_obstacles)
