__author__ = "Shihao Yu"
"""
source: https://leetcode.com/problems/valid-sudoku/
date: 11-2-2015
----------------
problem:
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.
----------------
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            s = set()
            for j in board[i]:
                if j != '.':
                    if j not in s:
                        s.add(j)
                    else:
                        return False
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] != '.':
                    if board[j][i] not in s:
                        s.add(board[j][i])
                    else:
                        return False
        for i in range(9):
            offsetX = i / 3 * 3
            offsetY = i % 3 * 3
            s = set()
            for j in range(9):
                innerX = j / 3
                innerY = j % 3
                num = board[offsetX + innerX][offsetY + innerY]
                if num != '.':
                    if num not in s:
                        s.add(num)
                    else:
                        return False
        return True
