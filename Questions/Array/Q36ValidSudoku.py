"""
Q36 - Valid Sudoku


Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1,
except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

"""
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # Check row
    for r in range(9):
        for c in range(9):
            if board[r].count(board[r][c]) > 1 and board[r][c] != '.':
                return False

    # Check square
    r = 0
    while r < 9:
        c = 0
        while c < 9:
            resultList = []
            resultList.append(board[r][c])
            resultList.append(board[r][c + 1])
            resultList.append(board[r][c + 2])
            resultList.append(board[r + 1][c])
            resultList.append(board[r + 1][c + 1])
            resultList.append(board[r + 1][c + 2])
            resultList.append(board[r + 2][c])
            resultList.append(board[r + 2][c + 1])
            resultList.append(board[r + 2][c + 2])
            for i in resultList:
                if i != '.' and resultList.count(i) > 1:
                    return False
            c = c + 3
        r = r + 3

    # Check column
    r = 0
    while r < 9:
        resultList2 = []
        c = 0
        while c < 9:
            resultList2.append(board[c][r])
            c = c + 1
        for i in resultList2:
            if i != '.' and resultList2.count(i) > 1:
                return False
        r = r + 1

    return True


print(isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."],
                     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                     [".", ".", ".", "5", "6", ".", ".", ".", "."],
                     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                     [".", ".", ".", "7", ".", ".", ".", ".", "."],
                     [".", ".", ".", "5", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", ".", "."]]))

print(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
