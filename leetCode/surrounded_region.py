#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess

board = [['O','O'], ['O','O']]
# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

def solve(board):
    print("in")
    def helper(i, j, m, n, grid):
        print(i, j, grid)
        if  i == m or j == n or i < 0 or j < 0 or grid[i][j] == "X":
            return

        grid[i][j] = "$"

        helper(i+1, j, m, n, grid)
        helper(i, j+1, m, n, grid)
        helper(i-1, j, m, n, grid)
        helper(i, j-1, m, n, grid)

    if len(board) == 0 or len(board[0]) == 0:
        return 0
    m,n = len(board), len(board[0])
    
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0 or i == m-1 or j == n-1) and board[i][j] == "O":
                helper(i, j, m, n, board)
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                board[i][j] = "X"
            if board[i][j] == "$":
                board[i][j] = "O"
    print(board)
print(board)

solve(board)


