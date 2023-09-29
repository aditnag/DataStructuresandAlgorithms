class Solution:
    @staticmethod
    def isSafe(i, j, grid):
        return len(grid) > i >= 0 == grid[i][j] and 0 <= j < len(grid[0])

    def cp(self, i, j, grid, isvisited):
        if grid[i][j] == 2:
            return all(all(row) for row in isvisited)
        isvisited[i][j] = 1
        targetsum = 0
        if self.isSafe(i, j + 1, grid) and (isvisited[i][j + 1]) == 0:
            targetsum += self.cp(i, j + 1, grid, isvisited)
        if self.isSafe(i, j - 1, grid) and isvisited[i][j - 1] == 0:
            targetsum += self.cp(i, j - 1, grid, isvisited)
        if self.isSafe(i + 1, j, grid) and isvisited[i + 1][j] == 0:
            targetsum += self.cp(i + 1, j, grid, isvisited)
        if self.isSafe(i - 1, j, grid) and isvisited[i - 1][j] == 0:
            targetsum += self.cp(i - 1, j, grid, isvisited)
        isvisited[i][j] = 0
        return targetsum

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        itr, jtr = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    itr, jtr = (i, j)
        isvisited = [[0] * len(grid[0]) for _ in range(len(grid))]
        return self.cp(itr, jtr, grid, isvisited)
