import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.toLowerCase(test_input)

    def toLowerCase(self, s: str) -> str:
        return s.lower()
