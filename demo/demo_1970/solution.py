import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.latestDayToCross(*test_input)

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        pass

