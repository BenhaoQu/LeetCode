import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkMove(*test_input)

    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        pass

