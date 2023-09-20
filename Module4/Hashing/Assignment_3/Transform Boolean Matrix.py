# cook your dish here
def matrixoperation(grid, r, c):
    row = [0] * r
    col = [0] * c
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                row[i] = 1
                col[j] = 1
    for i in range(r):
        for j in range(c):
            if row[i] == 1 or col[j] == 1:
                grid[i][j] = 1

    for i in range(r):
        for j in range(c):
            print(grid[i][j], end=" ")
        print()


t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        row = list(map(int, input().split()))
        grid.append(row)
    matrixoperation(grid, r, c)
