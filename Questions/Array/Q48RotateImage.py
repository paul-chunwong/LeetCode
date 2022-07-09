"""
Q48 - Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],        Output:  [[7,4,1],
                 [4,5,6],                  [8,5,2],
                 [7,8,9]]                  [9,6,3]]

"""
from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    # From YouTube

    # After the following:
    #      [[1,2,3],           [[1,4,7],
    #       [4,5,6],    ->      [2,5,8],
    #       [7,8,9]]            [3,6,9]]
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # After the following:
    #      [[1,4,7],           [[7,4,1],
    #       [2,5,8],    ->      [8,5,2],
    #       [3,6,9]]            [9,6,3]]
    for r in matrix:
        r.reverse()
