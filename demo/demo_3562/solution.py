import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(*test_input)

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        pass

