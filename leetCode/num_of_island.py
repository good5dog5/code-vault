#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess

# board = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
board = []

def numIslands(grid):
    def helper(i, j, m, n, grid):

        if i == m or j == n or i < 0 or j < 0 or grid[i][j] != "1" :
            return

        grid[i][j] = "2"

        helper(i+1, j, m, n, grid)
        helper(i, j+1, m, n, grid)
        helper(i-1, j, m, n, grid)
        helper(i, j-1, m, n, grid)

    if len(board) == 0:
        return 0

    m,n = len(grid), len(grid[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                cnt += 1
                helper(i, j, m, n, grid)
    return cnt

n = numIslands(board)
print(n)
