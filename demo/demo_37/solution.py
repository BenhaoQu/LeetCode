import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        self.solveSudoku(test_input)
        return test_input

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass

